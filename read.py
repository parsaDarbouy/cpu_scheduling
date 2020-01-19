import csv
from process import Process
from print_process import print_process
from output import Output


class Read(object):
    def __init__(self, path):
        self.path = path
        self.list_p = []

    def make_list_of_processes(self):
        with open(self.path) as file:
            readCSV = csv.reader(file, delimiter=',')
            flag = 0
            for row in readCSV:
                if flag == 0:
                    flag = 1
                else:
                    self.list_p.append(Process(int(row[0]), int(row[1]), int(row[2])))

        return self.list_p


# ob = Read("excel.csv")
# ob.make_list_of_processes()
