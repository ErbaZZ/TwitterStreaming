import re
import json

readfile = 'btc_log_raw.txt'
writefile = 'btc_log_clean.txt'

with open(readfile) as f:
    line = f.readline()

    with open(writefile,'w') as wf:
        while line:
            tweet = json.loads(line)
            outstr = ""
            time = tweet["created_at"]
            locstr = tweet["user"]["location"]
            tzstr = tweet["user"]["time_zone"]
            if locstr:
                outstr += locstr + '*'
            else:
                outstr += 'null*'
            if tzstr:
                outstr += tzstr
            else:
                outstr += 'null'
            outstr += '\n'
            if outstr != 'null*null\n':
                wf.write(time.encode('utf8') + '*' + outstr.encode('utf8'))
            line = f.readline()
            line = f.readline()
        wf.close()
    f.close()
'''     
        while line:
            locstr = re.search('"location":"([a-zA-Z0-9,]+)"', line)
            tzstr = re.search('"time_zone":"([a-zA-Z0-9,]+)"',line)
            outstr = ""
            if locstr:
                outstr += locstr.group(0)[11:] + '*'
            if tzstr:
                outstr += tzstr.group(0)[12:]
            if outstr:
                outstr += '\n'
'''
