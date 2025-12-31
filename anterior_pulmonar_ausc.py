# -*- coding: utf-8 -*-

#CODE FOR ANTERIOR PULMONAR AUSCULTATION

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def add_landmark(results, name, coordinates):
    landmark = results.pose_landmarks.landmark.add()
    landmark.x = coordinates[0]
    landmark.y = coordinates[1]
    landmark.z = coordinates[2]
    landmark.visibility = 1.0

cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            
            x11, y11 = int(results.pose_landmarks.landmark[11].x * image.shape[1]), int(results.pose_landmarks.landmark[11].y * image.shape[0])
            x23, y23 = int(results.pose_landmarks.landmark[23].x * image.shape[1]), int(results.pose_landmarks.landmark[23].y * image.shape[0])

            x12, y12 = int(results.pose_landmarks.landmark[12].x * image.shape[1]), int(results.pose_landmarks.landmark[12].y * image.shape[0])
            x24, y24 = int(results.pose_landmarks.landmark[24].x * image.shape[1]), int(results.pose_landmarks.landmark[24].y * image.shape[0])
            
            def calcular_comprimento(ponto1, ponto2):
                return ((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2) ** 0.5
            
            comprimento_linha_11_23 = calcular_comprimento((x11, y11), (x23, y23))
            comprimento_linha_12_24 = calcular_comprimento((x12, y12), (x24, y24))
            
            def calcular_reta(ponto1, ponto2):
                if ponto1[0] != ponto2[0]:
                    m = (ponto2[1] - ponto1[1]) / (ponto2[0] - ponto1[0])
                    b = ponto1[1] - m * ponto1[0]
                else:
                    m = float('inf')
                    b = ponto1[1]
                return m, b
            
            m_11_23, b_11_23 = calcular_reta((x11, y11), (x23, y23))
            
            m_12_24, b_12_24 = calcular_reta((x12, y12), (x24, y24))
            
            y_linha1_11_23 = y11 - 0.04 * comprimento_linha_11_23
            y_linha1_12_24 = y12 - 0.04 * comprimento_linha_12_24
            
            y_linha2_11_23 = y11 + 0.11 * comprimento_linha_11_23
            y_linha2_12_24 = y12 + 0.11 * comprimento_linha_12_24
            
            y_linha3_11_23 = y11 + 0.23 * comprimento_linha_11_23
            y_linha3_12_24 = y12 + 0.23 * comprimento_linha_12_24
            
            y_linha4_11_23 = y11 + 0.31 * comprimento_linha_11_23
            y_linha4_12_24 = y12 + 0.31 * comprimento_linha_12_24
            
            def calcular_coordenadas_x(y, m, b):
                if m != float('inf'):
                    x = (y - b) / m
                else:
                    x = y - b
                return x
            
            x_linha1_11_23 = calcular_coordenadas_x(y_linha1_11_23, m_11_23, b_11_23)
            x_linha1_12_24 = calcular_coordenadas_x(y_linha1_12_24, m_12_24, b_12_24)
            
            x_linha2_11_23 = calcular_coordenadas_x(y_linha2_11_23, m_11_23, b_11_23)
            x_linha2_12_24 = calcular_coordenadas_x(y_linha2_12_24, m_12_24, b_12_24)
            
            x_linha3_11_23 = calcular_coordenadas_x(y_linha3_11_23, m_11_23, b_11_23)
            x_linha3_12_24 = calcular_coordenadas_x(y_linha3_12_24, m_12_24, b_12_24)
            
            x_linha4_11_23 = calcular_coordenadas_x(y_linha4_11_23, m_11_23, b_11_23)
            x_linha4_12_24 = calcular_coordenadas_x(y_linha4_12_24, m_12_24, b_12_24)
            
            
            def desenhar_pontos(image, x1, y1, x2, y2, proporcao):
                if x1 != x2:
                    m = (y1 - y2) / (x1 - x2)
                else:
                    m = float('inf')
            
                x_L = x1 + proporcao * (x2 - x1)
                x_R = x2 - proporcao * (x2 - x1)
            
                if m != float('inf'):
                    b = y1 - m * x1
                    y_L = m * x_L + b
                    y_R = m * x_R + b
                else:
                    b = y1
                    y_L = b
                    y_R = b
            
                cv2.circle(image, (int(x_L), int(y_L)), radius=6, color=(255, 0, 0), thickness=-1)
                cv2.circle(image, (int(x_R), int(y_R)), radius=6, color=(255, 0, 0), thickness=-1)
            
            desenhar_pontos(image, x_linha1_11_23, y_linha1_11_23, x_linha1_12_24, y_linha1_12_24,0.38)
            desenhar_pontos(image, x_linha2_11_23, y_linha2_11_23, x_linha2_12_24, y_linha2_12_24,0.29)
            desenhar_pontos(image, x_linha3_11_23, y_linha3_11_23, x_linha3_12_24, y_linha3_12_24,0.22)
            desenhar_pontos(image, x_linha4_11_23, y_linha4_11_23, x_linha4_12_24, y_linha4_12_24,0.08)
            
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
        cv2.imshow('Posterior Pulmonary Auscultation', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
