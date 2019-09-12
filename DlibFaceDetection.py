# -*- coding: utf-8 -*-
"""
Created on Feb 15 17:00:05 2019

@author: omerfarukkoc
"""
import cv2
import sys
import dlib


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

HogFaceDetector = dlib.get_frontal_face_detector()

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

        FaceRects = HogFaceDetector(GrayFrame, 0)
        for FaceRect in FaceRects:
            x1 = FaceRect.left()
            y1 = FaceRect.top()
            x2 = FaceRect.right()
            y2 = FaceRect.bottom()
            cv2.rectangle(Frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

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



