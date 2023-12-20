import random

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    weekly_draw = random.sample(number_pool, amount)
    weekly_draw.sort()
    return weekly_draw

def get_lottery_numbers(amount: int, start: int, end: int):
    output = "<span class='lotto-numbers'>"
    for number in lottery_numbers(amount, start, end):
        output += f'{number} '
    output += "</span>"
    return output

def get_eurojackpot_lottery_numbers():
    output = "<span class='lotto-numbers'>"
    for number in lottery_numbers(5, 1, 50):
        output += f'{number} '
    output += "</span><span class='star-numbers'>"
    for number in lottery_numbers(2, 1, 12):
        output += f'{number} '
    output += "</span>"
    return output

def get_joker_numbers():
    result = []
    for i in range(7):
        next_number = random.randint(0, 9)
        result.append(next_number)
    return result

if __name__ == '__main__':
    pass
