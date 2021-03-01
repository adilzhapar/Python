import csv

with open('ex2.csv', mode='w') as employees:
    writer = csv.writer(employees, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Askar", "IT", "February"])
    writer.writerow(["Adil", "Product", "August"])
    writer.writerow(["Messi", "Football", "June"])
