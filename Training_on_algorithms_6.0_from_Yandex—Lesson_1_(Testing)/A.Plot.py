#Левый нижний угол
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
#Правый верхний угол
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
#Чел
x = int(input('Введите x: '))
y = int(input('Введите y: '))


def direction_to_swimmer(x1, y1, x2, y2, x, y):
    if y < y1:  # Пловец южнее плота
        vertical = 'S'
    elif y > y2:  # Пловец севернее плота
        vertical = 'N'
    else:
        vertical = ''

    if x < x1:  # Пловец западнее плота
        horizontal = 'W'
    elif x > x2:  # Пловец восточнее плота
        horizontal = 'E'
    else:
        horizontal = ''



    return vertical+horizontal

# Пример использования:
print(direction_to_swimmer(x1, y1, x2, y2, x, y))
