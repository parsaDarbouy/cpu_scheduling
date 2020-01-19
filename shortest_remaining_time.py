from output import Output
from print_process import print_process
from process import Process
import time

from tools import *


class SRT(object):
    @staticmethod
    def _sortByRemainTime(value):
        return value.remain_time

    @staticmethod
    def _sortByArrivalTime(value):
        return value.arrival_time

    def __init__(self, processLst):
        self.processLst = processLst
        self.currentTime = 0
        self.processExecQueue = []

    def _chooseProcess(self):
        readyQueue = []
        for process in self.processLst:
            if not process.isTerminated and process.arrival_time <= self.currentTime:
                readyQueue.append(process)

        readyQueue.sort(key=SRT._sortByRemainTime)
        if not readyQueue:
            return
        return readyQueue[0]

    def _getNextClosestTime(self):
        sortedProcess = sorted(self.processLst, key=SRT._sortByArrivalTime)
        for i in range(len(sortedProcess)):
            if sortedProcess[i].end_time == self.currentTime:
                return sortedProcess[i + 1].arrival_time

    def start(self):
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
            time.sleep(0.001)
            self.currentTime += 1
            currentProcess.remain_time -= 1
            if currentProcess.isFinished:
                currentProcess.end_time = self.currentTime
                processFinishedCount += 1

        print_process(self.processLst)
        output = Output(cal_awt(self.processLst), cal_art(self.processLst), cal_att(self.processLst),
                        cal_utilization(self.processLst, self.currentTime),
                        cal_through_put(self.processLst, self.currentTime))
        output.print()


# lst = [Process(1, 0, 2), Process(2, 2, 4), Process(3, 5, 1)]
# lst = [Process(1, 0, 5), Process(2, 3, 3)]

# srt = SRT(lst)

# srt.start()
