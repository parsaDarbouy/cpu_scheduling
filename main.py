from process import Process
from shortest_process_next import SPN
from shortest_remaining_time import SRT
import pandas as pd


def main():
    # filename = input("please enter the filename containing the process data:")
    df = pd.read_excel("../sep.xlsx")
    print(df.values)


if __name__ == "__main__":
    main()
