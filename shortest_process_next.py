from output import Output
from print_process import print_process
from process import Process
from tools import *
import time


class SPN(object):
    def __init__(self, processLst):
        self.processLst = processLst
        self.currentTime = 0
        self.processExecQueue = []

    @staticmethod
    def _sortByBurstTime(value):
        return value.cpu_burst

    @staticmethod
    def _sortByArrivalTime(value):
        return value.arrival_time

    def _chooseProcess(self):
        for process in self.processLst:
            if process.arrival_time <= self.currentTime and not process.isTerminated:
                return process

    def _getNextClosestTime(self):
        lst = sorted(self.processLst, key=SPN._sortByArrivalTime)
        for i in range(len(lst)):
            if lst[i].end_time == self.currentTime:
                return lst[i + 1].arrival_time

    def start(self):
        self.processLst.sort(key=SPN._sortByBurstTime)
        processFinishedCount = 0
        while processFinishedCount != len(self.processLst):
            currentProcess = self._chooseProcess()
            if currentProcess is None:
                nextTime = self._getNextClosestTime()
                time.sleep((nextTime - self.currentTime) * 0.001)
                self.currentTime = nextTime
                continue
            self.processExecQueue.append(currentProcess.process_id)
            currentProcess.start_time = self.currentTime
            time.sleep(currentProcess.cpu_burst * 0.001)
            self.currentTime += currentProcess.cpu_burst
            currentProcess.end_time = self.currentTime
            processFinishedCount += 1

        print_process(self.processLst)
        output = Output(cal_awt(self.processLst), cal_art(self.processLst), cal_att(self.processLst),
                        cal_utilization(self.processLst, self.currentTime),
                        cal_through_put(self.processLst, self.currentTime))
        output.print()


lst = [Process(1, 0, 1), Process(2, 3, 5), Process(3, 3, 4)]
#
spn = SPN(lst)
#
spn.start()
