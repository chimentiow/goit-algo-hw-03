import random
min = int(input(f"Введіть мінімальне число , яке буде не меньше 1:  "))
max = int(input(f"Введіть максимальне число , яке буде не більше 1000:  "))
quantity = int(input(f"Введіть скільки чисел повинно бути вибрані з діапазану від {min} до {max} "))

def get_numbers_ticket(min, max, quantity):
    if not isinstance(min , int) and isinstance(max , int) and isinstance(quantity , int) or min < 1 or max > 1000 or quantity < 1:
        return []
    numbers = random.sample(range(min, max), quantity)
    return sorted(numbers)

print ("Ваші лотерейні номерки :", (get_numbers_ticket(min , max , quantity)))