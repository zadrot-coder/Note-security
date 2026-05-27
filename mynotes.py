import sqlite3
import time

class Notes:
    def __init__(self, category: str, content: str):
        self.category = category
        self.content = content


def init_db():
    conn = sqlite3.connect("my_notes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()


def local_viewing(category_name, content_text):
    new_card = Notes(category_name, content_text)
    
    conn = sqlite3.connect("my_notes.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (category, content) VALUES (?, ?)", 
        (new_card.category, new_card.content)
    )
    conn.commit()
    conn.close()
    
    return f"Успешно записано в {new_card.category}"


def interactive_menu():
    print("🌟 СИСТЕМА ЗАМЕТОК ЗАПУЩЕНА! 🌟")
    
    while True:
        x = input("\nВыберите действие:\n1.Заметка | 2.Долг | 3.День рождения | 4.Просмотреть... | 5.Выход\nВведите цифру: ")
        
        if x == '1':
            text = input("📝 Введите текст заметки: ")
            answer = local_viewing("note", text)
            print(f"✅ Результат: {answer}")
                    
        elif x == '2':
            text = input("📝 Кто и сколько вам должен?: ")
            answer = local_viewing("duty", text)
            print(f"✅ Результат: {answer}")
                    
        elif x == '3':
            text = input("📝 У кого когда день рождения?: ")
            answer = local_viewing("birthday", text)
            print(f"✅ Результат: {answer}")

        elif x == '4':
            r = input("Что вы хотите осмотреть? \n1.Заметки📝 | 2.Долги💲 | 3.Дни рождения🥳\nВведите цифру: ")
            
            if r == '1':
                chosen_category = 'note'
                print("Идет запуск заметок...") 
            elif r == '2':
                chosen_category = 'duty'
                print("Идет запуск долгов...") 
            elif r == '3':
                chosen_category = 'birthday'
                print("Идет запуск дней рождения...") 
            else:
                print("❌ Неверный выбор категории!")
                continue
                
            time.sleep(1)
            
            conn = sqlite3.connect("my_notes.db")
            cursor = conn.cursor()
            cursor.execute("SELECT content FROM notes WHERE category = ?", (chosen_category,))
            rows = cursor.fetchall()
            conn.close()
            
            my_notes = [row for row in rows]
            
            if r == '1':
                print(f"✅ Ваши заметки: {my_notes}") 
            elif r == '2':
                print(f"✅ Ваши долги: {my_notes}")
            elif r == '3':
                print(f"✅ Ваши дни рождения: {my_notes}")

        elif x == '5':
            print("Идет закрытие программы...🌐")
            time.sleep(1)
            print("Программа закрыта✅")
            break
            
        else:
            print("❌ Неверный ввод! Выберите цифру от 1 до 5.")


if __name__ == '__main__':
    init_db()
    interactive_menu()
