import csv

with open("start_times.csv") as f:
    startTimes = csv.reader(f, delimiter=';')

    with open("submissions.csv") as f:
        submissions = csv.reader(f , delimiter=';')

        for line in  startTimes:
            name = line[0]


        for line in  submissions:
            print(line)