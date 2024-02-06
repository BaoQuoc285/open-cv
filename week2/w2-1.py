import cv2

# #read img
# img = cv2.imread("C:/quocbao/thuchanh_open_cv/cho.jpg")

# cv2.imshow('output',img)
# cv2.waitKey(0)
# set chiều dài rộng và ddoojj tương phản
video = cv2.VideoCapture(0)
video.set(3,940)
video.set(4,480)
video.set(10,250)
# a là biến true false
#frame là tensor của từng ảnh
while True:
    a,frame = video.read()
    if a:
        cv2.imshow('video',frame)
   
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
    

video.release()
cv2.destroyAllWindows()