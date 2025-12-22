# Auscultation-Points-Estimation

## Description

Auscultation, a crucial practice in medicine, plays a fundamental role in detecting cardiac and pulmonary signals, contributing to accurate diagnoses. 


<img width="660" height="267" alt="image" src="https://github.com/user-attachments/assets/fb46a166-12b2-4656-9cd8-f0cfa4fad422" />


However, the lack of organic teaching of auscultation and its inadequate practice have had a negative impact on the clinical competence of physicians in training, also reflecting a diminished academic interest. Consequently, auscultation has entered a phase of decline. 

In order to overcome this problem, this work proposed the estimation of cardiac and pulmonary auscultation points with the aid of OpenCV and MediaPipe. A Python application was developed that allows the estimation of auscultation points in three different modes: anterior and posterior pulmonary auscultation, and cardiac auscultation.

### OpenCV

An open-source computer vision library created by Intel in 1998, used for real-time image and video analysis. It consists of low-level image processing functions and high-level algorithms such as face and feature detection, pedestrian detection, and tracking.

### MediaPipe

An open-source framework created by Google in 2019 with the goal of providing machine learning (ML) solutions for applications under development that use cameras or audio to detect objects in real time.
It has several functions, including MediaPipe Pose, which allows obtaining estimates of 2D coordinates. It uses BlazePose, which extracts 33 reference points on the human body. This ML algorithm achieves high levels of performance on both mobile phones and computers.

<img width="1090" height="550" alt="image" src="https://github.com/user-attachments/assets/ec0e80e6-af27-43d7-a501-526a8b813539" />

### Mapping of Auscultation Points

The auscultation points were identified in relation to the reference points of the shoulders (11 and 12) and hips (23 and 24). Three different modes were developed: anterior and posterior pulmonary auscultation, and cardiac auscultation. The mapping of the auscultation points was performed based on posteroanterior (PA) or anteroposterior (AP) chest radiographs, as follows:

| Anterior lung auscultation on an AP radiograph  | Posterior lung auscultation on a PA radiograph | Cardiac auscultation on an AP radiograph |
| ------------- | ------------- | ------------- |
| <img width="361" height="399" alt="image" src="https://github.com/user-attachments/assets/ae5b65df-9971-414e-8390-4f86fa7b4ce6" /> | <img width="405" height="371" alt="image" src="https://github.com/user-attachments/assets/8e5cf7fa-be0e-4aff-8b56-252412201e1a" /> | <img width="360" height="400" alt="image" src="https://github.com/user-attachments/assets/4c0a514b-e193-4e59-9f28-4b1e0b5fa195" /> |

Next, we superimposed the MediaPipe reference points, drew lines between points 11 and 23 and between points 12 and 24 (shoulder and hip on each side), and drew horizontal lines to contain the auscultation points at the same height as follows:

<img width="514" height="473" alt="image" src="https://github.com/user-attachments/assets/d74d3d5c-bcb4-4792-b0a2-ddf43d2447d0" />

Proportions were calculated relative to the location of the horizontal lines and the points they contain, taking as reference the connections between points 11 and 12 and the connections between the shoulders and hips respectively, since these are part of the MediaPipe Pose.

- Taking as an example the second line and points L2 and R2, considering that the limits of the line are 1.2 cm from the shoulders and 2.2 cm from the points:

| Proportions |
| ---      |
| Prop.y2 = 1.2 / dy |
| Prop.x2 = 2.2 / dx2 |

- Considering in this body position the relationship dy1 = dy2 = 1.8 × dx1 obtained after testing the MediaPipe Pose model, with dx1 = 6.2 cm and dx2 = 5.7 cm:

| Proportions |
| ---      |
| Prop.y2 = 1.2 / (1.8 × 6.2) = 0.11 |
| Prop.x2 = 2.2 / 5.7 = 0.39 |

### Calculation of the Auscultation Points Coordinates

For the auscultation points to follow the movement of the MediaPipe Pose model, it was essential to establish a relationship with the reference points as discussed previously.

First, the linear equations (y = m.x + b) of the connections between the shoulders (P11 and P12) and hips (P23 and P24) on both sides were calculated:

| Linear Equations |
| ---      |
| mP11→P23 = (P23y – P11y) / (P23x – P11x) |
| bP11→P23 = P11y - mP11→P23 × P11x |
| mP12→P24 = (P24y – P12y) / (P24y – P12y) |
| bP12→P24 = P12y - mP12→P24 × P12x |

Next, horizontal lines containing the auscultation points were drawn, considering that the limits of these lines must belong to the previously established linear equations. Thus, using line 2 as an example, the coordinates were calculated as follows:

| Horizontal Lines Coordinates |
| ---      |
| LeftLimit.y2 = P11y + Prop.y2 × dy1 = P11y + 0.11 × dy1 |
| LeftLimit.x2 = (LimiteEsq.y2 - bP11→P23) / mP11→P23 |
| RightLimit.y2 = P12y + Prop.y2 × dy2 = P12y + 0.11 × dy2 |
| RightLimit.x2 = (RightLimit.y2 - bP12→P24) / mP12→P24 |

Finally, we placed the points on the lines considered previously, taking into account that they must belong to their line equations. After discovering the line equations of the lines, we calculated the coordinates of the points as observed in the following example of points L2 and R2:

| Auscultation Points Coordinates |
| ---      |
| L2x = LeftLimit.x2 + Prop.x2 × dx2 = LeftLimit.x2 + 0.39 × dx2 |
| L2y = mline2 × L2x + bline2 |
| R2x = RightLimit.x2 + Prop.x2 × dx2 = RightLimit.x2 - 0.39 × dx2 |
| R2y = mline2 × R2x + bline2 |

### Results

In order to create a sustainable, intuitive and accessible format for a healthcare professional or any other user, an interface was developed that allows each of the auscultation modes to be performed.

After the user selects the “START” button, the main menu is displayed where the user can choose each of the auscultation modes.

<img width="767" height="377" alt="image" src="https://github.com/user-attachments/assets/7c2ef497-7dd1-430e-8e5c-2ea9ee477580" />

Each button corresponds to an auscultation mode that the user can then select from the three available options (cardiac auscultation, anterior pulmonary auscultation, and posterior pulmonary auscultation), illustrated by images of the set of points to be estimated. By clicking on each of the information icons, it is possible to obtain information about the auscultation mode.

<img width="576" height="310" alt="image" src="https://github.com/user-attachments/assets/614a3cda-ab73-4685-8541-8f26b9d759ec" />

Following the program's flow, the user has the possibility, as explained previously, to select the auscultation mode, and the three scenarios that our program allows will then be presented. As can be seen next, in the three auscultation modes, the results obtained in the calculation of the auscultation points for the same patient are in accordance with what was proposed.

| Anterior lung auscultation | Posterior lung auscultation | Cardiac auscultation |
| ------------- | ------------- | ------------- |
| <img width="629" height="470" alt="image" src="https://github.com/user-attachments/assets/ca7af010-28e0-40db-8e23-921cb3d33f7e" /> | <img width="553" height="470" alt="image" src="https://github.com/user-attachments/assets/3935ea12-3236-40f1-afc2-b92cc8151101" /> | <img width="631" height="471" alt="image" src="https://github.com/user-attachments/assets/626b8084-9dbf-4aba-92b0-030ef529d194" /> |

