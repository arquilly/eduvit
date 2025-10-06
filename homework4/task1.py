list1 = [int(x)**2 for x in range(1,11)]

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
dct1 = {day: i for i, day in enumerate(days, start=1)}

tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
set1 = {tag.lower() for tag in tags}

list2 = [1, 3, 4, 87, 98, 15, 7, 4]
list3 = [int(x) for x in list2 if x % 2 == 0]

import math
dct2 = {i: math.factorial(i) for i in range(1, 6)}

print(f"1. {list1}\n2. {dct1}\n3. {set1}\n4. {list3}\n5. {dct2}")

