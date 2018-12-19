#Virus Total and Hybrid Analysis REST API Query
#Imports are added as I chug along.

import requests
import time
import os 
from consolemenu import *
from consolemenu.items import * 
from OTXv2 import OTXv2
import argparse


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
menu = ConsoleMenu("Threat Intelligence Application", "Main Menu")
menu_Item_1 = MenuItem("IP address Search")

#Creating the specific fucntion
function_item_1 = FunctionItem("Looking up all information available about this IP")

#Checking the domain for relevent information 
menu_Item_2 = MenuItem("Domain Research")

#Creating the second fuction
function_item_2 = FunctionItem("Domain Search")

menu.append_item(menu_Item_1)
menu.append_item(function_item_1)
menu.append_item(menu_Item_2)
menu.append_item(function_item_2)

menu.show()

def IP_Lookup():

