from typing import Optional


def get_employees(id: Optional[int] = None) -> str:
    if id is None:
        return f"Выбраны все сотрудники"
    return f"Сотрудник с id: {id} выбран из БД"


def set_employee(id: int, name: str) -> str:
    return f"Сотрудник {name} загружен в БД"
