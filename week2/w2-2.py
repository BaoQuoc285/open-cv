import cv2
import numpy as np
img = cv2.imread('cho.jpg')

#chuyển màu ảnh sang mau bac

imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#có chức năng làm mờ ảnh (imgBlur = cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]))
imgBlur = cv2.GaussianBlur(img,(37,37),0)

#setting threshold values
#Hàm cv2.Canny() trong OpenCV được sử dụng để phát hiện cạnh trong hình ảnh.
#Cạnh là những vùng trong hình ảnh có sự thay đổi đột ngột của màu sắc hoặc độ sáng, thường được coi là ranh giới giữa các đối tượng trong hình ảnh.
t_lower = 120
t_higher = 300
edge = cv2.Canny(imGray,t_lower,t_higher)
kernel = np.ones((5,5),np.uint8)
# kernel = np.array([[1, 1, 1, 1, 1],
#                    [1, 2, 2, 2, 1],
#                    [1, 2, 5, 2, 1],
#                    [1, 2, 2, 2, 1],
#                    [1, 1, 1, 1, 1]], np.uint8)

dilated_img = cv2.dilate(edge, kernel, iterations=1)
erode = cv2.erode(dilated_img,kernel,iterations=1)
print(dilated_img)
cv2.imshow("original_output", edge)
# cv2.imshow("Gray_ouput", imGray)
# cv2.imshow("ouput1", imgBlur)
cv2.imshow("output2", erode)
cv2.waitKey(0)