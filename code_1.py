import json

tasks = []


def load_file():
    """Загружает список задач из файла."""
    try:
        with open("taski.json", 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_file():
    """Сохраняет список задач в файл."""
    with open('taski.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(task):
    """Добавляет задачу в список и сохраняет в файл."""
    if task.strip():  # Проверяем, что строка не пустая
        tasks.append({'task': task.strip()})
        save_file()


def show_tasks():
    """Отображает список задач."""
    if not tasks:
        print("Список задач пуст.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']}")


def delete_task(task_num):
    """Удаляет задачу по номеру из списка."""
    try:
        del tasks[task_num - 1]
        save_file()
    except IndexError:
        print("Неверный номер задачи.")


def main_code():
    """Главная функция для работы в терминале."""
    global tasks
    tasks = load_file()
    while True:
        action = input("Выберите действие: добавить, показать, удалить, выйти: ").strip().lower()
        if action == 'добавить':
            task = input('Введите задачу: ')
            add_task(task)
        elif action == 'показать':
            show_tasks()
        elif action == 'удалить':
            show_tasks()
            if tasks:  # Убедимся, что список не пуст
                try:
                    task_num = int(input('Введите номер задачи для удаления: '))
                    delete_task(task_num)
                except ValueError:
                    print('Введите корректный номер задачи.')
        elif action == 'выйти':
            print('До скорых встреч!')
            break
        else:
            print("Неизвестное действие. Попробуйте снова.")


if __name__ == '__main__':
    main_code()