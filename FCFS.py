from process import Process
from output import Output
from tools import *
from print_process import print_process


def get_arrival(obj):
    return obj.arrival_time, obj.process_id


p1 = Process(1, 0, 24)
p2 = Process(2, 0, 3)
p3 = Process(3, 0, 3)
p4 = Process(4, 12, 1)
p5 = Process(5, 12, 4)
p6 = Process(6, 12, 6)

listP = [p3, p1, p2]


def fcfs(x):
    x.sort(key=get_arrival)
    count_done = 0
    count_processes = len(x)
    cpu_time = 0
    index = 0
    end_time = -1
    while count_done != count_processes:
        process = x[index]
        if (cpu_time < process.arrival_time):
            cpu_time = process.arrival_time
        process.start_time = cpu_time
        cpu_time = cpu_time + process.remain_time
        process.remain_time = 0
        index = index + 1
        count_done = count_done + 1
        if process.remain_time == 0:
            process.end_time = cpu_time
        if end_time < process.end_time:
            end_time = process.end_time
    print_process(x)
    output = Output(cal_awt(x), cal_art(x), cal_att(x), cal_utilization(x, end_time), cal_through_put(x, end_time))
    output.print()

    return output


fcfs(listP)
