import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6 outputbase digits'

# camera = cv2.VideoCapture(0)
while True:
    
    img = cv2.imread('12_09_2023 15-17-17.jpg')
    # _,img=camera.read()
    # img = cv2.imread('test.png')
    
    #ROI Coordinates
    dustx1 = 780 
    dusty1 = 620
    dustx2 = 888
    dusty2 = 700
    
    cox1 = 796   
    coy1 = 682
    cox2 = 888
    coy2 = 743
    
    humx1 = 657   
    humy1 = 125
    humx2 = 805
    humy2 = 259
    
    tempx1 = 825   
    tempy1 = 120
    tempx2 = 942
    tempy2 = 198

    roi_dust = img[dusty1:dusty2,dustx1:dustx2]
    roi_co = img[coy1:coy2,cox1:cox2]
    roi_hum = img[humy1:humy2,humx1:humx2]
    roi_temp = img[tempy1:tempy2,tempx1:tempx2]

    dust = pytesseract.image_to_string(roi_dust, config=custom_config)
    co = pytesseract.image_to_string(roi_co, config=custom_config)
    hum = pytesseract.image_to_string(roi_hum, config=custom_config)
    temp = pytesseract.image_to_string(roi_temp, config=custom_config)
    
    # print('dust=',dust,'co=',co,'hum=',hum,'temp=',temp)
    
    # cv2.imshow('img',img)
    cv2.imshow('dust',roi_dust)
    cv2.imshow('co',roi_co)
    cv2.imshow('hum',roi_hum)
    cv2.imshow('imdg',roi_temp)
        
    if cv2.waitKey(1)& 0xff == 27:
        break
# camera.release()
cv2.destroyAllWindows()