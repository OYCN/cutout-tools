import cv2
import numpy as np

img_path = 'imgs/raccoon-7228457.jpg'
img = cv2.imread(img_path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
canvas = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('canvas', cv2.WINDOW_NORMAL)


drawing = False
color = 0
size = 100
def draw_circle(event, x, y, flags, param):
    global drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(canvas, (x, y), size, color, -1)
            cv2.circle(img, (x, y), size, (0, color, 0), -1)
            print(f'draw at ({x}, {y}): {color}')

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.setMouseCallback('img', draw_circle) # 设置鼠标事件的回调函数

while(1):
    cv2.imshow('img', img)
    cv2.imshow('canvas', canvas)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        color = 0
    elif k == ord('w'):
        color = 128
    elif k == ord('e'):
        color = 255
    elif k == ord('-'):
        size -= 10
    elif k == ord('='):
        size += 10
    elif k == ord('s'):
        cv2.imwrite('imgs/out.jpg', canvas)
    elif k == 27:
        break
cv2.destroyAllWindows()