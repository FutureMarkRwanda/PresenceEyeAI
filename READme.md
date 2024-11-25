# PresenceEye AI Model
## 1. Introduction
   Purpose:
   PresenceEye is an AI-powered solution designed to detect human presence in indoor spaces. The core model, **[BEST](Models/best_v0.pt)**, is built on the YOLOv8 architecture and is currently trained to detect human presence, but due to limited data, it incorrectly classifies everyone as being in the "sitting" position. This is a result of training on a dataset where the model has only been exposed to the sitting activity, and thus, it fails to differentiate between sitting, standing,basic gestures or walking.

While this limitation persists, the model's overall goal is to automate device control based on human activity. The future plan is to expand the model's ability to detect a range of activities (sitting, standing, walking) by introducing more varied data in upcoming training sessions. This will enable smarter automation for devices such as lights and heating systems based on accurate human activity detection.

Weekly Evaluation Plan:
The development of the model progresses weekly, with continuous additions of new data to improve performance. Each week, the model is trained and evaluated, focusing on correcting its current over-simplification (i.e., detecting only sitting). Key performance metrics such as training loss and validation mAP are tracked, and the model's performance is reviewed to identify areas for improvement. This process ensures the steady progression of the PresenceEye AI model towards more accurate activity detection.

## 2. Current Version Details
###   Version: Pe 0.0 [Week 0](Documentation/Week_1_Report.md)
   The **PresenceEye AI model** (Week 1) is based on the YOLOv8 architecture and is currently limited to detecting the human activity of sitting, due to a training dataset that only included sitting. Because of this, the model incorrectly identifies every human it detects as sitting. This is a known issue, and we plan to address it in the coming weeks by expanding the dataset to include a wider variety of human activities (e.g., standing, walking).

#### Key Details for Current Version:

- **Model Type**: YOLOv8-based object detection model.
- **Core Functionality**: Detects human presence, but currently misclassifies all detected humans as sitting.
- **Training Process**: The model has been trained on a dataset with only the sitting activity. In future versions, a more diverse dataset will be used to train the model to accurately detect different human activities.
## Current Performance Metrics:
### Average Training Loss: 3.4530
### Average Validation mAP50(B): 0.7595
These metrics reflect the performance of the best.pt model, which is currently overfitting to detect sitting only. The next steps will involve training with a more varied dataset to prevent confusion and improve the model's accuracy in distinguishing different human activities.

For more details regarding the ongoing progress of the model, please refer to the 
[current version](Documentation/Week_1_Report.md).

