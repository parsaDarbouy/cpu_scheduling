class Process:

    def __init__(self, process_id, arrival_time, cpu_burst):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.cpu_burst = cpu_burst
        self.remain_time = cpu_burst

    startTime = -1
    endTime = -1
