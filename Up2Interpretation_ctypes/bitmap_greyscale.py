#!/usr/bin/env python

import ctypes

w, h = 2209, 1657

lh=ctypes.CDLL('./bitmap_greyscale.so')

imgbuf = ctypes.POINTER(ctypes.c_ubyte)()
lh.read_grayscale_bmp('./mountain-spring.bmp', w, h, ctypes.byref(imgbuf))
lh.write_bmp('./test.bmp', imgbuf, w, h)

