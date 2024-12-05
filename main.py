from flask import Flask, render_template, request, redirect
import code_1

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def task_manager():
    tasks = code_1.load_file()

    if request.method == 'POST':
        # Добавление задачи
        task = request.form.get('task')  # Получаем значение из поля добавления задачи
        if task and task.strip():  # Проверяем, что задача не пустая
            code_1.add_task(task)

        # Удаление задачи
        task_to_delete = request.form.get('delete_task')  # Получаем значение из кнопки удаления
        if task_to_delete:
            try:
                task_num = int(task_to_delete)  # Преобразуем в число
                code_1.delete_task(task_num)  # Удаляем задачу по номеру
            except ValueError:
                pass  # Игнорируем некорректные значения

        return redirect('/')  # Перенаправляем на главную страницу

    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)