import cv2
import numpy as np

image = cv2.imread('th.jpg')
print("imageL: ",image)
width,height = 500,500
new_image = cv2.resize(image,(500,500))
# Tọa độ của 4 điểm trên hình ảnh gốc
pts1 = np.float32([[180,13],[276,40],[136,142],[230,175]])
print("pts1: " ,pts1.shape)
# Tọa độ của 4 điểm trên hình ảnh đích (muốn chuyển đổi thành)
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
print("pts2: ",pts2.shape)
# Tính ma trận chuyển đổi (Perspective Transform Matrix)
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print("matrix: ", matrix)
ouput = cv2.warpPerspective(image,matrix,(width,height))
cv2.imshow("output", ouput)
cv2.waitKey(0)