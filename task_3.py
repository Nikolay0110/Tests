stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def maximus(stats):
    stat = []
    name = []
    for k, v in stats.items():
        stat.append(v)
        name.append(k)

    maximum = max(stat)
    for index, item in enumerate(stat):
        if item == maximum:
            return name[index]


if __name__ == '__main__':
    print(maximus(stats))
