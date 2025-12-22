# Auscultation-Points-Estimation

## Description

Auscultation, a crucial practice in medicine, plays a fundamental role in detecting cardiac and pulmonary signals, contributing to accurate diagnoses. 


<img width="660" height="267" alt="image" src="https://github.com/user-attachments/assets/fb46a166-12b2-4656-9cd8-f0cfa4fad422" />


However, the lack of organic teaching of auscultation and its inadequate practice have had a negative impact on the clinical competence of physicians in training, also reflecting a diminished academic interest. Consequently, auscultation has entered a phase of decline. 

In order to overcome this problem, this work proposed the estimation of cardiac and pulmonary auscultation points with the aid of OpenCV and MediaPipe. A Python application was developed that allows the estimation of auscultation points in three different modes: anterior and posterior pulmonary auscultation, and cardiac auscultation.

## OpenCV

An open-source computer vision library created by Intel in 1998, used for real-time image and video analysis. It consists of low-level image processing functions and high-level algorithms such as face and feature detection, pedestrian detection, and tracking.

## MediaPipe

An open-source framework created by Google in 2019 with the goal of providing machine learning (ML) solutions for applications under development that use cameras or audio to detect objects in real time.
It has several functions, including MediaPipe Pose, which allows obtaining estimates of 2D coordinates. It uses BlazePose, which extracts 33 reference points on the human body. This ML algorithm achieves high levels of performance on both mobile phones and computers.

<img width="1090" height="550" alt="image" src="https://github.com/user-attachments/assets/ec0e80e6-af27-43d7-a501-526a8b813539" />

## Mapping of Auscultation Points

The auscultation points were identified in relation to the reference points of the shoulders (11 and 12) and hips (23 and 24). Three different modes were developed: anterior and posterior pulmonary auscultation, and cardiac auscultation. The mapping of the auscultation points was performed based on posteroanterior (PA) or anteroposterior (AP) chest radiographs, as follows:

| First Header  | Second Header | Third Header |
| ------------- | ------------- | ------------- |
| Content Cell  | Content Cell  | Content Cell  |


