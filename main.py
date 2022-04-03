import csv
import pandas

'''
0 = Transaction_date
1 = Product
2 = Price
3 = Payment_Type
4 = City
5 = State
6 = Country
7 = Name
8 = Account_Created
9 = Last_Login
10 = Latitude
11 = Longitude
'''

file = open("cs340_hw01_salesData01.csv")
data = pandas.read_csv("cs340_hw01_salesData01.csv")

print(data)

csvreader = csv.reader(file)

header = next(csvreader)

print(header)

rows = []

for row in csvreader:
  rows.append(row)

file.close()


rows.sort(key=lambda rows: rows[1])

for row in rows:
  print()
  print("New Transaction")

  for i in row:
    print(i)

num = 0
for row in rows:
  names = row[7].split()
  for name in names:
    if name.lower() == "amanda":
      num += 1

print("NUMBER OF AMANDAS!")
print(num)

