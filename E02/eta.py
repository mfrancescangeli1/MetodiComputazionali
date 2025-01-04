from datetime import datetime, timedelta





def eta(date):
    now=datetime.now()
    timediff=now-date
    un=input("sciegliere unità di misura ")
    if un=="secondi":
        annis=timediff.total_seconds()
        print(annis)
    elif un=="anni":
        anniy=now.year-date.year
        print(anniy)
    elif un=="giorni":
        annid=timediff.days
        print(annid)
    else:
        print("sbagliato")
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
eta(mydate)
