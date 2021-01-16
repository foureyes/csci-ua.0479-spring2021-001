import csv
with open('/tmp/movies.csv') as csvfile:
    # gives back an ordered dictionary

    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
