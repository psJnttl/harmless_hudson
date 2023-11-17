import random

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    weekly_draw = random.sample(number_pool, amount)
    weekly_draw.sort()
    return weekly_draw

if __name__ == '__main__':
    pass
