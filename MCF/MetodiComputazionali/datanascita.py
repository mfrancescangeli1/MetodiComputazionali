from datetime import datetime, timedelta
data=input("data di nascita ")
mydate=datetime.strptime(data,"%d-%m-%Y")
print(mydate)
now=datetime.now()
timediff=now-mydate
print(timediff)
annis=timediff.total_seconds()
print(annis)
anniy=now.year-mydate.year
print(anniy)
