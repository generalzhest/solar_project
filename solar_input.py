# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = parse_star_parameters(line)
                objects.append(star)
            elif object_type == "planet":
                planet = parse_planet_parameters(line)
                objects.append(planet)

            else:
                print("Unknown space object")


    return objects


def parse_star_parameters(line):
    star = Star()
    s = line
    a = s.find(' ') #индекс первого пробела
    s = s[a+1:]
    a = s.find(' ')
    star.r = float(s[:a]) #радиус star
    s = s[a+1:]
    a = s.find(' ')
    star.color = s[:a] #
    s = s[a+1:]
    a = s.find(' ')
    star.m = float(s[:a])
    s = s[a+1:]
    a = s.find(' ')
    star.x = float(s[:a])
    s = s[a+1:]
    a = s.find(' ')
    star.y = float(s[:a])
    s = s[a+1:]
    a = s.find(' ')
    star.vx = float(s[:a])
    s = s[a+1:]
    a = s.find(' ')
    star.vy = float(s[:a])
    return star

    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    '''pass  # FIXME: not done yet'''

def parse_planet_parameters(line):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet = Planet()
    s = line
    a = s.find(' ') #индекс первого пробела
    s = s[a+1:]
    a = s.find(' ')
    planet.r = float(s[:a]) #радиус планеты
    s = s[a+1:]
    a = s.find(' ')
    planet.color = s[:a]
    s = s[a+1:]
    a = s.find(' ')
    planet.m = float(s[:a]) #масса планеты
    s = s[a+1:]
    a = s.find(' ')
    planet.x = float(s[:a])
    s = s[a+1:]
    a = s.find(' ')
    planet.y = float(s[:a])
    s = s[a+1:]
    a = s.find(' ')
    planet.vx = float(s[:a])
    s = s[a+1:]
    a = s.find(' ')
    planet.vy = float(s[:a])
    #pass  # FIXME: not done yet...
    return planet


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%f %s %f %f %f %f %f" % (obj.r, obj.color, obj.m, obj.x, obj.y, obj.vx, obj.vy))
            # FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
