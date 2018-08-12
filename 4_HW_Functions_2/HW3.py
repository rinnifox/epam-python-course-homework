def triangle_points(*args):

    (x1, y1), (x2, y2),(x3, y3) = args
    x_list = [x1, x2, x3]
    y_list = [y1, y2, y3]

    points_counter = 0

    for i in range(min(x_list), max(x_list)+1):
        for j in range(min(x_list), max(y_list)+1):
            w1 = (i - x1) * (y2 - y1) - (j - y1) * (x2 - x1)
            w2 = (i - x2) * (y3 - y2) - (j - y2) * (x3 - x2)
            w3 = (i - x3) * (y1 - y3) - (j - y3) * (x1 - x3)

            if (w1 > 0 and w2 > 0 and w3 > 0) or (w1 > 0 and w2 > 0 and w3 > 0) or w1 == 0 or w2 == 0 or w3 == 0:
                points_counter += 1

    return points_counter
