# import ffmpeg
#
# path = 'D:\\4_School_Works\\2022_Gradproj\\'
# basefile = path + 'chopsticks_credit.mp4'
# # print(basefile)
# stream = ffmpeg.input(basefile)
# stream = ffmpeg.hflip(stream)
# stream = ffmpeg.output(stream, path+'test.mp4')
# ffmpeg.run(stream)
import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('C:\\Users\\Elsholtzia\\Pictures\\lenna.png')
rgb_img = cv.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
ret, dst = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)


plt.subplot(131), plt.imshow(dst, cmap='gray', vmin=0, vmax=255), plt.title('executed image')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(rgb_img, cmap='gray', vmin=0, vmax=255), plt.title('rgb image')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(gray_img, cmap='gray', vmin=0, vmax=255), plt.title('grayscale image')
plt.xticks([]), plt.yticks([])

plt.show()
