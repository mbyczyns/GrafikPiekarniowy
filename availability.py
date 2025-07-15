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
workers = cf.get_workers_data(dyspo)

for day in month:
    print(day.name, day.number)
    print('-------')