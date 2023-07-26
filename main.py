import datetime
import application.db.people as people
from application.salary import calculate_salary
from dirty_main import *

if __name__ == '__main__':
    print(people.get_employees())
    print(calculate_salary())
    print(func1())
    print(datetime.datetime.now())