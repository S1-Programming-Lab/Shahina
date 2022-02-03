class time():
    def __init__(self,h,m,s):
        self.hr=h
        self.min=m
        self.sec=s
    def __add__(self,other):
        tempsec+self.sec+other.sec
        tempmin=tempsec/60
        self.sec=int(tempsec%60)
        self.min=self.min+other.min+tempmin
        temphr=self.min/60
        self.min=int(self.min%60)