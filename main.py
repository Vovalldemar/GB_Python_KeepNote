from manager import NoteManager

def print_menu():
    print("\n==== Меню ====")
    print("1. Создать заметку")
    print("2. Показать все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

def main():
    manager = NoteManager()
    
    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            manager.create_note(title, body)
            print("Заметка создана.")
        elif choice == "2":
            notes = manager.list_notes()
            if notes:
                for note in notes:
                    print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата: {note.timestamp}")
                    print(f"Текст: {note.body}\n")
            else:
                print("Заметок нет.")
        elif choice == "3":
            note_id = input("Введите ID заметки для редактирования: ")
            note = manager.find_note_by_id(note_id)
            if note:
                new_title = input("Введите новый заголовок: ")
                new_body = input("Введите новый текст: ")
                manager.update_note(note_id, new_title, new_body)
                print("Заметка обновлена.")
            else:
                print("Заметка не найдена.")
        elif choice == "4":
            note_id = input("Введите ID заметки для удаления: ")
            manager.delete_note(note_id)
            print("Заметка удалена.")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
