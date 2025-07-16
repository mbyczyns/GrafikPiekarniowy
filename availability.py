import classes_functions as cf

dyspo = {
  "pracownicy": [
    {
      "imie": "Anna",
      "dyspozycyjnosc": [
        {"rano": 0, "popo": 1},
        {"rano": 1, "popo": 1},
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
    }
  ]
}

month = cf.get_next_month()

# for day in month:
#     print(day.name, day.number)
#     print('-------')



shifts = cf.get_shifts(month)
# for sh in shifts:
#     print(sh.day.name,sh.day.number, sh.time_of_day)

workers_data = cf.get_workers_data(workers_info=dyspo, month=month)

for worker in workers_data:
    print(worker.name)
    print(worker.working_days)
    for sh in worker.availability:
        print(sh.day.number, sh.day.name, sh.time_of_day)
    print('')