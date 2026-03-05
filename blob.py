import cv2
import numpy as np

# Buka webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range warna merah
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Cari kontur
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500:
            x,y,w,h = cv2.boundingRect(cnt)

            # gambar kotak
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            # titik tengah
            cx = int(x + w/2)
            cy = int(y + h/2)

            cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()