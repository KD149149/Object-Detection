
import cv2
import pandas as pd
from ultralytics import YOLO
from datetime import datetime
import os

# ===================== INITIALIZATION =====================
model = YOLO("yolov8n.pt")  # Fast & lightweight

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

os.makedirs("videos", exist_ok=True)
os.makedirs("reports", exist_ok=True)

video_path = f"videos/object_detection_{timestamp}.mp4"
excel_path = f"reports/object_report_{timestamp}.xlsx"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

log_data = []

# ===================== WORLD-STANDARD CATEGORY MAP =====================
HUMAN = ["person"]

ANIMALS = [
    "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe"
]

VEHICLES = [
    "bicycle", "car", "motorcycle", "airplane",
    "bus", "train", "truck", "boat"
]

NATURE = [
    "potted plant", "bench", "fire hydrant", "stop sign"
]

OBJECTS = [
    "chair", "couch", "bed", "dining table",
    "laptop", "mouse", "keyboard", "cell phone",
    "tv", "refrigerator", "microwave", "oven"
]

FOOD = [
    "banana", "apple", "sandwich", "orange",
    "broccoli", "carrot", "pizza", "donut", "cake"
]

def get_category(label):
    if label in HUMAN:
        return "Human"
    elif label in ANIMALS:
        return "Animal"
    elif label in VEHICLES:
        return "Vehicle"
    elif label in NATURE:
        return "Nature / Environment"
    elif label in OBJECTS:
        return "Object / Infrastructure"
    elif label in FOOD:
        return "Food"
    else:
        return "Other"

# ===================== REAL-TIME DETECTION =====================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            label = model.names[cls_id]

            category = get_category(label)

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Green bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"{category}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            # Log data
            log_data.append({
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Object": label,
                "Category": category,
                "Confidence": round(confidence, 2)
            })

    out.write(frame)
    cv2.imshow("World-Standard Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ===================== CLEANUP =====================
cap.release()
out.release()
cv2.destroyAllWindows()

# ===================== EXCEL REPORT =====================
df = pd.DataFrame(log_data)
df.to_excel(excel_path, index=False)

print("✅ Detection completed successfully")
print("📹 Video saved:", video_path)
print("📊 Excel report saved:", excel_path)
