def add_one(num):
    if num == 3:
        return
    count = num + 1
    print(count)
    return add_one(count)


add_one(0)
