class Process:

    def __init__(self, process_id, arrival_time, cpu_burst):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.cpu_burst = cpu_burst
        self.remain_time = cpu_burst
        self.start_time = -1
        self.end_time = -1

    @property
    def isTerminated(self):
        if self.end_time == -1:
            return False
        return True

    @property
    def isFinished(self):
        if self.remain_time == 0:
            return True
        return False

    def copy(self):
        return Process(self.process_id, self.arrival_time, self.cpu_burst)
