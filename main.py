import cv2
import numpy as np
from faceDetector import faceDetector
from speech_api.jatts import jatts
def main():
    f=faceDetector()

    jatts("こんにちわ")

    # if ((username != "Unknown") & flag == False):
    #     flag = True
    #     jatts("こんにちわ" + username + "さん")



if __name__=='__main__':
    main()