import json
import os


def load_json(file_path):
    """

    Args:
        file_path: путь к файлу который переводим из json в список со словарями

    Returns: список со словарями

    """
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            return json.load(file)
    else:
        print('Файл не существует')
        return


def get_student_by_pk(pk, students_list):
    """

    Args:
        pk: номер студента
        students_list: список из студентов с информацией о них в словарях

    Returns: информацию в виде словаря о выбранном студенте

    """
    if pk.isdigit():
        for student in students_list:
            if student['pk'] == int(pk):
                return student
    print('У нас нет такого студента')
    return


def get_profession_by_title(title, prof_list):
    """

    Args:
        title: профессия
        prof_list: список из профессий с информацией о них в словарях

    Returns: информацию в виде словаря о выбранной профессии

    """
    for prof in prof_list:
        if prof['title'].lower() == title.lower():
            return prof
    print('У нас нет такой специальности')
    return


def check_fitness(student, profession):
    """

    Args:
        student: словарь с выбранным студентом
        profession: словарь с выбранной профессией

    Returns: словарь с результатом обработки пригодности

    """
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])
    matching_skills = student_skills & profession_skills
    other_skills = profession_skills - student_skills
    return {"has": list(matching_skills),
            "lacks": list(other_skills),
            "fit_percent": len(matching_skills)*100//len(profession_skills),
            }
