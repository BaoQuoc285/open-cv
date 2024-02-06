import cv2

img = cv2.imread('shape.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh_min = 200
thresh_max = 300

new_img = cv2.Canny(img_gray,thresh_min,thresh_max)

contours, _ = cv2.findContours(new_img .copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img1 = img.copy()
# cv2.drawContours(img1,contours,3,(0,255,0),8)
print(len(contours))
for cnt in contours:
    # print(cnt)
    #tinh dien tich 
    area = cv2.contourArea(cnt)
    # print(len(cnt))
    # print(area)
    cv2.drawContours(img1,cnt,-1,(0,255,0),8)
    
    # được sử dụng để tính độ dài của một đường cong hoặc một đa giác.(giống như tính chu vi)
    arc_length = cv2.arcLength(cnt, True)
    # Điều này thường được sử dụng để giảm số lượng điểm cần thiết để mô tả một đường cong.(giảm số lượng điểm có trong cnt)
    approx_curve = cv2.approxPolyDP(cnt, arc_length * 0.02, True)
    # print(len(approx_curve))
    # cv2.imshow("contours", img1)
    # cv2.waitKey(0)
    obj = len(approx_curve)
    x,y,w,h = cv2.boundingRect(approx_curve)
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,1),5)
    if obj ==3:
        obj_type = "Tri"
    elif obj == 4:
        aspect_ratio = w /float(h)
        if aspect_ratio > 0.98 and aspect_ratio < 1.03:
            obj_type = "Square"
        else:
            obj_type = "rectangle"
    elif obj > 4 :
        obj_type = "circle"

    cv2.putText(img1,obj_type,(x + (w//2) - 10, y + (h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

cv2.imshow('original',img)
cv2.imshow("output",new_img)
cv2.imshow("contours", img1)
cv2.waitKey(0)
