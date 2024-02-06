import cv2
import numpy as np

#this is gray scale image because have only 512 x 512 pixels or boxes
image = np.zeros((512,512))
#if we want to add the color functionality we have to give it the channel
image1 = np.zeros((512,512,3))

image1[:] = 255,0,0
#cv2.line(image, start_point, end_point, color, thickness=2)
cv2.line(image1,(20,30),(200,500),(0,255,0),3)

#cv2.rectangle(image, top_left, bottom_right, color, thickness=2)
cv2.rectangle(image1,(0,0),(250,350),(0,4,5),2)

#cv2.putText(image, text, position, font, font_scale, font_color, font_thickness)
#text: Chuỗi văn bản bạn muốn thêm vào hình ảnh.
#position: Tọa độ (x, y) của góc trái dưới của văn bản.
#font: Kiểu font chữ (ví dụ: cv2.FONT_HERSHEY_SIMPLEX).
#font_scale: Tỉ lệ thu nhỏ/phóng to của văn bản.
#font_color: Màu của văn bản (BGR).
#font_thickness: Độ dày của văn bản.
cv2.putText(image1, "quoc bao", (100,300),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
text = "Hello, OpenCV!"
position = (50, 200)

# Chọn font và kích thước
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  # Màu văn bản (trắng, BGR)
font_thickness = 2

# Thêm văn bản vào hình ảnh
cv2.putText(image1, text, position, font, font_scale, font_color, font_thickness)

# cv2.imshow("output", image)
cv2.imshow("output1", image1)
cv2.waitKey(0)