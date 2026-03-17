import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r" \d+(?:\.\d+)? "
    matches = re.findall(pattern, text)
    for m in matches:
        yield m.strip()

def sum_profit(text: str, func: Callable):
    return sum(float(x) for x in func(text))


text = "1000.01 дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений " \
"додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

