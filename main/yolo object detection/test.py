import cv2
from ultralytics import YOLO
import time

# Load YOLOv8 Model
model = YOLO("best.pt")  

cap = cv2.VideoCapture(0)  

prev_time = time.time()

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
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    
                elif class_name == 'elephant':
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                elif class_name == 'fox':
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                
                elif class_name == 'lion':
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    
                elif class_name == 'person':
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    
                elif class_name == 'tiger':
                    cv2.rectangle(annotated_frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                    cv2.putText(annotated_frame, f"{class_name} {confidence:.2f}", 
                                (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                 
 
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


cap.release()
cv2.destroyAllWindows()

