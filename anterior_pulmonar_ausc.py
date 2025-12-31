# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:19:20 2023

@author: PC
"""

#CÓDIGO PARA AUSCULTAÇÃO PULMONAR ANTERIOR

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

# For webcam input:
cap = cv2.VideoCapture(0)
#cv2.namedWindow('MediaPipe Pose', cv2.)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            
            # Linha entre os pontos 11 e 23
            x11, y11 = int(results.pose_landmarks.landmark[11].x * image.shape[1]), int(results.pose_landmarks.landmark[11].y * image.shape[0])
            x23, y23 = int(results.pose_landmarks.landmark[23].x * image.shape[1]), int(results.pose_landmarks.landmark[23].y * image.shape[0])

            # Draw line between points 12 and 24
            x12, y12 = int(results.pose_landmarks.landmark[12].x * image.shape[1]), int(results.pose_landmarks.landmark[12].y * image.shape[0])
            x24, y24 = int(results.pose_landmarks.landmark[24].x * image.shape[1]), int(results.pose_landmarks.landmark[24].y * image.shape[0])
            
            
            # Função para calcular o comprimento da linha entre dois pontos
            def calcular_comprimento(ponto1, ponto2):
                return ((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2) ** 0.5
            
            # Calcula o comprimento total das linhas 11-23 e 12-24
            comprimento_linha_11_23 = calcular_comprimento((x11, y11), (x23, y23))
            comprimento_linha_12_24 = calcular_comprimento((x12, y12), (x24, y24))
            
            
            # Função para calcular a equação da reta dado dois pontos
            def calcular_reta(ponto1, ponto2):
                if ponto1[0] != ponto2[0]:
                    m = (ponto2[1] - ponto1[1]) / (ponto2[0] - ponto1[0])
                    b = ponto1[1] - m * ponto1[0]
                else:
                    m = float('inf')
                    b = ponto1[1]
                return m, b
            
            # Calcula a equação da reta entre os pontos 11 e 23
            m_11_23, b_11_23 = calcular_reta((x11, y11), (x23, y23))
            
            # Calcula a equação da reta entre os pontos 12 e 24
            m_12_24, b_12_24 = calcular_reta((x12, y12), (x24, y24))
            
            
            # COORDENADAS DOS PONTOS LIMITE DAS LINHAS HORIZONTAIS
            # Calcular as coordenadas y para os pontos nas linhas horizontais
            y_linha1_11_23 = y11 - 0.04 * comprimento_linha_11_23
            y_linha1_12_24 = y12 - 0.04 * comprimento_linha_12_24
            
            y_linha2_11_23 = y11 + 0.11 * comprimento_linha_11_23
            y_linha2_12_24 = y12 + 0.11 * comprimento_linha_12_24
            
            y_linha3_11_23 = y11 + 0.23 * comprimento_linha_11_23
            y_linha3_12_24 = y12 + 0.23 * comprimento_linha_12_24
            
            y_linha4_11_23 = y11 + 0.31 * comprimento_linha_11_23
            y_linha4_12_24 = y12 + 0.31 * comprimento_linha_12_24
            
            
            # Calcular as coordenadas x para os pontos limite das linhas horizontais
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
            
            
            # # LINHAS E MEDIAPIPE POSE(pôr em comentário para aparecerem só os pontos)
            
            # # Desenhar as linhas entre 11 e 23 e entre 12 e 24
            # cv2.line(image, (x11, y11), (x23, y23), color=(0, 255, 0), thickness=2)
            # cv2.line(image, (x12, y12), (x24, y24), color=(0, 255, 0), thickness=2)
            
            # # Desenhar as linhas que conectam os pontos de auscultação
            # cv2.line(image, (int(x_linha1_11_23), int(y_linha1_11_23)),
            #           (int(x_linha1_12_24), int(y_linha1_12_24)), color=(0, 0, 255), thickness=2)
            # cv2.line(image, (int(x_linha2_11_23), int(y_linha2_11_23)),
            #           (int(x_linha2_12_24), int(y_linha2_12_24)), color=(0, 0, 255), thickness=2)
            # cv2.line(image, (int(x_linha3_11_23), int(y_linha3_11_23)),
            #           (int(x_linha3_12_24), int(y_linha3_12_24)), color=(0, 0, 255), thickness=2)
            # cv2.line(image, (int(x_linha4_11_23), int(y_linha4_11_23)),
            #           (int(x_linha4_12_24), int(y_linha4_12_24)), color=(0, 0, 255), thickness=2)
            
            # # Desenhar a POSE
            # mp_drawing.draw_landmarks(
            #     image,
            #     results.pose_landmarks,
            #     mp_pose.POSE_CONNECTIONS)
            
            
            def desenhar_pontos(image, x1, y1, x2, y2, proporcao):
                # Calcular o declive m
                if x1 != x2:
                    m = (y1 - y2) / (x1 - x2)
                else:
                    m = float('inf')  # Atribui um valor grande para m se y1 for igual a y2
            
                # Calcular as coordenadas x para os pontos na linha
                x_L = x1 + proporcao * (x2 - x1)
                x_R = x2 - proporcao * (x2 - x1)
            
                # Calcular a ordenada na origem b e as coordenadas y para os pontos na linha
                if m != float('inf'):
                    b = y1 - m * x1
                    y_L = m * x_L + b
                    y_R = m * x_R + b
                else:
                    b = y1
                    y_L = b
                    y_R = b
            
                # Desenhar os pontos na linha
                cv2.circle(image, (int(x_L), int(y_L)), radius=6, color=(255, 0, 0), thickness=-1)
                cv2.circle(image, (int(x_R), int(y_R)), radius=6, color=(255, 0, 0), thickness=-1)
            
            desenhar_pontos(image, x_linha1_11_23, y_linha1_11_23, x_linha1_12_24, y_linha1_12_24,0.38)
            desenhar_pontos(image, x_linha2_11_23, y_linha2_11_23, x_linha2_12_24, y_linha2_12_24,0.29)
            desenhar_pontos(image, x_linha3_11_23, y_linha3_11_23, x_linha3_12_24, y_linha3_12_24,0.22)
            desenhar_pontos(image, x_linha4_11_23, y_linha4_11_23, x_linha4_12_24, y_linha4_12_24,0.08)
            
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            

        # Mostrar Imagem
        cv2.imshow('Posterior Pulmonary Auscultation', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
