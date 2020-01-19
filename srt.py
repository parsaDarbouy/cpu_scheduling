from Process import Process
import time


class SRT(object):
    @staticmethod
    def _sortByRemainTime(value):
        return value.remain_time

    def __init__(self, processLst):
        self.processLst = processLst
        self.currentTime = 0
        self.processExecQueue = []

    def _chooseProcess(self):
        for process in self.processLst:
            if not process.isTerminated and process.arrival_time <= self.currentTime:
                return process

    def start(self):
        self.processLst.sort(key=SRT._sortByRemainTime)
        processFinishedCount = 0
        print(time.time())
        while processFinishedCount != len(self.processLst):
            currentProcess = self._chooseProcess()
            self.processExecQueue.append(currentProcess.process_id)
            currentProcess.start_time = self.currentTime
            time.sleep(0.001)
            self.currentTime += 1
            currentProcess.remain_time -= 1
            if currentProcess.isFinished:
                currentProcess.end_time = self.currentTime
                processFinishedCount += 1
        print(time.time())


lst = [Process(1, 0, 3), Process(2, 0, 4), Process(3, 1, 1), Process(4, 1, 2)]

srt = SRT(lst)

srt.start()
