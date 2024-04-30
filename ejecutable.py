from cx_Freeze import setup, Executable
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from time import sleep
from datetime import datetime
import tkinter as tk
from tkinter import *

setup( name = "Simplex",
           version = "1.0" ,
           options = {'build_exe': {'packages':['tkinter','selenium-wire','selenium','datetime','json','time','sympy'],'include_files':['logo.ico']}},
           description = "Resolver" ,
           executables = [Executable("webdriver.py")] , )