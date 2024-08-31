def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def number_exploration_tool():
    name = "Mian Muhammad Abdullah"
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))
    numbers = [num1, num2, num3]
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    for num, parity in even_odd_list:
        print(f"The number {num} is {parity}.")
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num**2})")
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")
number_exploration_tool()
