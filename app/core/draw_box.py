"""
    Это спизженный код от сюда: https://github.com/waittim/draw-YOLO-box/blob/main/draw_box.py
"""

import os
import random

import cv2


def plot_one_box(x, image, color=None, label=None, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(
        0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(image, label, (c1[0], c1[1] - 2), 0, tl / 3,
                    [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)


def draw_box_on_image(idxywhn, classes: tuple[str], colors: tuple[tuple[float]], raw_image_path: str, output_image_path: str):
    """
    This function will add rectangle boxes on the images.
    """
    image = cv2.imread(raw_image_path)
    try:
        height, width, channels = image.shape
    except:
        print('no shape info.')
        return 0

    box_number = 0
    for item in idxywhn:  # 例遍 txt文件得每一行  # 对每行内容 通过以空格为分隔符对字符串进行切片
        class_idx = int(item[0])

        x_center, y_center, w, h = float(item[1]) * width, float(item[2]) * height, float(item[3]) * width, float(item[4]) * height
        x1 = round(x_center - w / 2)
        y1 = round(y_center - h / 2)
        x2 = round(x_center + w / 2)
        y2 = round(y_center + h / 2)

        plot_one_box([x1, y1, x2, y2], image, color=colors[class_idx],
                     label=classes[class_idx], line_thickness=None)

        cv2.imwrite(output_image_path, image)

        box_number += 1
    return box_number
