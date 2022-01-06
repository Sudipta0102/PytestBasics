def test_add(numbers):
    assert numbers[0] + numbers[1] == 8, f"expected:{numbers[0] + numbers[1]}, result: {8}"


def test_sub(numbers):
    assert numbers[1] - numbers[0] == 2, f"expected:{numbers[1] - numbers[0]}, result: {2}"


