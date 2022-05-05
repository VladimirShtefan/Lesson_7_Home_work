# импортируем наши созданные функции и библиотеку для формирования пути к файлам
import functions
from os.path import join
# указываем путь к файлам
Path_file_students = join("json_files", "students.json")
Path_file_professions = join("json_files", "professions.json")


def main():
    # вызываем функции которые возвращают данные из файлов в виде списка со словарями
    dict_all_students = functions.load_json(Path_file_students)
    dict_all_professions = functions.load_json(Path_file_professions)

    if dict_all_students is None or dict_all_professions is None:
        print('Фаил не найден')
    else:
        # спрашиваем у пользователя номер студента
        user_input = input('Добро пожаловать.\nВведите номер студента: ')

        # вызываем функцию, которая возвращает данные о студенте в виде словаря
        dict_student = functions.get_student_by_pk(user_input, dict_all_students)

        # проверяем что вернулась не пустота
        if dict_student is not None:
            # выводим информацию
            full_name = dict_student["full_name"]
            print(f'Студент {full_name}')
            skills = ", ".join(dict_student["skills"])
            print(f'Знает: {skills}')

            # спрашиваем о профессии
            user_profession = input(f'Выберите специальность для оценки студента {full_name}: ')
            # вызываем функцию, которая возвращает данные о выбранной профессии
            dict_profession = functions.get_profession_by_title(user_profession, dict_all_professions)

            # проверяем что вернулась не пустота
            if dict_profession is not None:
                # вызываем функцию для обработки пригодности и выводим результаты
                check_fitness = functions.check_fitness(dict_student, dict_profession)
                print(f'Пригодность {check_fitness["fit_percent"]}')
                check_has = ", ".join(check_fitness["has"])
                check_lacks = ", ".join(check_fitness["lacks"])
                print(f'{full_name} знает {check_has}')
                print(f'{full_name} не знает {check_lacks}')
            else:
                print('У нас нет такой профессии')
        else:
            print('У нас нет такого студента')


if __name__ == '__main__':
    main()
