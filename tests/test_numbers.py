import pytest

from mathlib import numbers


@pytest.mark.parametrize(
    ["integers", "expected"],
    [[[], 0], [[45], 45], [[0, 8], 8], [[1, 2], 1], [[6, 4], 2], [[4, 2, 198, 6], 2]],
)
def test_gcd(integers, expected):
    assert numbers.gcd(*integers) == expected


@pytest.mark.parametrize(
    ["integers", "expected"],
    [
        [[], 1],
        [[45], 45],
        [[0, 8], 0],
        [[1, 2], 2],
        [[6, 4], 12],
        [[1, 2, 3, 4, 6], 12],
    ],
)
def test_lcm(integers, expected):
    assert numbers.lcm(*integers) == expected


@pytest.mark.parametrize(["a", "b"], [[7, 3], [872, 7959], [7959, 872], [42, 35129]])
def test_modular_inverse(a, b):
    inverse = numbers.modular_inverse(a, b)
    assert 0 < inverse < b
    assert (a * inverse) % b == 1


@pytest.mark.parametrize(
    ["n", "expected"],
    [[0, 1], [1, 1], [2, 2], [-11, 144], [-10, -89], [25, 121393], [40, 165580141]],
)
def test_fibonacci(n, expected):
    assert numbers.fibonacci(n) == expected


@pytest.mark.parametrize(
    ["initial", "count", "expected"],
    [[[0, 7], 4, [0, 7, 7, 14]], [[1, 1], 5, [1, 1, 2, 3, 5]]],
)
def test_fibonacci_numbers(initial, count, expected):
    fibonacci = numbers.fibonacci_numbers(*initial)
    result = [next(fibonacci) for _ in range(count)]
    assert result == expected


@pytest.mark.parametrize(
    ["n", "k", "expected"],
    [
        [0, 0, 1],
        [7, 0, 1],
        [7, 1, 7],
        [7, 2, 21],
        [7, 3, 35],
        [7, 4, 35],
        [7, 5, 21],
        [7, 6, 7],
        [7, 7, 1],
        [8, 0, 1],
        [8, 1, 8],
        [8, 2, 28],
        [8, 3, 56],
        [8, 4, 70],
        [8, 5, 56],
        [8, 6, 28],
        [8, 7, 8],
        [8, 8, 1],
    ],
)
def test_binomial(n, k, expected):
    assert numbers.binomial(n, k) == expected


@pytest.mark.parametrize(
    ["s", "n", "expected"], [[3, 4, 10], [4, 8, 64], [5, 5, 35], [6, 3, 15]]
)
def test_polygonal_number(s, n, expected):
    assert numbers.polygonal_number(s, n) == expected
