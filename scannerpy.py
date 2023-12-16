import cv2
from picamera2 import Picamera2
from pyzbar.pyzbar import decode
import numpy as np
import subprocess
import pickle
import json
from trigger_unlock import unlock_mechanism
from qrverify import verify_data
# set up camera object
# cap = cv2.VideoCapture(0, apiPreference=cv2.CAP_V4L2)

def get_qr_data(input_frame):
    try:
        return decode(input_frame)
    except:
        return []

def draw_polygon(f_in, qro):
    if len(qro) == 0:
        return f_in, None
    else:
        for obj in qro:
            text = obj.data.decode('utf-8')
            print("TEXT:",text)
            pts = np.array([obj.polygon], np.int32)
            # print("Before Reshape::", pts.shape)
            pts = pts.reshape((4, 1, 2))
            # print("After Reshape::",pts.shape)
            cv2.polylines(f_in, [pts], True, (255, 100, 5), 2)
            cv2.putText(f_in, text, (50, 50), cv2.FONT_HERSHEY_PLAIN,1.5,(255,100,5),2)
        return f_in, text
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format":"BGR888","size":(640,480)}))

picam2.start()
# QR code detection object
detector = cv2.QRCodeDetector()

while True:
    # get the image
    #_, img = cap.read()
    
    img = picam2.capture_array()
#     _, frame = cap.read()
    qr_obj = get_qr_data(img)
    frame, text = draw_polygon(img, qr_obj)
    cv2.imshow("DD", frame)
    
    if text:
        try:
            data = {"name": text}
            result_verify = verify_data(data)
            
            
            if result_verify:
                unlock_mechanism()
                print(f"data from verify: {result_verify}")
            else:
                print(f"Error: ")
            break
            
        except Exception as e:
            
            print("Quit error:", e)
            break
        
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
# free camera object and exit
cv2.destroyAllWindows()

