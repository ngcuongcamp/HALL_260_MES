import cv2
from pylibdmtx.pylibdmtx import decode
import zxingcpp
import os
import numpy as np

path = "./images"


def process_frame(frame):
    # height, width, channels = frame.shape
    # print(f"Size of image: {width} x {height}")
    frame_cutted = frame[0:480, 100:640]
    frame = cv2.resize(frame_cutted, None, fx=1.0, fy=1.0)
    blur = cv2.GaussianBlur(src=frame, ksize=(3, 3), sigmaX=3, sigmaY=3)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    return gray


arr = []


def read_dmt_loop(frame):
    for threshold in range(0, 220, 3):
        _, thresh = cv2.threshold(frame, threshold, 220, cv2.THRESH_BINARY)
        data_decoded = zxingcpp.read_barcodes(thresh)
        if data_decoded:
            print(f" Thresh value: {threshold} ")
            arr.append(threshold)
            return data_decoded[0].text
        cv2.imshow("image", thresh)
        cv2.waitKey(1)
    return None


for index in os.scandir(path=path):
    frame = cv2.imread(index.path)

    gray = process_frame(frame)
    data_decoded = None

    max_loop = 10

    while max_loop >= 0:
        max_loop = max_loop - 1
        data = zxingcpp.read_barcodes(gray)
        if data:
            data_decoded = data[0].text
            break
        else:
            data = decode(gray, timeout=50)
            if data != []:
                data_decoded = data[0][0].decode("utf-8")
                break
    cv2.imshow("image", gray)
    cv2.waitKey(1)
    # if data_decoded is None:
    #     print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx", index.path)
    # else:
    #     print(data_decoded, index.path)

    if data_decoded is None:
        data_decoded = read_dmt_loop(gray)

    if data_decoded is not None:
        print(data_decoded, index.path)
    else:
        cv2.waitKey(0)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXX", index.path)

# print(f"{min(arr)} - {max(arr)}")
cv2.destroyAllWindows()
