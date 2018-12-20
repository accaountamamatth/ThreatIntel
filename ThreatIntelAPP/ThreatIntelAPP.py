#Virus Total and Hybrid Analysis REST API Query
#Imports are added as I chug along.

import requests
import time
import os 
from consolemenu import *
from consolemenu.items import * 
from OTXv2 import OTXv2
import argparse
import socket


#Super Bone simple CLI interface. The point is to get data.

#Global Variables 
Hybrid_Key = input(" Please enter your Hybrid Analysis Key: ")
Hybrid_Key_Secret = input("And the secret if you will: ")
VT_Key = input(" Please enter your Virus Total Key: ")

#And something useless because people will complain without it
OTX_Key = input("Please enter your OTX Key")

#Now I will create the menue to use. This should be farily simple and easy to expand upon

#Create menu
#Creates the header menu
def Main_Menu():
    print(30 * "-", "Threat Intel API" , 30 * "-")
    print("1. IP address Lookup")
    print("2. Domain Lookup")
    print("3. API Key Change")
    print("4. Exit")
loop = True

while loop:
    Main_Menu()
    choice = input("Select a choice [1-4]: ")

    if choice == 1:
        def IP_Lookup():
            print("IP Lookup")


    if choice == 2:
        def Domain_Lookup():
            print("Domain Lookup: ")
            
            domain1 = input("Please enter the domain to search. This will take a while: ")
            rsv_domain = socket.gethostbyname(domain1)
            print(rsv_domain)

            #VT Domain Scanner
            url = 'https://www.virustotal/vtapi/v2/url/scan'
            params = {'apikey': VT_Key, 'url': domain1}

            try:
                r = requests.post(url, params=params)
            except requests.ConnectTimeout as timeout:
                print()

        domain_Lookup()

    if choice == 3:
        def API_Key_Change():
            print("Please enter your API Keys for the following Intel Sources: ")
            Hybrid_Key = input("Please enter your Hybrid Analysis Key: ")
            Hybrid_Key_Secret = input("Please enter your new Hybrid Analysis Secret: ")
            OTX_Key = input("Please enter your new OTX key: ")
            VT_Key = input("Please enter your new VT key: ")



    

