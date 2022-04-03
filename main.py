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

def createData(file):
  return pandas.read_csv("cs340_hw01_salesData01.csv")

def printByProduct(data):
  rsltData = data.sort_values(by = "Product")
  print(rsltData)


def createHeaderRows(file):
  csvreader = csv.reader(file)

  header = next(csvreader)
  


  rows = []

  for row in csvreader:
    rows.append(row)

  file.close()
  
  return header, rows

def findName(rows, name):
  name = name.lower()
  num = 0
  for row in rows:
    print(row[7])
    names = row[7].split()
    for n in names:
      if n.lower() == name:
        num += 1

  print("Number of NAMES")
  print(num)

'''
rows.sort(key=lambda rows: rows[1])

num = 0
for row in rows:
  names = row[7].split()
  for name in names:
    if name.lower() == "amanda":
      num += 1

print("NUMBER OF AMANDAS!")
print(num)
tot = 0 
ind = 0

for row in rows:
  if len(row[2]) > 0:
    tot += int(row[2])
    ind += 1
  else:
    ind += 1


print()
print("AVERAGE")
print(round(tot/ind, 2))
for row in rows:
  if row[6].lower() == "united states":
    row[6] = "USA"

fileName = "new_csv.csv"

with open(fileName, 'w', newline="") as file:
  csvwriter = csv.writer(file)
  csvwriter.writerow(header)
  csvwriter.writerows(rows)

for row in rows:
  print(row)
  print()
'''
data = createData(file)

printByProduct(data)
header, rows = createHeaderRows(file)
findName(rows, "amanda")

