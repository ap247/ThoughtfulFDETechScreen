
def sort(width, height, length, mass):
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        return 'Fields must be positive'

    is_heavy = check_heavy(mass)
    is_bulky = check_bulky(width, height, length)

    if is_bulky and is_heavy:
        return 'REJECTED'
    elif is_bulky or is_heavy:
        return 'SPECIAL'
    else:
        return 'STANDARD'


def check_bulky(width, height, length):
    return width * height * length >= 1000000 or width >= 150 or height >= 150 or length >= 150


def check_heavy(mass):
    return mass >= 20


if __name__ == '__main__':
    # test cases
    print('sort(99, 99, 99, 19): ' + sort(99, 99, 99, 19))
    print('sort(149, 149, 149, 19): ' + sort(149, 149, 149, 19))
    print('sort(151, 20, 20, 19): ' + sort(151, 20, 20, 19))
    print('sort(151, 100, 110, 21): ' + sort(151, 100, 110, 21))
    print('sort(-1, 1, 1, 1): ' + sort(-1, 1, 1, 1))
    print('sort(1, -1, 1, -1): ' + sort(1, -1, 1, -1))
    print('sort(1, 1, 1, 0): ' + sort(1, 1, 1, 0))

