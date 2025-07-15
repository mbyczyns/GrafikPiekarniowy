import calendar
from datetime import datetime as dt

class worker:
    def __init__(self, name, availability):
        self.name=name
        self.availability = availability
        self.working_days = 0

class day:
    def __init__(self,name, number):
        self.name=name
        self.number = number

class shift:
    def __init__(self, day, time_of_day):
        self.day = day
        self.time_of_day = time_of_day
        self.assigned_worker = None

    def assign_worker(self, worker):
        self.assigned_worker=worker


def get_next_month():

    year = dt.today().year
    month_nr = dt.today().month

    if month_nr==12:
        month_nr=0
        year+=1
    else: month_nr+=1

    cal_month = calendar.monthcalendar(year,month_nr)

    month = []
    for idx, week in enumerate(cal_month):
        for d in range (len(week)):
            if (week[d]!=0 ):
                match d:
                    case 0:
                        month.append(day(name='monday',number=week[d]))
                    case 1:
                        month.append(day(name='tuesday',number=week[d]))
                    case 2:
                        month.append(day(name='wednesday',number=week[d]))
                    case 3:
                        month.append(day(name='thursday',number=week[d]))
                    case 4:
                        month.append(day(name='friday',number=week[d]))
                    case 5:
                        month.append(day(name='saturday',number=week[d]))
                    case 6:
                        month.append(day(name='sunday',number=week[d]))
    return month



def get_workers_data(workers_info):
    workers = []
    for person in workers_info['pracownicy']:
        workers.append(worker(name=person['imie'], availability=person['dyspozycyjnosc']))
    return workers

