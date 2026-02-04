import numpy as np
import matplotlib.pyplot as plt

STEP = 0.01

def make_x(choice: int) -> np.ndarray:
    two_pi = 2 * np.pi

    if choice == 3: 
        return np.arange(0.01, two_pi, STEP)

    if choice == 7:  
        return np.arange(-1.0, 1.0 + STEP, STEP)

    return np.arange(0.0, two_pi + STEP, STEP)

def compute_y(choice: int, x: np.ndarray) -> tuple[np.ndarray, str]:
    if choice == 1:
        y = np.tan(x)
        name = "y = tan(x)"
        y = np.where(np.abs(y) > 10, np.nan, y)
        return y, name

    if choice == 2:
        y = np.exp(x / np.pi)  
        name = "y = exp(x / π)"
        return y, name

    if choice == 3:
        y = np.log(x)
        name = "y = ln(x)"
        return y, name

    if choice == 4:
        y = x**3 + 2
        name = "y = x³ + 2"
        return y, name

    if choice == 5:
        y = 0.5 * x**4 - 2 * x**2 + x + 1
        name = "y = 0.5x⁴ - 2x² + x + 1"
        return y, name

    if choice == 6:
        y = np.sin(x) + 0.3 * np.cos(3 * x)
        name = "y = sin(x) + 0.3cos(3x)"
        return y, name

    if choice == 7:
        inside = 1 - x**2
        y = np.sqrt(np.clip(inside, 0, None))
        name = "y = √(1 - x²)"
        return y, name

    raise ValueError("Неизвестный выбор функции.")

def main():
    print("Выберите функцию для построения графика:")
    print("1) Тангенс y = tan(x)")
    print("2) Экспонента y = exp(x/π)")
    print("3) Логарифм y = ln(x)")
    print("4) Кубическая y = x^3 + 2")
    print("5) Полином y = 0.5x^4 - 2x^2 + x + 1")
    print("6) Периодическая y = sin(x) + 0.3cos(3x)")
    print("7) Радиальная y = sqrt(1 - x^2)")
    choice = int(input("Введите номер (1-7): ").strip())

    x = make_x(choice)
    y, title = compute_y(choice, x)

    plt.figure()
    plt.plot(x, y)
    plt.title(f"График функции: {title}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
