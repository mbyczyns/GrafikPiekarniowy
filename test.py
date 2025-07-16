import classes_functions as cf

anna = cf.worker(name='anna',  availability=[])
kamil = cf.worker(name='kamil', availability=[])
stefan = cf.worker(name='stefan',  availability=[])
anna.working_days=3
kamil.working_days=1
stefan.working_days=5

workers = [anna, kamil,stefan]

workers = cf.sort_workers_by_working_days(workers)

for wor in workers:
    print(wor.name, wor.working_days)