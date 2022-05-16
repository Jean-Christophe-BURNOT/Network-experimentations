#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:43:13 2022

@author: terramotu
This programm is a WIFI Scanner found on a book
"""
import network, ubinascii

wlan = network.WLAN(network.STA_IF)
wlan.active(True) #activation of the interface
resultat_scan = wlan.scan()
nb_points_acces = len(resultat_scan)
print("Nombre de points d'acces: ", nb_points_acces)
# %% display the result
print("SSID: ")
print("BSSID: ")
print("Canal de connexion: ")
print("RSSI: ")
print("mode 0:open 1:WEP 2:WPAPSK 3:WPA2PSK 4:WPA-WPA2-PSK")
print("Mode: ")
print("SSID visible(False) ou cache(True)")


