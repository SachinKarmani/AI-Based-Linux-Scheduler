from Process import Process, find_weight
from RedBlackTree import RedBlackTree
import pickle
from math import floor


class Scheduler:

    def scheduleRBTree(self, processes, total_quantum=2):

        rt = RedBlackTree()
        model = pickle.load(open('final_model.sav', 'rb'))

        processes.sort(key=lambda elem: elem[2])
        no_of_processes = len(processes)
        weights = {}
        model_result = {}

        CLOCK = 0
        min_vr = 0
        totalWaitTime = 0
        totalContextSwitches = 0
        totalTurnAroundTime = 0
        tr_ts = []
        
        while(processes or rt.count >= 1):

            print("Time: ", round(CLOCK,3), "\n")
            
            # processes[0][1] = arrival time of first process in sorted list
            # using while loop as it is possible that in the queue there are 2+ processes having
            # same arrival time, therefore we will check unitil <= CLOCK condition
            while (True):
                if processes and processes[0][2] <= CLOCK:
                    CLOCK = CLOCK + 1
                    curr_proc =  processes.pop(0)
                    expected = 0
                    expected = model.predict([curr_proc[4:]])[0]
                    Process(rt, newId=curr_proc[1], newArrivalTime=curr_proc[2], expected = expected,
                            newExecTime=curr_proc[0], niceVal=curr_proc[3], min_vr = min_vr)
                    weights[curr_proc[1]] = find_weight(curr_proc[3])
                    model_result[curr_proc[1]] = expected
                else:
                    break
                
            total_weight = sum(weights.values())
            rt.printRBTree()
            print('###')

            curr_node = rt.delete_node()
            
            # increase quantum by factor q_i
            q_i = 1.5
            
            if curr_node:
                # rt.count + 1 coz current process has been removed from tree and we still need
                # to include it in count
                
                # change
                quantum = total_quantum * curr_node.process.weight / total_weight
                
                if q_i:
                    curr_expect = curr_node.process.expected * 1000
                    
     #               target_num = round(curr_expect/quantum)
     #               target_num = round(curr_expect *  quantum)
                    target_num = round(curr_expect / (q_i * quantum))
                    
                    quantum = curr_expect / target_num

                if (curr_node.process.execTime > quantum):
                    CLOCK = CLOCK + quantum
                    curr_node.process.timeInCPU = curr_node.process.timeInCPU + quantum
                    curr_node.process.execTime = curr_node.process.execTime - quantum
                    curr_node.process.unfairness = curr_node.process.unfairness + (quantum * 1024 /curr_node.process.weight)
#                    curr_node.process.unfairness = curr_node.process.unfairness + (curr_node.process.timeInCPU * 1024 /curr_node.process.weight)
                    min_vr = curr_node.process.unfairness
                    rt.add(curr_node.process)

                else:
                    CLOCK = CLOCK + curr_node.process.execTime
                    curr_node.process.timeInCPU = curr_node.process.timeInCPU + curr_node.process.execTime
                    curr_node.process.waitTime = CLOCK - curr_node.process.arrivalTime - curr_node.process.timeInCPU
                    totalWaitTime += curr_node.process.waitTime
                    curr_node.process.turnAroundTime = CLOCK - curr_node.process.arrivalTime
                    tr_ts.append(curr_node.process.turnAroundTime / curr_node.process.fix)
                    totalTurnAroundTime += curr_node.process.turnAroundTime
                    del weights[curr_node.process.processId]

                CLOCK += 0.25
                totalContextSwitches += 1
                
            else:
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
