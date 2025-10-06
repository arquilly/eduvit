import random
from pathlib import Path

for i in range(10):
    symbols = '0123456789abcdefghijklmnopqrstuvwxyz'
    filename="homework5/"
    for j in range(8):
        filename += random.choice(symbols)
    filename+=".txt"
    file = Path(filename)
    file.touch()
    print(file.absolute())
