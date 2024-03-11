import pytesseract
import cv2
import numpy as np
import pytesseract
import pyscreeze
from utilities import cmd_printer
from skimage.metrics import structural_similarity as ssim


# (L352, T104, R780, B136)


def capture_screen(self):
    # left = 352
    # top = 104
    # right = 780
    # bottom = 136
    print(
        "get position of txtSN when capture screen called: ", self.MES_SN_INPUT_POSITION
    )
    left = self.MES_SN_INPUT_POSITION.left
    top = self.MES_SN_INPUT_POSITION.top
    right = self.MES_SN_INPUT_POSITION.right
    bottom = self.MES_SN_INPUT_POSITION.bottom
    position = (left, top, (right - left), (bottom - top))
    try:
        screenshot = pyscreeze.screenshot(region=position)
        screenshot = np.array(screenshot)
        return screenshot

    except Exception as E:
        print(E)


# def detect_label(screenshot):
#     pytesseract.pytesseract.tesseract_cmd = (
#         # r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#         r"./libs/Tesseract-OCR/tesseract.exe"
#     )
#     # config = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ</"
#     # config = r"--oem 3 --psm 6 outputbase digits tessedit_char_whitelist=0123456789"
#     config = r"--oem 3 --psm 6"
#     # config = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789</"
#     try:
#         # str_label = pytesseract.image_to_string(screenshot, config=config)
#         # txt_result = str_label.strip().split(" ")[-1]
#         # return txt_result
#         str_label = pytesseract.image_to_string(screenshot, config=config)
#         cmd_printer("SUCCESS", str_label)
#     except Exception as E:
#         print(E)


# def percent_matching():

#     # image_1st = cv2.imread("./test3.png")
#     # image_2rd = cv2.imread("./test1.png")

#     image_1st = capture_screen()
#     image_2rd = capture_screen()

#     image_1st = cv2.cvtColor(image_1st, cv2.COLOR_BGR2GRAY)
#     image_2rd = cv2.cvtColor(image_2rd, cv2.COLOR_BGR2GRAY)

#     cv2.imshow("1", image_1st)
#     cv2.imshow("2", image_2rd)
#     cv2.waitKey(0)

#     try:
#         similarity_index = cv2.matchTemplate(
#             image_1st, image_2rd, cv2.TM_CCOEFF_NORMED
#         )[0][0]

#         similarity_percentage = similarity_index * 100

#         return similarity_percentage
#     except Exception as E:
#         print(E)


# value = percent_matching()
# print(value)


def compare_image_ssim(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    similarity_index, _ = ssim(img1, img2, full=True)
    return float(similarity_index)


# img1 = capture_screen()
# img2 = capture_screen()

# compare_images_ssim(img1, img2)
