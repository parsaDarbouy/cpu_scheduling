from Process import Process
import time


class SRT(object):
    @staticmethod
    def _sortByArrivalTime(value):
        return value.arrival_time

    @staticmethod
    def _sortByRemainTime(value):
        return value.remain_time

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

        return readyQueue[0]

    def start(self):
        processFinishedCount = 0
        # print(time.time())
        while processFinishedCount != len(self.processLst):
            currentProcess = self._chooseProcess()
            currentProcess.start_time = self.currentTime
            self.processExecQueue.append(currentProcess.process_id)
            # time.sleep(0.001)
            self.currentTime += 1
            currentProcess.remain_time -= 1
            if currentProcess.isFinished:
                currentProcess.end_time = self.currentTime
                processFinishedCount += 1
        # print(time.time())


lst = [Process(1, 0, 4000), Process(2, 0, 5000), Process(3, 1, 2000)]

srt = SRT(lst)

srt.start()
