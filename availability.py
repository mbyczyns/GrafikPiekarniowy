import classes_functions as cf

dyspo = {
  "pracownicy": [
    {
      "imie": "Anna",
      "dyspozycyjnosc": [
        {"rano": 0, "popo": 1},
        {"rano": 0, "popo": 1},
        {"rano": 0, "popo": 1}
      ]
    },
    {
      "imie": "Tomek",
      "dyspozycyjnosc": [
        {"rano": 1, "popo": 1},
        {"rano": 0, "popo": 0},
        {"rano": 1, "popo": 0}
      ]
    },
    {
      "imie": "Wojtek",
      "dyspozycyjnosc": [
        {"rano": 1, "popo": 1},
        {"rano": 1, "popo": 1},
        {"rano": 1, "popo": 0}
      ]
    },
    {
      "imie": "Marta",
      "dyspozycyjnosc": [
        {"rano": 1, "popo": 1},
        {"rano": 1, "popo": 1},
        {"rano": 1, "popo": 0}
      ]
    }
  ]
}

month = cf.get_next_month() # getting data about month (days of week)

shifts = cf.get_shifts(month) # getting list of available shifts

workers_data = cf.parse_workers_data(workers_info=dyspo, month=month) # parsing workers availability to their classes

dummy_worker = cf.worker(name='Mr. Nobody', availability=shifts) # creating a dummy worker - he is assigned when there is nobody who can work 
dummy_worker.working_days=1000
workers_data.append(dummy_worker)

assigned_shifts = cf.assign_shifts(workers_data=workers_data, shifts=shifts) # creating the work schedule for the month
for as_sh in assigned_shifts:
    print(as_sh.day.name,as_sh.day.number, as_sh.time_of_day, ' - ', as_sh.assigned_worker.name)