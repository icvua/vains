import numpy as np
import cv2
from matplotlib import pyplot as plt


g = float(input("Gamma is : "))
img = cv2.imread("C:\\Users\\Elsholtzia\\Pictures\\lenna.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
out = img.copy()  # out에 원본 이미지를 그대로 복사
out = out.astype(float)  # out 이미지의 모든 값을 float으로 변환해줘야 float인 감마를 곱할 수 있다. 원래는 int다.
out = ((out / 255) ** (1 / g)) * 255  # out / 255를 통해 모든 값을 정규화해주고(0-1 로 변환) 1 / 감마값 만큼 제곱해준다. 제곱하는 이유는 값이 높아질수록 밝기가 같이 올라가게 하기 위해. 그리고 다시 255를 곱해준다
out = out.astype(np.uint8)  # 다시 int로 변경
# out = 255 - out

plt.subplot(121), plt.imshow(img, cmap='gray', vmin=0, vmax=255), plt.title('plate')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out, cmap='gray', vmin=0, vmax=255), plt.title('rgb image')
plt.xticks([]), plt.yticks([])
plt.show()