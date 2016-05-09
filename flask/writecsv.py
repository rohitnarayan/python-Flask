import csv


def writeThrough():
    with open('scores.txt','a') as scorefile:
        writeHandle = csv.writer(scorefile)
        writeHandle.writerow(['rahul',5,9])

    scorefile.close()


def readThrough():
    with open('scores.txt','r') as scorefile:
        readingHandle = csv.reader(scorefile)
        mylist=[]
        for row in readingHandle:
            if len(row) != 0:
                mylist = mylist + [row]
    scorefile.close()
    print mylist


if __name__ == '__main__':
    writeThrough()
    readThrough()

