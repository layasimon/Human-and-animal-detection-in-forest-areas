import cv2
from ultralytics import YOLO
import time
import serial

ser = serial.Serial('COM4', 9600)
ser.timeout = 1

# Load YOLOv8 Model
model = YOLO("best.pt")  

cap = cv2.VideoCapture(0)  

prev_time = time.time()
p=0
e=0
l=0
f=0
t=0
b=0
while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model(frame)  # Run YOLO inference

        annotated_frame = frame.copy()
        valid_detection = False  

        for box in results[0].boxes:
            confidence = float(box.conf)  
            if confidence > 0.75:
                valid_detection = True
                x0, y0, x1, y1 = map(int, box.xyxy[0])  
                label = int(box.cls)  
                
          
                class_name = model.names.get(label, f"Class {label}")  

                if class_name == 'bear':
                    b+=1
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    if b==20:
                        ser.write(b"b#")
                        b=0
                elif class_name == 'elephant':
                    e+=1
                    if e==20:
                        cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                        cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                    (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                        ser.write(b"e#")
                        e=0
                elif class_name == 'fox':
                    f+=1
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    if f==20:
                        f=0
                        ser.write(b"f#")
                    
                elif class_name == 'lion':
                    l+=1
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    if l==20:
                        ser.write(b"l#")
                        l=0
                    
                elif class_name == 'person':
                    p+=1
                    
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    if p == 50:
                        ser.write(b"h#")
                        p=0
                    
                elif class_name == 'tiger':
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    ser.write(b"t#")
 
        current_time = time.time()
        fps = min(30, 1 / (current_time - prev_time))  
        prev_time = current_time

        cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

 
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break  

ser.close()
cap.release()
cv2.destroyAllWindows()

