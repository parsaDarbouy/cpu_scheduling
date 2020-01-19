from process import Process
from output import Output


def get_arrival(obj):
    return obj.arrival_time, obj.process_id


p1 = Process(1, 0, 24)
p2 = Process(2, 0, 3)
p3 = Process(3, 0, 3)
p4 = Process(4, 12, 1)
p5 = Process(5, 12, 4)
p6 = Process(6, 12, 6)

listP = [p3, p1, p2]


def print_process(list_processes):
    print("process_id :" + '\t', end=" ")
    for i in list_processes:
        print(str(i.process_id) + '\t', end=" ")
    print()
    print("arrival_time :" + '\t', end=" ")
    for i in list_processes:
        print(str(i.arrival_time) + '\t', end=" ")
    print()
    print("start_time :" + '\t', end=" ")
    for i in list_processes:
        print(str(i.start_time) + '\t', end=" ")
    print()
    print("remain_time :" + '\t', end=" ")
    for i in list_processes:
        print(str(i.remain_time) + '\t', end=" ")
    print()
    print("end_time :" + '\t\t', end=" ")
    for i in list_processes:
        print(str(i.end_time) + '\t', end=" ")
    print()
    print("cpu_burst :" + '\t\t', end=" ")
    for i in list_processes:
        print(str(i.cpu_burst) + '\t', end=" ")
    print()
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
    return len(list_p) / end_time


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


def r_r(x):
    x.sort(key=get_arrival)
    count_done = 0
    count_processes = len(x)
    cpu_time = x[0].arrival_time
    index = 0
    end_time = -1
    queue = []
    is_in_cpu = []
    q = 5
    for i in x:
        is_in_cpu.append(0)

    while (count_done != count_processes):

        for i in range(len(x)):
            if (x[i].arrival_time <= cpu_time and is_in_cpu[i] == 0):
                queue.append(x[i])
                is_in_cpu[i] = 1
        process = queue[0]
        if (process.remain_time > q):
            if (process.start_time == -1):
                process.start_time = cpu_time
            process.remain_time = process.remain_time - q
            cpu_time = cpu_time + q
            queue.remove(process)
            queue.append(process)
        else:
            if (process.start_time == -1):
                process.start_time = cpu_time
            cpu_time = cpu_time + process.remain_time
            process.remain_time = 0
            process.end_time = cpu_time
            queue.remove(process)
            count_done = count_done + 1
        if (not len(queue)):
            if (count_done == count_processes):
                break
            else:
                for i in range(len(is_in_cpu)):
                    if (is_in_cpu == 0):
                        cpu_time = x[i].arrival_time
                        queue.append(x[i])
                        is_in_cpu[i] = 1

    print_process(x)
    output = Output(cal_awt(x), cal_art(x), cal_att(x), cal_utilization(x, cpu_time), cal_through_put(x, cpu_time))
    output.print

    return output


r_r(listP)
# fcfs(listP)
