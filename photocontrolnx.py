
import subprocess
import time
import logging
import threading
from os import remove




class GphotoCmdInt():
    def __init__(self):
        self.lastcmd=''
        self.lastout = []
        self.maincall = 'gphoto2'
        self.commands =  {  'summary' : '--summary',
                            'getConfigs': '--list-config',
                            'getVal' : '--get-config',
                            'setVal' : '--set-config-value',
                            'captDown' : '--capture-image-and-download',
                            'capt' : '--capture-image',
                            'filen':'--filename'}
    def exeCommand(self):
        p = subprocess.Popen(self.lastcmd, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE)
        p.wait()
        self.lastout = p.stdout.readlines()
        return self.lastout 
    def getSummary(self):
        self.lastcmd = [self.maincall,self.commands['summary']]
        out = self.exeCommand()
        return out
    def getModel(self):
        model = ''
        out = self.getSummary()
        for line in out:
            if "Model:" in line:
                model = " ".join(line.split()[1:])
        return model
    def getConfigs(self):
        self.lastcmd = [self.maincall,self.commands['getConfigs']]
        out = self.exeCommand()
        return [(x.split('/')[len(x.split('/'))-1:][0]).split('\n')[0] for x in out ]
    def getChoices(self,config):
        self.lastcmd = [ self.maincall, self.commands['getVal'],config ]
        out = self.exeCommand()
        choices = []
        for line in out:
            if "Choice:" in line:
                tup = line.split()[1:]
                tupb = ' '.join(tup[1:])
                choices.append([tup[0],tupb])
        return  dict(choices)
    def getValue(self, config):
        self.lastcmd = [ self.maincall, self.commands['getVal'],config ]
        out = self.exeCommand()
        value=''
        for line in out:
            if "Current:" in line:
                value=(line.split()[1:])
        return  value[0]
    def setValue(self, config, value):
        self.lastcmd = [ self.maincall, 
                    self.commands['setVal'],
                    '='.join([config,value]) ]
        out = self.exeCommand()
        return  out
    def capture(self):
        self.lastcmd = [ self.maincall, self.commands['capt']]
        out = self.exeCommand()
        return  out
    def captureFile(self,filename):
        try:
            remove(filename)
        except:
            pass
        self.lastcmd = [ self.maincall, self.commands['captDown'],
                        '='.join([self.commands['filen'],filename])]
        out = self.exeCommand()
        return  out

class Camera():
    def __init__(self):
        self.interface = GphotoCmdInt()
        self.lastcmd = ''
        # Trovar model de camara
        logging.info( "Connecting to Camara")
        self.model = self.interface.getModel()
        logging.info( "Hello "+self.model+" !")
        #   Trovar els posibiliats de la camara
        self.configs = self.interface.getConfigs()
        #   Trovar el rang possible de compensacions
        self.compensations = self.interface.getChoices('exposurecompensation').values()
        self.compensation = self.readCompensation()
    def readCompensation(self):
        logging.info( "Reading Compensation Values")
        logging.info("hello")
        self.compensation = self.interface.getValue('exposurecompensation')
        return self.compensation
    def getCurrentPictureStyle(self):
        return self.interface.getValue('picturestyle')
    def getPictureStyleChoices(self):
        return self.interface.getChoices('picturestyle')      
    def setCurrentPictureStyle(self,picturestyle):
        return self.interface.setValue('picturestyle',picturestyle)           
    def doCapture(self,exposurecompensation ='0',filename = '' ):
        logging.info("Capturing at "+exposurecompensation+", storing at "+filename)
        self.interface.setValue('exposurecompensation',exposurecompensation)
        if filename != '':
            out = self.interface.captureFile(filename)
        else:
            out = self.interface.capture()
        return out



#class StartCapture(threading.Thread):
#    def __init__(self,x):
#        self.__x = x
#        threading.Thread.__init__(self)
#    def run (self):
#          print str(self.__x)




class Capture(threading.Thread):
    def __init__(self, Camera):
        threading.Thread.__init__(self)
        self.interval = 3
        self.shots = 2
        self.currentcam = Camera
        self.compensation = self.currentcam.readCompensation()
        self.hdrexpspan = set(self.currentcam.compensations)
        self.picturestyles = set(self.currentcam.getPictureStyleChoices().values())
        self.picturestyle = self.currentcam.getCurrentPictureStyle()
        self.target="./"
        self.hdr = self.currentcam.readCompensation()
    def setCapture(self, 
            interval, 
            shots, 
            target = ".", 
            hdr = None):
        self.interval = interval
        self.shots = shots
        self.target = target
        if hdr!=None:
            if hdr in self.hdrexpspan :
                self.hdr = hdr
    def getPictureStyle(self):
        return self.picturestyle
    def setPictureStyle(self,picturestyle):
        self.currentcam.setCurrentPictureStyle(picturestyle)
        self.picturestyle = self.currentcam.getCurrentPictureStyle()
    def getPictureStyles(self):
        return self.picturestyles
    def setHDR(self,hdr):
        #comprovar el rang
        if hdr == '0':
            self.hdr=None
        else:  
            self.hdr=hdr
    def getHDR(self):
        return self.hdr
    def setFile(self,file):
        self.target = file
    def getFile(self):
        return self.target
    def setShots(self,shots):
        self.shots=shots
    def getShots(self):
        return self.shots
    def setInterval(self,interval):
        self.interval = interval
    def getInterval(self):
        return self.interval
    def exeCapture(self):
        capPlan = []
        s = 0
        while s < self.shots:
            filebase = self.target+ "/capture_" + str(s)
            if (self.hdr != None) and (self.hdr != "0") :
                capPlan.append( [filebase + "_u.cr2","-"+self.hdr,0] )
                capPlan.append( [filebase + "_n.cr2","0",0] )
                capPlan.append( [filebase + "_o.cr2",self.hdr,self.interval] )
            else:
                capPlan.append( [filebase + ".cr2","0",self.interval] )   
            s = s+1
        for act in capPlan:
            Camera.doCapture(self.currentcam,act[1],act[0])
            time.sleep(act[2])

    def run(self):
        self.exeCapture()
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting No GUI controller")
    n = Camera()
    c = Capture(n)
#c.setCapture(1, 2, "test", "0")

#c.exeCapture()
