process = {"P1":[0,30],
           "P2":[0,20],
           "P3":[0,1]}

arrival_times = {"P1":0,
                 "P2":0,
                 "P3":0}

# returnTimes = {}
returnTimes = []
responeTimes = [] # when first cpu time
burstTime = 0
cpuFirst = 0
while len(process) > 0:
    
    print(process)
    lowest_key = min(process, key=lambda k: (process[k][0], process[k][1]))
    print("selected process:", lowest_key)
    
    numbers = []
    for key in process:
        if key != lowest_key:
            process[key] = [max(process[key][0] - process[lowest_key][1], 0), process[key][1]]
        else :
            # returnTimes.append(process[key][1])
            # returnTimes[process].append(burstTime)
            arrive = arrival_times[key]
            # yek marhale qabl az jam kardan burst time mishe shoro process ke vared shode
            whatIsHappeningHere2 = burstTime - arrive
            responeTimes.append(whatIsHappeningHere2) 

            burstTime += process[key][1]

            # arrive = process[lowest_key][0] # 

            print("Arrival time for", lowest_key, "is", arrive)
            whatIsHappeningHere = burstTime - arrive
            returnTimes.append(whatIsHappeningHere)

            
            
    print(f"{lowest_key} job has done and take {process[lowest_key][1]} CPU Time")
    del process[lowest_key]
    print("Updated process:", process)

avg_return_time = sum(returnTimes) / len(returnTimes)
print(f"Average Return Time: {avg_return_time}s", )

avg_response_time = sum(responeTimes) / len(responeTimes)
print(f"Average response Time: {avg_response_time}s")