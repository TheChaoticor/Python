import cv2 as cv

# Use an absolute path or properly formatted relative path
# Example: absolute path
# img = cv.imread('C:/Users/HP/Desktop/Python/OpenCv Projects(Computer Vision)/images/images.jpg')

# Example: relative path with corrected slashes
img = cv.imread('OpenCv Projects(Computer Vision)/images/images.jpg')

# Check if the image was successfully loaded


    

def rescaleframe(frame,scale=0.20):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)  
   
capture=cv.VideoCapture('OpenCv Projects(Computer Vision)/videos/856309-hd_1920_1080_30fps.mp4')
while True:
   
    istrue,frame=capture.read()
    rescalef=rescaleframe(frame,0.20)
    cv.imshow('space',rescalef)
    if cv.waitKey(3400) or 0xff==ord('d'):
        break