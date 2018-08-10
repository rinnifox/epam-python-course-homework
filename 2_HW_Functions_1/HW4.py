def letters_range(*args):

    """
    letters_range is analogue of built-in range function
    letters_range works in the same way but uses latin letters instead of numbers

    *args = [start], stop[, step]
    """

    output = list()

    if len(args) == 3:
        start, stop, step = args
        if step == 0:
            return output
    elif len(args) == 2:
        start, stop = args
        step = 1
    else:
        stop = args[0]
        start = 'a'
        step = 1

    for elem in range(ord(start), ord(stop), step):
        output.append(chr(elem))

    return output
