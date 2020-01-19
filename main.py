from FCFS import fcfs
from read import Read
from round_robin import r_r
from shortest_process_next import SPN
from shortest_remaining_time import SRT


def main():
    filename = input("please enter the filename containing the process data:")
    readExcel = Read(filename)
    processLst = readExcel.make_list_of_processes()
    print("FCFS:")
    fcfs(processLst)
    print("Round Robin:")
    r_r(processLst)
    spn = SPN(processLst)
    srt = SRT(processLst)
    print("Shortest Process Next:")
    spn.start()
    print("Shortest Remaining Time:")
    srt.start()


if __name__ == "__main__":
    main()
