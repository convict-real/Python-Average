def main():
    try:
        first_number = input("Enter the first number: ")

        first_number = float(first_number)

        second_number = input("Enter the second number: ")

        second_number = float(second_number)

        numbers = [first_number, second_number]

        total_sum = sum(numbers)

        average = total_sum / 2

        if average.is_integer():
            average = int(average)
        else:
            average = float(average)

        print(f"Average: {average}")
    except ValueError:
        print("Value can only be a number.")
        return

if __name__ == "__main__":
    main()
