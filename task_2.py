ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def unique_id(ids):
    new_list = []

    for user, number in ids.items():
        new_list.extend(number)

    return list(set(new_list))


if __name__ == '__main__':
    print(unique_id(ids))
