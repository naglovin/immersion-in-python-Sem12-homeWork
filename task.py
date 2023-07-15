# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.


class Grades:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_val}')
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_val}')


class Names:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        """Проверка на заглавную букву и отсутствие цифр"""
        if value.istitle() == False:
            raise ValueError(f'Значение {value} должно начинаться с  заглавной буквы ')
        if value.isalpha() == False:
            raise ValueError(f'Значение {value} не должно содержать цыфры')


class Subjects:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        data = []
        with open('subjects.txt', 'r', encoding='utf=8') as f:
            new_file = f.readlines()
            for line in new_file:
                data.append(''.join(line))

            if value not in data:
                raise ValueError(f'такого значения {value} нет в списке ')


class Student:
    last_name = Names
    first_name = Names
    father_name = Names

    grade = Grades(2, 5)
    exam = Grades(0, 100)

    subject = Subjects(str)

    def __init__(self, last_name, first_name, father_name, subject, grade, exam):
        self.last_name = last_name
        self.first_name = first_name
        self.father_name = father_name
        self.subject = subject
        self.exam = exam
        self.grade = grade


if __name__ == '__main__':
    student = Student('perov', 'pavel', 'kostomirovich', 'математика', 4, 50)
    student_2 = Student('мотин', 'фотин', 'фомилович', 'Информатика', 4, 99)
