from Process import Process
import time


class SRT(object):
    @staticmethod
    def _sortByArrivalTime(value):
        return value.arrival_time

    @staticmethod
    def _sortByBurstTime(value):
        return value.cpu_burst

    def __init__(self, processLst):
        self.processLst = processLst
        self.currentTime = 0
        self.processExecQueue = []

    def _chooseProcess(self):
        nominates = []
        for process in self.processLst:
            if not process.isTerminated and process.arrival_time <= self.currentTime:
                nominates.append(process)

        nominates.sort(key=SRT._sortByBurstTime)

        return nominates[0]

    def _areAllTerminated(self):
        for process in self.processLst:
            if not process.isTerminated:
                return False
        return True

    def start(self):
        currentProcess = self._chooseProcess()

        while not self._areAllTerminated():
            time.sleep(0.001)
            self.currentTime += 1
            currentProcess.

