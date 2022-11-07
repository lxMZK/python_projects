import csv

with open('Assets.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    for host in csv_reader:
        print(host["IP Address"])
