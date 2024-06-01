# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:12:17 2024

@author: Jakub
"""
# from random import randrange
# N = 4
# pole = [0,1,2,3,4,5,6,7,8,9]

# def funkcia(N,pole):
    
#     print(pole)
#     vystupnePole2 = []
#     for i in range (N):
#         vystupnePole = []
#         for j in range (N):
#             vystupnePole.append(randrange(10))
#         vystupnePole2.append(vystupnePole)
#     return(vystupnePole2)
# print(funkcia(N,pole))


# import cv2
# import numpy as np

# def display_image_with_overlays(image_path, num_overlays):
#     # Načítaj obrázok
#     image = cv2.imread(image_path)
    
#     # Nastav rozmery okna
#     window_size = (800, 800)
    
#     # Zmeň veľkosť pôvodného obrázka na rozmery okna
#     resized_image = cv2.resize(image, window_size)
    
#     # Vytvor prázdne plátno s bielym pozadím
#     canvas = np.ones((800, 800, 3), dtype=np.uint8) * 255
    
#     # Vlož veľký obrázok na plátno
#     canvas = resized_image.copy()
    
#     # Vytvor a vlož zmenšené verzie obrázka
#     for i in range(1, num_overlays + 1):
#         factor = 1 - i * 0.2  # faktor zmenšenia
#         small_size = (int(window_size[0] * factor), int(window_size[1] * factor))
#         small_image = cv2.resize(image, small_size)
        
#         # Vypočítaj pozíciu na vloženie obrázka
#         top_left_x = (window_size[0] - small_size[0]) // 2
#         top_left_y = (window_size[1] - small_size[1]) // 2
        
#         # Vlož zmenšený obrázok na plátno
#         canvas[top_left_y:top_left_y + small_size[1], top_left_x:top_left_x + small_size[0]] = small_image
    
#     # Vytvor okno a zobraz obrázok
#     cv2.imshow('Image Overlay', canvas)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Príklad použitia funkcie
# image_path = 'image.jpg'  # Zmeňte na cestu k vášmu obrázku
# num_overlays = 4  # Počet zmenšení
# display_image_with_overlays(image_path, num_overlays)

import cv2
image_path = 'image.jpg'
img = cv2.imread(image_path)
window_size = (800, 800)
resized_image = cv2.resize(img, window_size)
cv2.imshow("Obrazok", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()