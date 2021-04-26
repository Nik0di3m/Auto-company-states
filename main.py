import requests
import shutil
from ftplib import FTP
from requests.api import request
from requests.auth import HTTPDigestAuth
from requests.models import HTTPBasicAuth
import wget
import os
from make import makeCSV
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sel import seleniumDownload
import login
import server
from vLookUp import vLookUp




def downloadCandelux():
    r = requests.get(server.candeluServer, stream=True)
    with open("Candelux.csv", "wb") as file:
        shutil.copyfileobj(r.raw, file)
    del r

def downloadEglo():
    filename = "stock_eglo_pl.csv"
    ftp = FTP(server.egloServer)
    ftp.login(login.egloUser, login.egloPassword)
    ftp.cwd('./')
    ftp.retrbinary("RETR " + filename, open("Eglo.csv", 'wb').write)
    ftp.quit()

def downloadHoldbox():
    filename = "puchacz.csv"
    ftp = FTP(server.holdBoxServer)
    ftp.login(login.holdBoxUser, login.holdBoxPassword)
    ftp.cwd("./")
    ftp.retrbinary("RETR " + filename, open("Holdbox.csv", 'wb').write)
    ftp.quit()


def downloadLampex():
    wget.download(server.lampexServer)
    os.rename(r'csv4', r'Lampex.csv')

def downloadLedea():
    r = requests.get(server.lampexServer, stream=True)
    with open("Ledea.csv", 'wb') as file:
        shutil.copyfileobj(r.raw, file)


def downloadLightPrestige():
    filename="lp_product_2.csv"
    ftp = FTP(server.lighPrestigeServer)
    ftp.login(login.lightPrestigeUser, login.lightPrestingePassword)
    ftp.cwd('./')
    ftp.retrbinary("RETR " + filename, open("LightPrestige.csv", 'wb').write)
    ftp.quit()

def downloadMwGlasberg():
    r = requests.get(server.mwGlasbergServer, stream=True)
    with open("Mw_glasberg.csv", 'wb') as file:
        shutil.copyfileobj(r.raw, file)

def downloadMaytoni():
    filename = "stock_maytoni.csv"
    ftp = FTP(server.maytoniServer)
    ftp.login(login.maytoniUser, login.maytoniPassword)
    ftp.cwd('./')
    ftp.retrbinary("RETR " + filename, open("Maytoni.csv", 'wb').write)
    ftp.quit()


def downloadRabalux():
    filename = 'webshop_stock.csv'
    ftp = FTP(server.rabaluxServer)
    ftp.login(login.rabaluxUser, login.rabaluxPassword)
    ftp.cwd('./')
    ftp.retrbinary("RETR " + filename, open("Rabalux.csv", 'wb').write)
    ftp.quit()

def downloadTkLight():
    wget.download(server.tkLightingServer)
    os.rename(r'listaplikow.CSV', r'TkLight.csv')

def downloadZumaLine():
    r = requests.get(server.zumaLineServer, stream=True)
    with open("ZumaLine.csv", 'wb') as file:
        shutil.copyfileobj(r.raw, file)


def makeDir():
    if os.path.isdir('pliki_csv'):
        print("Directory exist")
        os.chdir("pliki_csv")
    else:
        os.mkdir('pliki_csv')
        os.chdir('pliki_csv')
        pass

def skuDir():
    os.chdir("../")
    if os.path.isdir('pliki_sku'):
        print("Sku directory exist")
        os.chdir("pliki_sku")
    else:
        os.mkdir("pliki_sku")
        os.chdir("pliki_sku")

def exitSku():
    os.chdir("../pliki_csv/")
 
def main():
    
    makeDir()
    downloadCandelux()
    downloadEglo()
    skuDir()
    downloadHoldbox()
    exitSku()
    downloadLampex()
    downloadLedea()
    downloadLightPrestige()
    downloadMwGlasberg()
    skuDir()
    downloadMaytoni()
    exitSku()
    downloadRabalux()
    downloadTkLight()
    downloadZumaLine()
    seleniumDownload()
    # EkoLight i Italux ściąga się przez sellenium
    os.chdir('../')
    vLookUp()




if __name__ == "__main__":
    main()
    