from Process import Process


def get_arrival(obj):
    return (obj.arrival_time, obj.process_id)


p1 = Process(1, 2, 3)
p2 = Process(2, 5, 5)
p3 = Process(3, 8, 5)
p4 = Process(4, 12, 5)
p5 = Process(5, 12, 5)
p6 = Process(6, 12, 5)

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


def fcfs(x):
    x.sort(key=get_arrival)
    count_done = 0
    count_processes = len(x)
    cpu_time = 0
    index = 0
    while (count_done != count_processes):
        process = x[index]
        process.startTime = cpu_time
        cpu_time = + process.remain_time
        process.remain_time = 0
        index = index + 1
        count_done = count_done + 1
        if (process.remain_time == 0):
            process.endTime = cpu_time
    print_process(x)

    return

fcfs(listP)
