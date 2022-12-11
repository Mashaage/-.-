import random
def get_unique_list_numbers(a, b, c) -> list[int]:

    while True:
        uni = [random.randint(a,b) for _ in range(c)]
        if len(uni) == len(set(uni)):
            return uni
        else:
            continue


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
