Make a program that simulate SJF ( Shortest Job First ) CPU scheduling algorithm

how it's works?


| Process name | Arrive time | Burst time |
| -- | -- | -- |
|P1| 0 | 4 |
|P2| 2 | 1 |
|P3| 0 | 2 |
|P4| 4 | 6 |



```html
       P3          P2         P1         P4
|0----####---2----####---3---####---7---####---13-|
```

Return time (Turnaround time) formula:
```
Turnaround Time = Completion Time - Arrival Time

Where,
Completion Time: The time when a process completes its execution
Arrival Time: The time when a process arrives in the ready queue

Average Turnaround Time = (Sum of Turnaround Times for all processes) / (Number of processes)

```