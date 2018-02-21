import re
import json
import csv
import pandas
from time import sleep

readfile = 'diabetes.txt'
writefile = 'diabetes_csv.csv'
coorfile = 'coor.csv'

coor = pandas.read_csv(coorfile)
pos = 0

while True:
    print('Pos = ' + str(pos))
    with open(readfile) as f:
        f.seek(pos)
        line = f.readline()
        with open(writefile,'ab') as wf:

            writer = csv.writer(wf)
            if pos == 0:
                writer.writerow(["created_at", "timezone", "latitude", "longitude", "weight", "radius"])
            while line:
                tweet = json.loads(line)
                outstr = ""
                time = tweet["created_at"]
                locstr = tweet["user"]["location"]
                tzstr = tweet["user"]["time_zone"]
                text = tweet["text"]
                row = coor.loc[coor['location'] == tzstr]
                if row.size != 0 and tzstr:
                    writer.writerow([time.encode('utf8'), tzstr.encode('utf8'), row.values[0][0], row.values[0][1], row.values[0][3], row.values[0][4]])
    #            write(time.encode('utf8') + '::' + text.encode('utf8')+ '::' + outstr.encode('utf8'))
                line = f.readline()
                while '"limit"' in line:
                    line = f.readline()
            pos = f.tell()
            wf.close()
            print 'No more line! Sleeping for 10 seconds'
            sleep(10)
        f.close()