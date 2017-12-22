# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import cv2


class FrameRate:
    def __init__(self):
        self._count = 0
        self._fps = 0
        self._freq = 1000 / cv2.getTickFrequency()
        self._tmStart = cv2.getTickCount()
        self._tmNow = cv2.getTickCount()

    def get(self):
        self._count += 1
        self._tmNow = cv2.getTickCount()
        tmDiff = (self._tmNow - self._tmStart) * self._freq
        if tmDiff >= 1000:
            self._tmStart = self._tmNow
            self._fps = self._count
            self._count = 0
        return self._fps