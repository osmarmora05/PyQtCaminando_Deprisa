from datetime import datetime, date

def getDate():
    today = date.today()
    return (today.strftime("%d/%m/%Y"))

def getTime():
    now = datetime.now()
    return(now.strftime("%H:%M"))