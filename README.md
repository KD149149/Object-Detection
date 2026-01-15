
# Real-Time Object Detection with World-Standard Categories

This project implements a **real-time object detection system** using a laptop camera.
It detects objects, classifies them into **globally accepted categories**, displays bounding boxes on live video, records the video with timestamps, and generates an **Excel report** for all detections.

---

## 1. Objective

* Capture live video from a laptop camera
* Detect objects in real time
* Classify detected objects using world-standard categories
* Display bounding boxes with category labels
* Save recorded video with date and time
* Generate an Excel report containing detection details

---

## 2. World-Standard Categories

The classification is aligned with the **COCO dataset standard**, which is widely used worldwide.

### Categories Used

| Category                | Objects Included                                                                |
| ----------------------- | ------------------------------------------------------------------------------- |
| Human                   | person                                                                          |
| Animal                  | bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe               |
| Vehicle                 | bicycle, car, motorcycle, airplane, bus, train, truck, boat                     |
| Nature / Environment    | potted plant, bench, fire hydrant, stop sign                                    |
| Object / Infrastructure | chair, couch, bed, dining table, laptop, keyboard, mouse, phone, TV, appliances |
| Food                    | apple, banana, sandwich, orange, pizza, cake, etc.                              |
| Other                   | Objects not covered above                                                       |

---

## 3. Technology Stack

* Python 3.8 or higher
* YOLOv8 (Ultralytics)
* OpenCV
* Pandas
* OpenPyXL

---

## 4. Installation Procedure

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Install Required Libraries

```bash
pip install ultralytics opencv-python pandas openpyxl
```

---

## 5. Execution Procedure

### Step 1: Run the Application

```bash
python main.py
```

### Step 2: Live Operation

* The laptop camera will start automatically
* Detected objects will be shown with green bounding boxes
* Each object will display its **category**

### Step 3: Stop Execution

* Press **Q** to stop the program safely

---

## 6. Output Generated

### Video Output

* Recorded video with bounding boxes
* Filename includes date and time

### Excel Report

* Automatically generated at program exit
* Contains structured detection logs

---

## 7. Output Folder Structure

```text
project-folder/
│
├── videos/
│   └── object_detection_YYYY-MM-DD_HH-MM-SS.mp4
│
├── reports/
│   └── object_report_YYYY-MM-DD_HH-MM-SS.xlsx
│
├── main.py
└── README.md
```

---

## 8. Excel Report Format

| Date       | Time     | Object | Category | Confidence |
| ---------- | -------- | ------ | -------- | ---------- |
| 2026-01-15 | 11:30:12 | person | Human    | 0.98       |
| 2026-01-15 | 11:30:18 | dog    | Animal   | 0.92       |
| 2026-01-15 | 11:30:25 | car    | Vehicle  | 0.89       |

---

## 9. Use Cases

* Smart surveillance systems
* Wildlife monitoring
* Traffic and vehicle analysis
* Campus and workplace safety
* AI and computer vision education

---

## 10. Limitations

* Nature detection is limited with general-purpose models
* Advanced detection (fire, water, forest, weapons) requires custom training
* Performance depends on camera quality and hardware

---

## 11. Future Scope

* Custom-trained models for environment detection
* Risk-based alerting system
* Separate videos per category
* Dashboard and analytics integration
* Cloud-based storage and reporting

---

## 12. License

This project is intended for **educational and research purposes**.
Review and update the license as required for commercial deployment.


