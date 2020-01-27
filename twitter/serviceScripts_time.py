from datetime import datetime

def daysInMonth2020(month):
    return{
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }[month]

def calculateTime(time):
    day = int(time.split('T')[0].split('-')[2])
    month = int(time.split('T')[0].split('-')[1])
    year = int(time.split('T')[0].split('-')[0])
    hour = int(time.split('T')[1].split(':')[0])
    if hour < 5:
        if day > 1:
            day = day - 1
        else:
            if month > 1:
                month = month - 1 
                day = daysInMonth2020(day)
            else:
                year = year - 1
                month = 12
                day = daysInMonth2020(day)
    
    timeNowMonth = int(str(datetime.now()).split()[0].split('-')[1])
    timeNowDay = int(str(datetime.now()).split()[0].split('-')[2])

    if timeNowMonth - month == 1:
        timeNowDay = timeNowDay + daysInMonth2020(timeNowMonth - 1)  
        return timeNowDay - day <= 7
    elif timeNowMonth == month:
        return timeNowDay - day <= 7
    else:
        return False

def dateParser(date, time):
    dateComponents = date.split()
    if "PM" or "AM" in dateComponents:
        dateHour  = int(dateComponents[0].split(":")[0])
        if "PM" in dateComponents:
            dateHour = dateHour + 12
    timeHour = int(time.split('T')[1].split(':')[0]) - 5
    return timeHour == dateHour
    
