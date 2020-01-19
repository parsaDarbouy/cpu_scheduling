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