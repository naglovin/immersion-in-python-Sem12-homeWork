# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

from validate import Validate
class Student:
    """Базовый класс для всех студентов"""
    name = Validate
    frst_name = Validate
    lst_name = Validate
    std_count = 0

    def __init__(self, name, frst_name, lst_name, estimation, test_result):
        self.name = name
        self.frst_name = frst_name
        self.lst_name = lst_name
        self.estimation = estimation
        self.test_res = test_result
        Student.std_count += 1

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


    def display_count(self):
        print('Всего студентов: %d' % Student.std_count)

    def display_student(self):
        print('ФИО: {}  {}  {}. Оценка: {}. Результат теста: {}.'.format(self.name, self.frst_name,\
        self.lst_name, self.estimation, self.test_res))



if __name__ == '__main__':
    std1 = Student("aндрей", "Малюга", "Фатихович", 4, 100)
    std2 = Student("Мария", "Аликова", "Владимировна", 2, 69)
    std3 = Student("Семен", "Пестряков", "Александрович", 5, 89)
    std4 = Student("Ашот", "Ваншот", "С локтя выносович", 3, 50)
    std1.display_student()
    std2.display_student()
    std3.display_student()
    std4.display_student()
    print("Всего студентов: %d" % Student.std_count)


