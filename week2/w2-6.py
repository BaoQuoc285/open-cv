import cv2
import numpy as np

def empty(a):
    pass
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500,300)

cv2.createTrackbar("Hue Min ","Trackbar",0,179,empty)
cv2.createTrackbar("Hue Max ","Trackbar",179,179,empty)
cv2.createTrackbar("Sat Min ","Trackbar",0,255,empty)
cv2.createTrackbar("Sat Max ","Trackbar",255,255,empty)
cv2.createTrackbar("Val Min ","Trackbar",0,255,empty)
cv2.createTrackbar("Val Max ","Trackbar",255,255,empty)

while True:
    image = cv2.imread("car.jpg")
    image = cv2.resize(image,(300,200))
    new_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("Hue Min ","Trackbar")
    hmax = cv2.getTrackbarPos("Hue Max ","Trackbar")
    smin = cv2.getTrackbarPos("Sat Min ","Trackbar")
    smax = cv2.getTrackbarPos("Sat Max ","Trackbar")
    vmin = cv2.getTrackbarPos("Val Min ","Trackbar")
    vmax = cv2.getTrackbarPos("Val Max ","Trackbar")
    print(hmin,hmax,smin,smax,vmin,vmax)
    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])
    #cv2.inRange là một hàm trong thư viện OpenCV (Open Source Computer Vision) được sử dụng để chọn ra các phần tử trong một mảng (hoặc hình ảnh)
    # mà nằm trong một khoảng giá trị cụ thể. Thường thì, hàm này được sử dụng để tạo ra một masK, nơi mà giá trị của mỗi pixel trong ảnh sẽ được so sánh với một khoảng giá trị,
    # và các pixel nằm trong khoảng đó sẽ được chọn.
    #Công dụng chính của nó là làm việc với ảnh số và lọc ra các vùng quan trọng dựa trên mức độ sáng, màu sắc hoặc các đặc trưng khác:
    #---Chấm điểm ảnh (Image Thresholding)
    #---Phân đoạn hình ảnh (Image Segmentation):
    #---Tracking đối tượng :  bạn có thể sử dụng cv2.inRange để tạo mask giúp xác định vị trí của đối tượng trong khung hình.
    mask = cv2.inRange(new_image,lower,upper)
    cv2.imshow("output1",image)
    cv2.imshow("output2",new_image)
    cv2.imshow("output3",mask)
    cv2.waitKey(1)
cv2.destroyAllWindows()




