from homework1.task04 import check_sum_of_four


def test_1_check_sum_of_four():
    a = [1, 5]
    b = [0, -4]
    c = [2, -8]
    d = [3, 7]
    assert check_sum_of_four(a, b, c, d) == 3


def test_2_check_sum_of_four():
    a = [0, 0]
    b = [0, 0]
    c = [0, 0]
    d = [0, 0]
    assert check_sum_of_four(a, b, c, d) == 16
