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

if __name__ == '__main__':
    pass
