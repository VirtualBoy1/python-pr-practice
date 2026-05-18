def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print("Приложение запущено")
    test_data = [10, 20, 30]
    avg = calculate_average(test_data)
    print(f"Среднее значение: {avg}")

if __name__ == "__main__":
    main()
