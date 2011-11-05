
import subprocess
import time

class Camera():
    lastcmd = ''
    model = ''
    configs = []
    compensations = ["0.3","0.6", "1.0","1.3", "1.6","2"]
    compensation = '0'
    def __init__(self):
        # Trovar model de camara
        self.lastcmd = ["gphoto2", "--summary"]
        p = subprocess.Popen(self.lastcmd, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE)
        p.wait()
        for line in p.stdout:
            if "Model:" in line:
                self.model = " ".join(line.split()[1:])
        #   Trovar els posibiliats de la camara
        self.configs = []
        self.lastcmd = ["gphoto2", "--list-config"]
        p = subprocess.Popen(self.lastcmd, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE)
        p.wait()
        for line in p.stdout:
            self.configs.append(line.split("\n")[0])
    def readCompensation(self):
        self.lastcmd = ["gphoto2", "--get-config", "exposurecompensation"]
        p = subprocess.Popen(self.lastcmd, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE)
        p.wait()
        for line in p.stdout:
            self.configs.append(line.split("\n")[0])
            if "Current:" in line:
                self.compensation = " ".join(line.split()[1:])
        return self.compensation
    def doCapture(self,exposurecompensation ='0',filename = None ):
        file=''
        if filename != None:
            file="--filename="+filename
        self.lastcmd = ["gphoto2", "--set-config", 
                        "exposurecompensation=" + exposurecompensation]
        p = subprocess.Popen(self.lastcmd, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE)
        p.wait()
        self.lastcmd = ["gphoto2", "--capture-image-and-download", file]
        p = subprocess.Popen(self.lastcmd, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE)
        p.wait()
    
class Capture( ):
    
    interval = 30
    shots = 1000
    hdrexpspan = []
    hdr = "0"
    target="./"
    currentcam = None
    def __init__(self, Camera):
        self.currentcam = Camera
        self.compensation = self.currentcam.readCompensation()
        self.hdrexpspan = set(self.currentcam.compensations)
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
    def exeCapture(self):
        capPlan = []
        s = 0
        while s < self.shots:
            filebase = self.target+ "/capture_" + str(s)
            if self.hdr != None:
                capPlan.append( [filebase + "_u.cr2","-"+self.hdr,0] )
                capPlan.append( [filebase + "_n.cr2","0",0] )
                capPlan.append( [filebase + "_o.cr2",self.hdr,self.interval] )
            s = s+1
        for act in capPlan:
            print(str(act))
            Camera.doCapture(self.currentcam,act[1],act[0])
            time.sleep(act[2])
    
    
    
#n = Camera()
#c = Capture(n)
#c.setCapture(10, 2, "test", "1.6")

#c.exeCapture()
