# -*- coding: utf-8 -*-
"""
Created on Feb 15 17:00:05 2019

@author: omerfarukkoc
"""
import cv2
import sys
import dlib
from imutils import face_utils


Cam = cv2.VideoCapture(0)
# Cam.set(3, 2464)
# Cam.set(4, 2056)

ResizeWidth = 1024
ResizeHeight = 768

if Cam.isOpened() == True:
    print('\nKamera Açıldı')
    # print("-Özellikler-\nW: ", CamWidth, "\nH: ", CamHeight, "\nFPS: ", CamFps, "\n")
else:
    print('\nHATA!! \nKamera Açılamadı!!')
    exit(1)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    Ret, Frame = Cam.read()
    Frame = cv2.resize(Frame, (ResizeWidth, ResizeHeight), interpolation=cv2.INTER_LINEAR)
    try:
        if Ret != True:
            print('\nHATA!! Kameradan Frame Alınamıyor \nUygulamayı Yeniden Başlatın')
            cv2.destroyAllWindows()
            Cam.release()
            break
            exit(1)
        GrayFrame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

        rects = detector(GrayFrame, 0)

        for (i, rect) in enumerate(rects):
            shape = predictor(GrayFrame, rect)
            shape = face_utils.shape_to_np(shape)

            for (x, y) in shape:
                cv2.circle(Frame, (x, y), 2, (255, 0, 0), -1)

                # cv2.line(Frame, (x-20,y-20), (x+20,y+20),(255,0,0),5)

        cv2.imshow("Frame", Frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            print("Çıkış Yapıldı")
            Cam.release()
            cv2.destroyAllWindows()
            break
    except:
        print("\nBeklenmedik Hata!!! ", sys.exc_info()[0])
        raise

Cam.release()
cv2.destroyAllWindows()