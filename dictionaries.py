# Словарь с информацией о нескольких студентах
students = {
    "айдай": {
        "возраст": 21,
        "факультет": "Факультет информационных технологий"
    },
    "альбина": {
        "возраст": 22,
        "факультет": "Факультет биологии"
    },
    "алия": {
        "возраст": 23,
        "факультет": "Факультет экономики"
    }
}

# Выводим информацию о студенте Альбина
student = "альбина"
print(f"Возраст студента {student}: {students[student]['возраст']}")
print(f"Факультет студента {student}: {students[student]['факультет']}")