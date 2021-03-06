import csv


class Output:
    def __init__(self, A_W_T, A_R_T, A_T_T, cpu_utilization, through_put):
        self.A_W_T = A_W_T
        self.A_R_T = A_R_T
        self.A_T_T = A_T_T
        self.cpu_utilization = cpu_utilization
        self.through_put = through_put

    def print(self):
        print("A.W.T : " + str(self.A_W_T) + '\t', end=" ")
        print("A.R.T : " + str(self.A_R_T) + '\t', end=" ")
        print("A.T.T : " + str(self.A_T_T) + '\t', end=" ")
        print("cpu utilization : " + str(self.cpu_utilization) + '\t', end=" ")
        print("throughput : " + str(self.through_put) + '\t', end=" ")

    def write(self, path):
        with open(path, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['A.W.T'] + ['A.R.T'] + ['A.T.T'] + ['cpu_utilization'] + ['throughput'])
            spamwriter.writerow(
                ["{:.3f}".format(self.A_W_T), "{:.3f}".format(self.A_R_T), "{:.3f}".format(self.A_T_T),
                 "{:.3f}".format(self.cpu_utilization), "{:.3f}".format(self.through_put)])
