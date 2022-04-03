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
    """
    Returns a pandas.core.frame.DataFrame object from a csv file
    """
    return pandas.read_csv("cs340_hw01_salesData01.csv")


def printByProduct(data):
    """
    Prints the data returned from the csv file sorted by 'Product'
    """
    rsltData = data.sort_values(by="Product")
    print(rsltData)


def createHeaderRows(file):
    """
    Reads a csv file and returns the header and the rows of the csv file
    """
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []

    for row in csvreader:
        rows.append(row)

    file.close()

    return header, rows


def findName(rows, name):
    """
    Searches over rows for a search over the csv file for a particular name
    """
    name = name.lower()
    num = 0
    for row in rows:
        names = row[7].split()
        for n in names:
            if n.lower() == name:
                num += 1

    print("Number of " + name + 's:' + str(num))
    # print(num)


def getAverage(rows):
    """
    Returns the average of the rows. The else statement could be removed if
    the empty values were wanted to be handled differently
    """
    tot = 0
    ind = 0

    for row in rows:
        if len(row[2]) > 0:
            tot += int(row[2])
            ind += 1

        else:
            ind += 1

    print("Average Transaction Total: " + str(round(tot/ind, 2)))


def changeUSA(rows):
    """
    Changes the name of the country from all variations of united states to USA
    """
    for row in rows:
        if row[6].lower() == "united states":
            row[6] = "USA"

    return rows


def createNewFile(fileName, header, rows):
    """
    Creates a new file given a file name, the header, and the rows of the csv file
    """
    with open(fileName, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)


data = createData(file)
printByProduct(data)
header, rows = createHeaderRows(file)
findName(rows, "amanda")
getAverage(rows)
createNewFile("new_csv.csv", header, changeUSA(rows))
