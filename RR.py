from process import Process
from output import Output
from cal import *
from Print_process import print_process


def get_arrival(obj):
    return obj.arrival_time, obj.process_id


p1 = Process(1, 0, 24)
p2 = Process(2, 0, 3)
p3 = Process(3, 0, 3)
p4 = Process(4, 12, 1)
p5 = Process(5, 12, 4)
p6 = Process(6, 12, 6)

listP = [p3, p1, p2]


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
    output.write("eggs.csv")

    return output


r_r(listP)
