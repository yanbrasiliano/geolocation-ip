""" 
File name: 	geolocat.py		                
Author:			Yan Brasiliano Silva Penalva	                       
Email: 			yanpenabr@gmail.com
---------------------------------------------------------------------
Date created:								17 MAR 21                   
Date last modified: 				17 MAR 21
Python Version: 						Above 3.6 
License: 										GNU License
Maintainer: 								Yan Brasiliano Silva Penalva
Version:										1.0
---------------------------------------------------------------------
Description: 
PT-BR
Este script recebe uma URL e retorna informações de sua localização e seu endereço IP.
EN-US
This script receives a URL and returns information about its location and its IP address. 
"""


import socket
from ip2geotools.databases.noncommercial import DbIpCity
from time import sleep


url = input('Insert a URL: ')
IP = socket.gethostbyname(url)
response = DbIpCity.get(IP,api_key='free')

print('Searching...') 
sleep(1)
print(f'Address IP: {IP}')
print(f'City: {response.city}')
print(f'Region: {response.region}')
print(f'Country: {response.country}')