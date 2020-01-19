from process import Process
import time


class SPN(object):
    def __init__(self, processLst):
        self.processLst = processLst
        self.currentTime = 0
        self.processExecQueue = []

    @staticmethod
    def _sortByBurstTime(value):
        return value.cpu_burst

    def _chooseProcess(self):
        for process in self.processLst:
            if process.arrival_time <= self.currentTime and not process.isTerminated:
                return process

    def start(self):
        self.processLst.sort(key=SPN._sortByBurstTime)
        processFinishedCount = 0
        while processFinishedCount != len(self.processLst):
            currentProcess = self._chooseProcess()
            self.processExecQueue.append(currentProcess.process_id)
            currentProcess.start_time = self.currentTime
            time.sleep(currentProcess.cpu_burst * 0.001)
            self.currentTime += currentProcess.cpu_burst
            currentProcess.end_time = self.currentTime
            processFinishedCount += 1


# lst = [Process(1, 0, 4000), Process(2, 0, 5000), Process(3, 1, 2000)]
#
# spn = SPN(lst)
#
# spn.start()
