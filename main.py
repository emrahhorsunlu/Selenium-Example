# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:11:02 2024

@author: emrah
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from login_python import Ui_MainWindow # GELECEK OLAN UI'I buradan algılıyor test.py'den

class main (QMainWindow):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    

    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)
        self.qtTasarim.pushButton_Connect.clicked.connect(self.RunSite) #Butonların tıklamaları burada tanımlanıyor hangi methodu çağıracağı.
        
        

    def RunSite(self):
        
        url = self.qtTasarim.lineEdit_Url.text()
        userTime = self.qtTasarim.lineEdit_time.text()
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(30)
        userId = "test"
        password = "test"
        driver.find_element(By.CSS_SELECTOR, '[class="btn grey-gallery"]').click()
        #driver.find_element(By.CSS_SELECTOR, '[id="textKulID"]').send_keys(userId)
        #driver.find_element(By.CSS_SELECTOR, '[id="textSifre"]').send_keys(password)
        print('Timer Started at : ', datetime.datetime.now())
        time.sleep(10)
        print('Timer Finished at : ', datetime.datetime.now())
        
        time.sleep(int(userTime))
        driver.close()
        
        
app = QApplication([])
pencere = main()
pencere.show()
app.exec_()





