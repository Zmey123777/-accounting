import pandas as pd
from datetime import date
from application.people import get_employees, set_employee
from application.salary import calculate_salary, set_salary


def do_something_with_pd():
    json = [{'id': 2, 'name': 'Непуш', 'surename': 'Напродов'}]
    df = pd.DataFrame(json, index=[0])
    # делаем какие то расчеты, или что-то еще например:
    df = df.rename(columns={'surename':'фамилия'})
    return df.to_dict(orient='records')
    

if __name__ == '__main__':
    print(f"Дата сегодня: {date.today()}")
    print(f"Получаем работника: {get_employees(1)}")
    print(f"Получаем всех работников: {get_employees()}")
    print(f"Загружаем работника: {set_employee(2, 'Леонид Якубович')}")
    print(f"Получаем расчет по зп: {calculate_salary(4)}")
    print(f"Устанавливаем зп: {set_salary(5)}")
    print(f"Получаем измененный датафрейм: {do_something_with_pd()}")
    
