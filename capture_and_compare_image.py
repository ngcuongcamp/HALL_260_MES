import pytesseract
import cv2
import numpy as np
import pytesseract
import pyscreeze
from utilities import cmd_printer
from skimage.metrics import structural_similarity as ssim


def capture_screen(position):
    # (L352, T104, R780, B136)
    # cmd_printer(
    #     "INFO",
    #     f"get position of txtSN: {self.MES_SN_INPUT_POSITION}",
    # )

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
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    similarity_index, _ = ssim(img1, img2, full=True)
    return round(float(similarity_index), 2)
