from process import Process
from spn import SPN
from srt import SRT
import pandas as pd


def main():
    # filename = input("please enter the filename containing the process data:")
    df = pd.read_excel("../sep.xlsx")
    print(df.values)


if __name__ == "__main__":
    main()
