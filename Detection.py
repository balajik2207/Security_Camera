import cv2
import twilio
import datetime

print("start")

import cv2
from twilio.rest import Client
from datetime import datetime

# Twilio credentials
account_sid = 'AC9708938c1d9c5b564ce35241d1e5b1e1'
auth_token = 'ae89783d2d51e56d3cd9f3cf7a5a06b7'
twilio_phone_number = '+18572148208'
user_mobile_number = '+918220710738'  

human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')


cap = cv2.VideoCapture('http://192.0.0.4:8080/video')


client = Client(account_sid, auth_token)

while True:
    
    ret, frame = cap.read()

    
    resized = cv2.resize(frame, (600, 400))

    
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    
    for (x, y, w, h) in humans:
        cv2.rectangle(resized, (x, y), (x + w, y + h), (255, 0, 0), 2)

        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

       
        message = client.messages.create(
            body=f"Human detected at {current_time}! Your area may be in danger.",
            from_=twilio_phone_number,
            to=user_mobile_number
        )

        print(f"Alert message sent to {user_mobile_number}, SID: {message.sid}")

    
    cv2.imshow("Human Detection", resized)

    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()