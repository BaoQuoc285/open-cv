import cv2

img = cv2.imread('cho.jpg')
print("origianl image: " ,img.shape)
#----->1000 ----> resize image width
#----->650 -----> resize image height
#width
#----------------------->
#|
#|
#|
#|
#|
#|
#- height
image_re = cv2.resize(img,(1000,650))
print("resize image: " ,image_re.shape)
#crop image
#the first parameter is height and the second is width
img2 = img[200:500,20:700]

cv2.imshow("orignal: ",img)
cv2.imshow("reize_picture: ",img2)
cv2.waitKey(0)