from Process import Process, find_weight
from RedBlackTree import RedBlackTree
import pickle
from math import floor


class Scheduler:

    def scheduleRBTree(self, processes, total_quantum=2):

        processes.sort(key=lambda elem: elem[2])
        no_of_processes = len(processes)
        queue = []

        CLOCK = 0
        totalWaitTime = 0
        totalContextSwitches = 0
        totalTurnAroundTime = 0
        tr_ts = []
        
        while(processes):

            print("Time: ", round(CLOCK,3), "\n")
            
            # processes[0][1] = arrival time of first process in sorted list
            # using while loop as it is possible that in the queue there are 2+ processes having
            # same arrival time, therefore we will check unitil <= CLOCK condition
            while (True):
                if processes and processes[0][2] <= CLOCK:
                    curr_proc =  processes.pop(0)
                    queue.append(curr_proc)
                    queue.sort(key=lambda elem: elem[0])
                    
#                    Process(rt, newId=curr_proc[1], newArrivalTime=curr_proc[2], expected = expected,
#                            newExecTime=curr_proc[0], niceVal=curr_proc[3], min_vr = min_vr)
                else:
                    break
                
            if queue:
                curr_node = queue.pop(0)
                    
                totalWaitTime += (CLOCK - curr_node[2])
                CLOCK = CLOCK + curr_node[0]
                totalTurnAroundTime += (CLOCK - curr_node[2])
                tr_ts.append((CLOCK - curr_node[2]) / curr_node[0])
        

#                CLOCK += 0.25
                totalContextSwitches += 1
            
            CLOCK += 1
                

        print("\nCOMPLETELY FAIR SCHEDULING USING RED BLACK TREES- PERFORMANCE METRICS ")
        print("------------------------------------------------------------------------")
        print("1.Total Number of processes : ", no_of_processes)
        print("2.Total Running Time: ",  round(CLOCK,3),  " seconds")
        print("3.Running time per process:",  round(CLOCK / no_of_processes,3), " seconds")
        print("4.Total Wait Time :",  round(totalWaitTime,3), " seconds")
        print("5.Average Wait Time :",  round((totalWaitTime / no_of_processes),3) ,  "  seconds")
        print("6.Total turn around time: ",  round(totalTurnAroundTime,3) , " seconds")
        print("7.Average turn around time: ", round( (totalTurnAroundTime / no_of_processes),3) ,  " seconds")
        print("8.Total context switches: ",  round(totalContextSwitches) )
        print("9.Average context switches: ", round( (totalContextSwitches / no_of_processes),3))
        print("10.Average tr_ts: ", round( sum(tr_ts) / len(tr_ts) ,3))
        print("11. tr_ts: ", tr_ts)
