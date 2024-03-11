from libs.libs import cv2, decode, zxingcpp


def read_dmt_zxingcpp(frame):
    data_decoded = zxingcpp.read_barcodes(frame)
    if data_decoded:
        if len(data_decoded[0].text) == 17:
            return data_decoded[0].text
    return read_dmt_pylibdmtx(frame)


def read_dmt_pylibdmtx(frame):
    data = decode(frame, timeout=50)
    if data != []:
        data = data[0][0].decode("utf-8")
        if len(data) == 17:
            return data
    return None


def read_dmt_loop(self, frame):
    # print(self.MIN_THRESH, self.MAX_THRESH, self.THRESH_JUMP)
    for threshold in range(self.MIN_THRESH, self.MAX_THRESH, self.THRESH_JUMP):
        _, thresh = cv2.threshold(frame, threshold, self.MAX_THRESH, cv2.THRESH_BINARY)
        # print('loop 3')
        data_decoded = zxingcpp.read_barcodes(thresh)
        if data_decoded and data_decoded[0].text == 17:
            return data_decoded[0].text
    return None


def process_frame(frame):
    # 640 x 480

    frame = cv2.resize(frame, None, fx=1, fy=1)
    # blur = cv2.GaussianBlur(frame, (5, 5), 0)
    blur = cv2.GaussianBlur(src=frame, ksize=(3, 3), sigmaX=3, sigmaY=3)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    return gray
