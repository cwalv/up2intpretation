#!/usr/bin/env python

import time
import ctypes
import logging

# This could be read from the header, but I just hard coded it here for easy comparison
w, h = 2209, 1657
fn = './mountain-spring.bmp'
outfn = './test.bmp'

def ctypes_grayscale(fn, w, h, outfn):
    lh = ctypes.CDLL('./bitmap_greyscale.so')
    imgbuf = ctypes.POINTER(ctypes.c_ubyte)()
    lh.read_grayscale_bmp(fn, w, h, ctypes.byref(imgbuf))
    lh.write_bmp(outfn, imgbuf, w, h)

def python_grayscale(fn, w, h, outfn):
    header_sz = 54
    bmppad_sz = (4 - (w * 3) % 4) % 4
    row_sz = w * 3

    with open(fn, 'rb') as fp:
        imgbytes = fp.read()
    
    img_rows = []
    for row_idx in range(h):
        row_start_idx = header_sz + (row_sz + bmppad_sz) * row_idx
        img_rows.append(imgbytes[row_start_idx:row_start_idx + row_sz])
    # assert len(img_rows) == h
    # assert all(len(row) == w * 3 for row in img_rows)

    grayscale_rows = []
    for row in img_rows:
        grayscale_row = []
        for pix_idx in range(0, w * 3, 3):
            pix_bytes = row[pix_idx:pix_idx + 3]
            b, g, r = map(ord, pix_bytes)
            ciey = .212671 * r + .715160 * g + .072169 * b
            grayscale_pix_bytes = chr(int(ciey)) * 3
            grayscale_row.append(grayscale_pix_bytes)
        grayscale_rows.append(''.join(grayscale_row))
    # assert len(grayscale_rows) == h
    # assert all(len(row) == w * 3 for row in grayscale_rows)

    with open(outfn, 'wb') as outfp:
        outfp.write(imgbytes[:header_sz])
        for row in grayscale_rows:
            outfp.write(row)
            outfp.write('\0' * bmppad_sz)


if __name__ == '__main__':
    start_time = time.time()
    
    ctypes_grayscale(fn, w, h, './ctypes_test.bmp')
    ctypes_time = time.time() - start_time

    python_grayscale(fn, w, h, './py_test.bmp')
    py_time = time.time() - start_time

    logging.basicConfig(level=logging.INFO)
    logging.info("""
    ctypes time: {}
    python time: {}
    diff: {}
    % diff: {}
    """.format(ctypes_time, py_time, py_time - ctypes_time, (py_time - ctypes_time) / py_time))
