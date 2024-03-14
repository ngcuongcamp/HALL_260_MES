import pytesseract
import cv2
import numpy as np
import pytesseract
import pyscreeze
from utilities import cmd_printer
from skimage.metrics import structural_similarity as ssim
import pyautogui


def capture_screen(position):
    position = (
        position.left,
        position.top,
        (position.right - position.left),
        (position.bottom - position.top),
    )
    try:
        screenshot = pyscreeze.screenshot(region=position)
        screenshot = np.array(screenshot)
        return screenshot

    except Exception as E:
        print(E)


def compare_image_ssim(img1, img2):
    try:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        similarity_index, _ = ssim(img1, img2, full=True)
        percent_matching = round(float(similarity_index), 3)
        print("percent matching: ", percent_matching)

        # if percent matching smaller than 1.0 -> two images deference true
        # equal 1.0 -> same -> return false
        if percent_matching < 1.0:
            return False
        elif percent_matching == 1.0:
            return True
        else:
            print("Throw error when compare two images")

    except Exception as E:
        print(E)


def lookup_screenshot(template):
    try:
        position = pyscreeze.locateOnScreen(
            image=template,
            region=None,
            grayscale=True,
            confidence=0.998,
            minSearchTime=0.01,
        )
        if position:
            return True
    except Exception as E:
        print(E)
        return True


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
