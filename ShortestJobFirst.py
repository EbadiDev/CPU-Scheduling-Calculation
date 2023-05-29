# import matplotlib.pyplot as plt

class ProcessScheduler:    
    def __init__(self, processes, arrival_times):
        self.processes = processes
        self.arrival_times = arrival_times
        self.turn_around_times = []
        self.response_times = []
        self.p = []
        self.time = 0        
                
    def schedule_processes(self):
        while len(self.processes) > 0:
            # select process based on lowest arrival time and burstime
            lowest_key = min(self.processes, key=lambda k: (self.processes[k][0], self.processes[k][1]))
            # check if 
            if self.time < self.arrival_times[lowest_key]:
                self.time = self.arrival_times[lowest_key] 
                
            self.p.append(lowest_key)
            
            for key in self.processes:
                if key != lowest_key:
                    self.processes[key] = [max(self.processes[key][0] - self.processes[lowest_key][1], 0), self.processes[key][1]]
                else:
                    self.response_times.append(self.time - self.arrival_times[key])
                    self.time += self.processes[key][1]
                    self.turn_around_times.append(self.time - self.arrival_times[key])
            
            del self.processes[lowest_key]
    
    def get_avg_turn_around_time(self):
        return sum(self.turn_around_times) / len(self.turn_around_times)
    
    def get_avg_response_time(self):
        return sum(self.response_times) / len(self.response_times)
    
    def print_results(self):
        print(f"Average Turnaround Time: {self.get_avg_turn_around_time()}")
        print(f"Average Response Time: {self.get_avg_response_time()}")
        print(f"Scheduling Order: {self.p}")
      
