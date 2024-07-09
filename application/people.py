
def get_worker(id: int) -> str:
    return f"Сотрудник с id: {id} выбран из БД"


def set_worker(id: int, name: str) -> str:
    return f"Сотрудник {name} загружен в БД"