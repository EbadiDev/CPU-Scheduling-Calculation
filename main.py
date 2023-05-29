import RoundRobin
import ShortestJobFirst

import os

def clear_terminal():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux and macOS
        _ = os.system('clear')

def main(processes,arrivalTime):
    print_info = """
         █████╗ ██████╗  ██████╗██╗  ██╗ ███╗   ██╗███████╗████████╗
        ██╔══██╗██╔══██╗██╔════╝██║  ██║ ████╗  ██║██╔════╝╚══██╔══╝
        ███████║██████╔╝██║     ███████║ ██╔██╗ ██║█████╗     ██║   
        ██╔══██║██╔══██╗██║     ██╔══██║ ██║╚██╗██║██╔══╝     ██║   
        ██║  ██║██║  ██║╚██████╗██║  ██║ ██║ ╚████║███████╗   ██║   
        ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   
             sign up now for cheap vpn at hub.archnet.online   
             
                                                     
                                                                            
            Select Type of CPU Scheduling Calculation: 
            ────────────────────────────────────────
            
            1. Round Robin (RR)
            2. Shortest Job First (SJF)
    """
    print(print_info)
    try:
        select = int(input())
    except ValueError:
        print("Exting")
    
    try:
        if select == 1:
            clear_terminal()
            print("Round Robin (RR)")
            RoundRobin.RoundRobinScheduler().run()
        elif select == 2:
            print("Shortest Job First (SJF)")
            sjf = ShortestJobFirst.ProcessScheduler(processes, arrivalTime)
            sjf.schedule_processes()
            sjf.print_results()
        else:
            raise ValueError("Select 1 or 2")
    except ValueError:
        print("Select 1 or 2")
        
        
if __name__ == "__main__":
    # For SJF we most initial variables 
    # processes = {"P1": [0, 4],
    #                  "P2": [2, 1],
    #                  "P3": [0, 2],
    #                  "P4": [4, 6]}
    # arrival_times = {"P1": 0, "P2": 2, "P3": 0, "P4": 4}
    process = {"P1":[2,2],
           "P2":[7,1],
           "P3":[5,1]}

    arrival_times = {"P1":2,
                    "P2":7,
                    "P3":5}
    # Run 
    main(process,arrival_times)   