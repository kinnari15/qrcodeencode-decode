import qrcode
import cv2

data = "https://medium.com/p/c482e281bf1b"
text = "Hey!astronomy is the best"
#encoding the data
img = qrcode.make(data)
img1 = qrcode.make(text)
print(type(img))

img.save("mediumblog.jpg")
img1.save("random.jpg")

#decoding the image  

detector = cv2.QRCodeDetector()
val, points, straight_qrcode = detector.detectAndDecode(cv2.imread("random.jpg"))
print(val)