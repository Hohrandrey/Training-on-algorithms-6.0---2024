#Левый нижний угол
x1 = int(input(''))
y1 = int(input(''))
#Правый верхний угол
x2 = int(input(''))
y2 = int(input(''))
#Чел
x = int(input(''))
y = int(input(''))


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
