from ultralytics import YOLO
import os

from our_solutions.paths import get_weight_yolo

model = YOLO(get_weight_yolo(name='best_28'))

model.fuse()

n = 0

for filename in os.listdir("../static/test_transformed_data/"):
    print(filename)
    # try:
    #     results = model(
    #         "C:/Users/filip/PycharmProjects/hackathon-perm/our_solutions/static/test_transformed_data/".format(
    #             filename), save_txt=True, conf=0.4)
    # except FileNotFoundError:
    #     print("Not Found")
    break
