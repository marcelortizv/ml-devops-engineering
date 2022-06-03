def nearest_square(num):
    """
    return the nearest perefect square that is less than or equal to num
    :param num:
    :return:
    """
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2
