
def get_cats_info(path: str) -> [dict]:
    with open(path, 'r') as file:
        lines = file.readlines()
        cats_info = []
        for line in lines:
            cat_id, name, age = line.split(',')
            cats_info.append({'id': cat_id, 'name': name, 'age': int(age)})

    return cats_info


def main():
    cats_info = get_cats_info('task2.csv')
    print(cats_info)


if __name__ == '__main__':
    main()