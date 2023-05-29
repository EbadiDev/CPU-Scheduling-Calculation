from matplotlib.ticker import MaxNLocator
from prettytable import PrettyTable
import matplotlib.pyplot as plt

class RoundRobinScheduler:
    # constructor
    def __init__(self):
        self.table = PrettyTable() # showing informations
        self.start_time = [] #
        self.finish_time = []
        self.executed_process = [] # to save processes' execution sequence
        self.first_time = []
        
    # input process data
    def inputProcessData(self, num):
        data = []
        # input information
        for i in range(num):
            process_id = i + 1
            arrival_time = int(input(f"Enter Arrival Time of Process {process_id}: "))
            burst_time = int(input(f"Enter Burst Time of Process {process_id}: "))
            # 0 means not executed and 1 means execution is complete
            data.append([process_id, arrival_time, burst_time, 0, burst_time])
        q = int(input('Enter Time Period: '))
        self.schedulingProcess(data, q)

    def schedulingProcess(self, data, q):
        self.start_time = []
        self.finish_time = []
        self.executed_process = [] # to save processes' execution sequence
        self.first_time = []
        start_time = self.start_time
        finish_time = self.finish_time
        executed_process = self.executed_process
        ready_queue = [] # to stores all the processes that have already arrived
        s_time = 0
        # Sort processes according to the Arrival Time
        data.sort(key=lambda x: x[1])
        
        # execute processes until all the processes are complete
        while True:
            notArrived_queue = [] # to store all the processes that haven't arrived yet
            # check if the next process is not a part of ready_queue
            for i in range(len(data)):
                    #arrivaltime             #is executed? (0=no)
                if data[i][1] <= s_time and data[i][3] == 0:
                    present = 0
                    
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if data[i][0] == ready_queue[k][0]:
                                present = 1
                    # add a process to the ready_queue if it is not already present in it                                
                    if present == 0:
                                           #Process ID  #Arrival Time #burst Time # burst Time 2
                        ready_queue.append([data[i][0], data[i][1], data[i][2], data[i][4]])
                    # make sure that the recently executed process is appended at the end of ready_queue
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k)) # save executed last
                elif data[i][3] == 0:
                    notArrived_queue.append([data[i][0], data[i][1], data[i][2], data[i][4]])

            if len(ready_queue) == 0 and len(notArrived_queue) == 0:
                break

            if len(ready_queue) != 0:
                # If process has remaining burst time greater than the time period,
                # it will execute for a time period equal to time period and then switch
                if ready_queue[0][2] > q:
                    start_time.append(s_time)
                    s_time = s_time + q
                    f_time = s_time
                    finish_time.append(f_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(data)):
                        # to find which process is executing right now and store in j
                        if data[j][0] == ready_queue[0][0]:
                            break
                    # burttime = burstime - time slice
                    data[j][2] = data[j][2] - q
                    # remove from ready queue list
                    ready_queue.pop(0)
                # If a process has a remaining burst time less than or equal to time period,
                # it will complete its execution                    
                elif ready_queue[0][2] <= q:
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    f_time = s_time
                    finish_time.append(f_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(data)):
                        if data[j][0] == ready_queue[0][0]:
                            break
                    data[j][2] = 0
                    data[j][3] = 1
                    data[j].append(f_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < notArrived_queue[0][1]:
                    s_time = notArrived_queue[0][1]
                if notArrived_queue[0][2] > q:
                    # If process has remaining burst time greater than the time period,
                    # it will execute for a time period equal to time period and then switch                    
                    start_time.append(s_time)
                    s_time = s_time + q
                    f_time = s_time
                    finish_time.append(f_time)
                    executed_process.append(notArrived_queue[0][0])
                    for j in range(len(data)):
                        if data[j][0] == notArrived_queue[0][0]:
                            break
                    data[j][2] = data[j][2] - q
                # If a process has a remaining burst time less than or equal to time period,
                # it will complete its execution                    
                elif notArrived_queue[0][2] <= q:
                    start_time.append(s_time)
                    s_time = s_time + notArrived_queue[0][2]
                    f_time = s_time
                    finish_time.append(f_time)
                    executed_process.append(notArrived_queue[0][0])
                    for j in range(len(data)):
                        if data[j][0] == notArrived_queue[0][0]:
                            break
                    data[j][2] = 0
                    data[j][3] = 1
                    data[j].append(f_time)
        # store first time executing             
        uniq_process = set()
        for i in range(len(executed_process)):
            process_id = executed_process[i]
            if process_id not in uniq_process:
                print(f"P[{process_id}] = {start_time[i]}")
                uniq_process.add(process_id)
                self.first_time.append(start_time[i])
        
        turnaround = self.calculateTurnaroundTime(data)
        waiting = self.calculateWaitingTime(data)
        response = self.calculateResponseTime(data)
        self.printData(data, turnaround, waiting, response, executed_process)
        # make plot
        self.showPlot(executed_process, q, start_time, finish_time)

    def showPlot(self, executed_process, q, start_time, finish_time):
        
        dic = {}
        for i in range(len(executed_process)):
            try:
                dic[str(executed_process[i])].extend([(start_time[i], finish_time[i] - start_time[i])])
            except:
                dic[str(executed_process[i])] = [(start_time[i], finish_time[i] - start_time[i])]

        fig, ax = plt.subplots()
        i = 0
        color = 1
        for item, item2 in dic.items():
            ax.broken_barh(item2, (10 + i, 10), facecolors=('C' + str(color)))
            color += 1
            i += 10

        ax.set_xlabel(f'Round Robin Process Scheduling, Time Slice:{q}')
        ax.set_yticks(list(range(10, len(dic) * 10 + 1, 10)))
        ax.set_yticklabels(dic.keys())
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.invert_yaxis()
        ax.autoscale()
        plt.grid(True)
        plt.show()

    def calculateTurnaroundTime(self, data):
        """
        calculate each process turnaround time and append it at the end of process data list
        return average turnaround time
        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        total_turnaround_time = 0
        for i in range(len(data)):
            # turnaround_time = completion_time - arrival_time
            turnaround_time = data[i][5] - data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            data[i].append(turnaround_time)
        # average_turnaround_time = total_turnaround_time / no_of_processes    
        average_turnaround_time = total_turnaround_time / len(data)
        return average_turnaround_time

    def calculateWaitingTime(self, data):
        """
        calculate each process waiting time and append it at the end of process data list
        return average waiting time
        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        total_waiting_time = 0
        for i in range(len(data)):
            # waiting_time = turnaround_time - burst_time
            waiting_time = data[i][6] - data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            data[i].append(waiting_time)
        # average_waiting_time = total_waiting_time / no_of_processes    
        average_waiting_time = total_waiting_time / len(data)
        return average_waiting_time

    def calculateResponseTime(self, data):
        """
        calculate each process response and append it at the end of process data list
        return average response time
        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        total_response_time = 0
        for i in range(len(data)):
            response_time = self.first_time[i] - data[i][1]
            total_response_time = total_response_time + response_time
            data[i].append(response_time)
        average_response_time = total_response_time / len(data)
        return average_response_time

    def printData(self, data, average_turnaround_time, average_waiting_time, average_response_time, executed_process):
        """_summary_
        printing data

        Args:
            data (_type_): _description_
            average_turnaround_time (_type_): _description_
            average_waiting_time (_type_): _description_
            average_response_time (_type_): _description_
            executed_process (_type_): _description_
        """
        table = PrettyTable()
        # Sort processes according to the Process ID
        data.sort(key=lambda x: x[0])
        # add fields name to pretty table
        table.field_names = ['ID', 'Arrival', 'Remaining', 'isCompleted', 'BurstTime', 'FinishTime', 'Turnaround', 'Waiting', 'Response']
        # add data to pretty table
        for i in range(len(data)):
            table.add_row(data[i])
        # print pretty table    
        print(table)
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Average Response Time: {average_response_time}')
        print(f'Sequence of Processes: {executed_process}')

    def run(self):
        processes = int(input("Enter number of processes: "))
        self.inputProcessData(processes)