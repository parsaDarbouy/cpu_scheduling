from process import Process
from output import Output


def get_arrival(obj):
    return obj.arrival_time, obj.process_id


p1 = Process(1, 2, 3)
p2 = Process(2, 5, 5)
p3 = Process(3, 8, 8)
p4 = Process(4, 12, 1)
p5 = Process(5, 12, 4)
p6 = Process(6, 12, 6)

listP = [p5, p2, p1, p4, p6, p3]


def print_process(list_processes):
    for i in list_processes:
        print(str(i.process_id) + '\t', end=" ")
    print()
    for i in list_processes:
        print(str(i.arrival_time) + '\t', end=" ")
    print()
    for i in list_processes:
        print(str(i.start_time) + '\t', end=" ")
    print()
    for i in list_processes:
        print(str(i.remain_time) + '\t', end=" ")
    print()
    for i in list_processes:
        print(str(i.end_time) + '\t', end=" ")
    print()
    for i in list_processes:
        print(str(i.cpu_burst) + '\t', end=" ")
    print()


def cal_awt(list_p):
    total_waiting = 0
    for i in list_p:
        total_waiting = total_waiting + (i.start_time - i.arrival_time)
    return total_waiting / len(list_p)


def cal_art(list_p):
    total_response = 0
    for i in list_p:
        total_response = total_response + i.end_time
    return total_response / len(list_p)


def cal_att(list_p):
    total_turnaround = 0
    for i in list_p:
        total_turnaround = total_turnaround + (i.end_time - i.arrival_time)
    return total_turnaround / len(list_p)


def cal_through_put(list_p, end_time):
    return end_time / len(list_p)


def cal_utilization(list_p, end_time):
    total_burst = 0
    for i in list_p:
        total_burst = total_burst + i.cpu_burst
    return total_burst / end_time


def fcfs(x):
    x.sort(key=get_arrival)
    count_done = 0
    count_processes = len(x)
    cpu_time = 0
    index = 0
    end_time = -1
    while count_done != count_processes:
        process = x[index]
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
