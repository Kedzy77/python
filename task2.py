def sumofmissnum(numbers: list[int]) -> int:

    min_num = min(numbers)
    max_num = max(numbers)

    full_range = set(range(min_num, max_num + 1))

    missnum= full_range - set(numbers)
    return sum(missnum)

print(sumofmissnum([1, 3, 5, 7, 10]))
print(sumofmissnum([10, 7, 5, 3, 1]))
print(sumofmissnum([10, 20, 30, 40, 50, 60]))

