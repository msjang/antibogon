import datetime

base = datetime.datetime.today()
days = [base - datetime.timedelta(days=x) for x in range(1, 365)]
days = [(x.year,x.month,x.day) for x in days]

fmt_dmp = "wget http://data1.labs.apnic.net/bgplog/%04d/%02d/%02d/%04d-%02d-%02d.dmp.gz;"
fmt_del = "wget http://ftp.apnic.net/stats/apnic/%04d/delegated-apnic-%04d%02d%02d.gz;"

for d in days:
    cmd = fmt_del % (d[0],d[0],d[1],d[2])
    print(cmd)

for d in days:
    cmd = fmt_dmp % (d[0],d[1],d[2],d[0],d[1],d[2])
    print(cmd)
