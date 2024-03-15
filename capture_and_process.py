import pytesseract
import cv2
import numpy as np
import pytesseract
import pyscreeze
from utilities import cmd_printer
from skimage.metrics import structural_similarity as ssim
import pyautogui
import time


def capture_screen(position):
    # position = (
    #     position.left,
    #     position.top,
    #     (position.right - position.left),
    #     (position.bottom - position.top),
    # )
    position = (
        position[0],
        position[1],
        (position[2] - position[0]),
        (position[3] - position[1]),
    )
    try:
        screenshot = pyscreeze.screenshot(region=position)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        return screenshot

    except Exception as E:
        print(E)


img1 = cv2.imread("./temp/1.png")
img2 = cv2.imread("./temp/2.png")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


def compare_image_ssim(img1, img2):
    try:
        similarity_index, _ = ssim(
            img1,
            img2,
            full=True,
        )
        percent_matching = round(float(similarity_index), 3)
        print("percent matching: ", percent_matching)

        # if percent matching smaller than 1.0 -> two images deference true
        # equal 1.0 -> same -> return false
        # if percent_matching < 1.0:
        if percent_matching < 0.98:
            return False
        elif percent_matching >= 0.98:
            return True
        else:
            print("Throw error when compare two images")

    except Exception as E:
        print(E)


stime = time.time()
result = compare_image_ssim(img1, img2)
etime = time.time() - stime
print(result, f"time used: {etime}")


def lookup_screenshot(self, template):
    try:
        position = pyscreeze.locateOnScreen(
            image=template,
            # region=None,
            # L229, T44, R826, B493
            # region=(229, 44, 826, 493),
            # region=(
            #     self.MES_AREA_SNAPSHOT_POSITION[0],
            #     self.MES_AREA_SNAPSHOT_POSITION[1],
            #     self.MES_AREA_SNAPSHOT_POSITION[2],
            #     self.MES_AREA_SNAPSHOT_POSITION[3],
            # ),
            region=(
                self.MES_SN_INPUT_POSITION[0] - 25,
                self.MES_SN_INPUT_POSITION[1] - 25,
                self.MES_SN_INPUT_POSITION[2] + 25,
                self.MES_SN_INPUT_POSITION[3] + 25,
            ),
            grayscale=True,
            confidence=self.MES_COMPARE_CONFIDENCE,
            minSearchTime=0.01,
        )
        if position:
            return True
    except Exception as E:
        print(E)
        return False
        # return True


# template = cv2.imread("./temp/test.png")
# is_found = lookup_screenshot(template)
# print(is_found)


def detect_label(screenshot):
    pytesseract.pytesseract.tesseract_cmd = r"./libs/Tesseract-OCR/tesseract.exe"
    # config = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ</"
    # config = r"--oem 3 --psm 6 outputbase digits tessedit_char_whitelist=0123456789"
    config = r"--oem 3 --psm 6"
    # config = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789</"
    try:
        # str_label = pytesseract.image_to_string(screenshot, config=config)
        # txt_result = str_label.strip().split(" ")[-1]
        # return txt_result
        str_label = pytesseract.image_to_string(screenshot, config=config)
        cmd_printer("SUCCESS", str_label)
    except Exception as E:
        print(E)
