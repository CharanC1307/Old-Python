import cv2

#Show Image
"""
img=cv2.imread("C:\Brothers\Charan\Python\Youtube\Murtaza's Workshop - Robotics and AI\Cv2\Image//crop.jpg")

cv2.imshow("Outside", img)

cv2.waitKey(0)
"""

#Show Video
"""
vid=cv2.VideoCapture("C:\Brothers\Charan\Python\Youtube\Murtaza's Workshop - Robotics and AI\Cv2\Video\WIN_20200602_17_53_57_Pro.mp4")

while True:
    success, img=vid.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
"""

#Show Webcam
"""
vid=cv2.VideoCapture(0)
#3 is for width
vid.set(3, 640)
#4 is for height
vid.set(4, 480)
#10 is for width
vid.set(10, 100)

while True:
    success, img=vid.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
"""