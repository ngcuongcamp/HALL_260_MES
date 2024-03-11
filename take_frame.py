import cv2
import zxingcpp
from pylibdmtx.pylibdmtx import decode
import time

capture = cv2.VideoCapture(0)


def read_dmt_zxingcpp(frame):
    data_decoded = zxingcpp.read_barcodes(frame)
    if data_decoded:
        return data_decoded[0].text
    else:
        return read_dmt_pylibdmtx(frame)


def read_dmt_pylibdmtx(frame):
    data = decode(frame, timeout=50)
    if data != []:
        data = data[0][0].decode("utf-8")
        return data
    else:
        return None


def read_dmt_loop(frame):
    for threshold in range(30, 70, 3):
        _, thresh = cv2.threshold(frame, threshold, 70, cv2.THRESH_BINARY)
        data_decoded = zxingcpp.read_barcodes(thresh)
        if data_decoded != []:
            print("thresh value: ", threshold)
            return data_decoded[0].text
        else:
            data = decode(frame, timeout=50)
            if data != []:
                data = data[0][0].decode("utf-8")
                print("thresh value: ", threshold)
                return data
    return None


def on_press_space(frame):
    cv2.imwrite(f"./image_2/{time.time()}.png", frame)

    # max_loop = 3
    # while max_loop > 0:
    #     max_loop = max_loop - 1
    #     data_decoded = read_dmt_zxingcpp(frame)
    #     if data_decoded is not None:
    #         break

    blur = cv2.GaussianBlur(src=frame, ksize=(5, 5), sigmaX=3, sigmaY=3)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    data_decoded = read_dmt_zxingcpp(gray)
    if data_decoded is None:
        data_decoded = read_dmt_loop(gray)
        if data_decoded is None:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        else:
            print(data_decoded)
    else:
        print(data_decoded)


if not capture.isOpened():
    print("Error: Unable to open the camera or video source.")
    exit()

while True:
    ret, frame = capture.read()

    if not ret or frame is None:
        print("Error: Unable to capture frame.")
        break
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 32:
        on_press_space(frame=frame)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
