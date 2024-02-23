def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]

    highest = max(num_list)
    lowest = min(num_list)

    return f"{highest} {lowest}"

x = high_and_low("8 3")
print(x)