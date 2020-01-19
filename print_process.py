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
