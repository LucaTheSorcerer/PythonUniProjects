def FileExractor(filename):
    """
    It extracts all the lines in f and append them to a new list
    :param filename:
    :return:
    """
    l = []
    with (open(filename) as f):
        for line in f:
            l.append(line.strip())

    return l