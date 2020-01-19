from Process import Process


class SRT(object):
    @staticmethod
    def _sortByArrivalTime(value):
        return value.arrival_time

    @staticmethod
    def _sortByBurstTime(value):
        return value.cpu_burst

    def __init__(self, processLst):
        self.processLst = processLst

    def start(self):
        processByArrival = self.processLst.copy()
        processByArrival.sort(key=SRT._sortByArrivalTime)
        processByCpuBurst = self.processLst.copy()
        processByCpuBurst.sort(key=SRT._sortByBurstTime)

        nominates = []
        for process in processByArrival:
            pass
