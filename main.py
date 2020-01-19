from FCFS import fcfs
from read import Read
from round_robin import r_r
from shortest_process_next import SPN
from shortest_remaining_time import SRT


def main():
    filename = input("please enter the filename containing the process data:")
    readExcel = Read(filename)
    processLst = readExcel.make_list_of_processes()
    print("\n\nFCFS:\n")
    fcfs([x.copy() for x in processLst])
    print("\n\nRound Robin:\n")
    r_r([x.copy() for x in processLst])
    spn = SPN([x.copy() for x in processLst])
    srt = SRT([x.copy() for x in processLst])
    print("\n\nShortest Process Next:\n")
    spn.start()
    print("\n\nShortest Remaining Time:\n")
    srt.start()


if __name__ == "__main__":
    main()
