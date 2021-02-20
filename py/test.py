import random
import math

correct = 0
it = 0
while correct < 224:
    it += 1
    correct = 0
    c = []
    for point in range(15):
        c.append([random.random(), random.random()])
    for p1 in c:
        for p2 in c:
            d = math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1] - p2[1], 2))
            if d > 0.05 or d < 0.00001:
                print('ok  ' + str(d))
                correct += 1
            else:
                print('no  ' + str(d))
print(it)
print(c)
# import random
# import math
#
# run = True
# correct = 0
#
#
# while correct < 99:
#     correct = 0
#     print(correct)
#     correct = 0
#     x = []
#     y = []
#     for point in range(100):
#         x.append(random.random())
#         y.append(random.random())
#
#     for pos_x1 in x:
#         for pos_x2 in x:
#             for pos_y1 in y:
#                 for pos_y2 in y:
#
#         #     if math.sqrt(pos_x**2 + pos_y**2) < 0.005:
#         #         correct = correct + 0
#         #     else:
#         #         correct = correct + 1
