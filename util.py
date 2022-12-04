import os
from datetime import date

from aocd import get_data


def get_advent_of_code_file_of_day(day, year=2022):
    data = get_data(day=day, year=year)
    day_str = str(day).zfill(2)
    if not os.path.exists(f"Day{day_str}"):
        os.makedirs(f"Day{day_str}")
    with open(f"Day{day_str}/day{day_str}.txt", "w") as f:
        f.write(data)


if __name__ == '__main__':
    get_advent_of_code_file_of_day(date.today().day)
