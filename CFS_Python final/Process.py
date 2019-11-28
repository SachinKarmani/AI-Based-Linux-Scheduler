class Process:

    def __init__(self, rbtree,  newId,  newArrivalTime,  newExecTime, niceVal, min_vr, expected ):

        self.timeInCPU=0
        self.processId = newId
        self.execTime = newExecTime
        self.fix = newExecTime
        self.arrivalTime = newArrivalTime
        self.waitTime = 0
        self.unfairness = min_vr
        self.startTime = 0
        self.rbt = rbtree
        self.rbt.add(self)
        self.turnAroundTime = 0
        self.niceValue = niceVal
        self.expected = expected
        self.weight = 1024 / (1.25 ** niceVal)
        self.context_switch = 0
        
        
def find_weight(niceVal):
    return 1024 / (1.25 ** niceVal)
