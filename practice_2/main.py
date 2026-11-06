def chairs_per_row(chairs, rows):
    return chairs / rows if rows != 0 else "На ноль делить нельзя"


assert chairs_per_row(72, 9) == 8
assert chairs_per_row(64, 0) == "На ноль делить нельзя"
assert chairs_per_row(49, 7) == 7
print(chairs_per_row(66, 6) == 11)

words = ["ряд", "класс", "библиотека"]
print(sorted(words, key=lambda word: len(word)))
