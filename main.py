import cv2
from ultralytics import YOLO

# Load a YOLOv8 model (pre-trained)
model = YOLO('yolov8n.pt')  # You can also use other models like 'yolov8s.pt' or custom trained models

# Open the webcam (use the appropriate camera index)
cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Check if both cameras opened successfully
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open one or both video captures.")
    exit()

# Set video frame width and height for both cameras
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Loop to continuously get frames from both cameras
while True:
    # Capture frame-by-frame from both cameras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("Error: Failed to capture frame from one or both cameras.")
        break

    # Perform object detection on both frames
    results1 = model(frame1)
    results2 = model(frame2)

    # Draw the bounding boxes and labels on both frames
    annotated_frame1 = results1[0].plot()
    annotated_frame2 = results2[0].plot()

    # Display the resulting frames
    cv2.imshow('YOLOv8 Camera 1', annotated_frame1)
    cv2.imshow('YOLOv8 Camera 2', annotated_frame2)

    # Check if the window is open and being displayed
    if (cv2.getWindowProperty('YOLOv8 Camera 1', cv2.WND_PROP_VISIBLE) < 1 or
            cv2.getWindowProperty('YOLOv8 Camera 2', cv2.WND_PROP_VISIBLE) < 1):
        break

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release both captures
cap1.release()
cap2.release()
cv2.destroyAllWindows()