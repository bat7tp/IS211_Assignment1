
# Part 1 of Assignment 1


def list_divide(numbers, divide=2):
    list = []
    for x in numbers:
        if x % divide == 0:
            list.append(x)
    return (len(list))


def test_list_divide():
    a = list_divide([1, 2, 3, 4, 5])

    if a != 2:
        raise List_Divide_Exception()

    b = list_divide([2, 4, 6, 8, 10])

    if b != 5:
        raise List_Divide_Exception()

    c = list_divide([30, 54, 63, 98, 100], divide=10)

    if c != 2:
        raise List_Divide_Exception()

    d = list_divide([])

    if d != 0:
        raise List_Divide_Exception()

    e = list_divide([1, 2, 3, 4, 5], 1)

    if e != 5:
        raise List_Divide_Exception()


class List_Divide_Exception(Exception):
    pass


test_list_divide()
