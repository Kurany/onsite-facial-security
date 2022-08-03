# add a face
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        name = input('Enter Name: ')
        out = cv2.imwrite('./known/' + str(name) + '.jpg', frame)
        if out is None:
            continue
        break

cap.release() 
cv2.destroyAllWindows()
