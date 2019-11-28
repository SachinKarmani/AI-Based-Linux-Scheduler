from Scheduler import Scheduler
from pandas import read_excel
import pickle

sch = Scheduler()

# ID, Arrival time, Execution time
processes = read_excel('alldata_test.xlsx', index=False)

#if "name" in list(processes.columns):
labelencoder_X = pickle.load(open('final_encod.sav', 'rb'))
processes["name"] = labelencoder_X.transform(processes["name"])
processes['execution'] = processes['execution'] * 1000
processes['Arrival'] = processes['Arrival'] * 1000

processes1 = processes.values.tolist()
x = sch.scheduleRBTree(processes1)


"""

normal
COMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS 
------------------------------------------------------------------------
1.Total Number of processes :  14
2.Total Running Time:  34561.611  seconds
3.Running time per process: 2468.686  seconds
4.Total Wait Time : 81499.439  seconds
5.Average Wait Time : 5821.388   seconds
6.Total turn around time:  86125.05  seconds
7.Average turn around time:  6151.789  seconds
8.Total context switches:  5147
9.Average context switches:  367.643

with model: //round
COMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS 
------------------------------------------------------------------------
1.Total Number of processes :  14
2.Total Running Time:  34551.611  seconds
3.Running time per process: 2467.972  seconds
4.Total Wait Time : 81388.077  seconds
5.Average Wait Time : 5813.434   seconds
6.Total turn around time:  86013.688  seconds
7.Average turn around time:  6143.835  seconds
8.Total context switches:  5142
9.Average context switches:  367.286

with model: //ceil
COMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS 
------------------------------------------------------------------------
1.Total Number of processes :  14
2.Total Running Time:  34561.611  seconds
3.Running time per process: 2468.686  seconds
4.Total Wait Time : 81486.833  seconds
5.Average Wait Time : 5820.488   seconds
6.Total turn around time:  86112.444  seconds
7.Average turn around time:  6150.889  seconds
8.Total context switches:  5150
9.Average context switches:  367.857

with model: //round curr * q
COMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS 
------------------------------------------------------------------------
1.Total Number of processes :  14
2.Total Running Time:  28602.611  seconds
3.Running time per process: 2043.044  seconds
4.Total Wait Time : 53352.751  seconds
5.Average Wait Time : 3810.911   seconds
6.Total turn around time:  57978.362  seconds
7.Average turn around time:  4141.312  seconds
8.Total context switches:  4133
9.Average context switches:  295.214

with model: //ceil curr * q
COMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS 
------------------------------------------------------------------------
1.Total Number of processes :  14
2.Total Running Time:  28617.611  seconds
3.Running time per process: 2044.115  seconds
4.Total Wait Time : 53428.142  seconds
5.Average Wait Time : 3816.296   seconds
6.Total turn around time:  58053.753  seconds
7.Average turn around time:  4146.697  seconds
8.Total context switches:  4137
9.Average context switches:  295.5

with model: // round curr / 1.5
COMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS 
------------------------------------------------------------------------
1.Total Number of processes :  14
2.Total Running Time:  27401.611  seconds
3.Running time per process: 1957.258  seconds
4.Total Wait Time : 52451.127  seconds
5.Average Wait Time : 3746.509   seconds
6.Total turn around time:  57076.738  seconds
7.Average turn around time:  4076.91  seconds
8.Total context switches:  3304
9.Average context switches:  236.0

with model: //ceil curr / 1.5
COMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS 
------------------------------------------------------------------------
1.Total Number of processes :  14
2.Total Running Time:  27431.611  seconds
3.Running time per process: 1959.401  seconds
4.Total Wait Time : 52565.81  seconds
5.Average Wait Time : 3754.701   seconds
6.Total turn around time:  57191.421  seconds
7.Average turn around time:  4085.101  seconds
8.Total context switches:  3313
9.Average context switches:  236.643







"""
