import calendar
from datetime import datetime as dt

class worker:
    def __init__(self, name, availability):
        self.name=name
        self.availability = availability
        self.working_days = 0
    
    def is_available_for(self, shift):
        for s in self.availability:
            if s.day.number == shift.day.number and s.time_of_day == shift.time_of_day:
                return True
        return False

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
        worker.working_days+=1

    def is_assigned(self):
        if self.assigned_worker==None: return 0
        else: return 1


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


def get_shifts(month):
    shifts = []
    for d in month:
        if d.name != 'sunday':
            sh = shift(d, 'morning')
            sh2 = shift(d, 'afternoon')
            shifts.append(sh)
            shifts.append(sh2)
    return shifts


def parse_workers_data(workers_info, month):
    workers = []
    for person in workers_info['pracownicy']:
        workername = person['imie']
        worker_availability=[]
        for idx, availability_day in enumerate(person['dyspozycyjnosc']):
            day_nr = next(filter(lambda d: d.number == idx+1, month), None)
            if availability_day['rano']==1: 
                sh1 = shift(day=day_nr,time_of_day='morning')
                worker_availability.append(sh1)
            if availability_day['popo']==1:
                sh1 = shift(day=day_nr,time_of_day='afternoon')
                worker_availability.append(sh1)
        workers.append(worker(name=workername,availability=worker_availability))
    return workers


def sort_workers_by_working_days(workers_info):
    return sorted(workers_info, key=lambda w: w.working_days)


def assign_shifts(workers_data, shifts):
    it_shifts = iter(shifts)
    shift_pairs = list(zip(it_shifts, it_shifts)) 

    for sh_morning, sh_afternoon in shift_pairs:
        workers_data = sort_workers_by_working_days(workers_data)
        for wrk in workers_data:
            if wrk.is_available_for(sh_morning):
                sh_morning.assign_worker(wrk)
                morning_worker = wrk
                break

        workers_data = sort_workers_by_working_days(workers_data)

        for wrk in workers_data:
            if (wrk.is_available_for(sh_afternoon) and wrk != morning_worker) or wrk.name=='Mr. Nobody':
                sh_afternoon.assign_worker(wrk)
                break

    all_shifts = [sh for pair in shift_pairs for sh in pair]
    return all_shifts


    

