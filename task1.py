import math


def total_salary(path: str) -> (int, int):
    with open(path, 'r') as file:
        lines = file.readlines()
        total = 0
        count = 0
        for line in lines:
            count += 1
            total += int(line.split(',')[1])
    return total, math.floor(total / count)


def main():
    total, average = total_salary('task1.csv')
    print(f'Total salary: {total}, average salary: {average}')


if __name__ == '__main__':
    main()