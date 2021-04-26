import time
from numpy.core.numeric import _mode_from_name
from numpy.lib.ufunclike import fix
import pandas as pd
from pandas.core.algorithms import mode
from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv
import csv
import os
from datetime import date


def addEglo(date):
    df = pd.read_csv("./pliki_csv/Eglo.csv", sep=";", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df["EAN"], "qty": df["Qty"]}
    #df.to_csv('test.csv', 'a', columns=['EAN'], encoding="UTF-8")
    df = pd.DataFrame(dict)
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", index=False, header=['Nr_katalogowy', "Ilosc_produktow"], sep=";", mode="a")

def addCandelux(date):
    df = pd.read_csv("./pliki_csv/Candelux.csv", sep=";", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df["EAN"], "qty": df["Stan_magazynowy"]}
    df = pd.DataFrame(dict)
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", index=False, sep=";", mode="a", header=False)

def addHoldBox():
    df = pd.read_csv("./pliki_csv/Holdbox.csv")

def addItalux(date):
    df = pd.read_csv("./pliki_csv/Italux_dostepnosci.csv", sep=",", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df['EAN'], 'qty':df['Stan magazynowy']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df['qty'] = df['qty'].str.replace(',00','')
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", index=False, sep=";", mode="a", header=False)

def addLampex(date):
    df = pd.read_csv("./pliki_csv/Lampex.csv", sep=";", skip_blank_lines=True, encoding="utf-8", skipinitialspace=True)
    dict = {'Nr_katalogowy': df["EAN"], 'qty': df["Dostępność"]}
    df = pd.DataFrame(dict)
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", index=False, sep=";", mode="a", header=False)

def addLedea(date):
    df = pd.read_csv("./pliki_csv/Ledea.csv", sep=";", skip_blank_lines=True, encoding="utf-8", skipinitialspace=True)
    dict = {'Nr_katalogowy': df['EAN'], 'qty': df['Dostępność']}
    df = pd.DataFrame(dict)
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", index=False, sep=";", mode='a', header=False)

def addLightPrestige(date):
    df = pd.read_csv("./pliki_csv/LightPrestige.csv", sep=";", skip_blank_lines=True, skipinitialspace=True, encoding="utf-8")
    dict = {'Nr_katalogowy': df['Ean'], 'qty': df['Stan_mag']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", sep=";", mode="a", index=False, header=False)

def addMwGlasberg(date):
    df = pd.read_csv("./pliki_csv/Mw_glasberg.csv", sep=",", skip_blank_lines=True, encoding="utf-8", skipinitialspace=True)
    dict = {'Nr_katalogowy': df['ean'], 'qty': df['Qty']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", index=False, mode="a", sep=";", header=False)

def addMaytoni():
    pass

def checkEkoLight():
    
    for file in os.listdir('./pliki_csv'):
        if file.startswith("produkty_"):
            print(file)
            return file

def addEkoLight(file, date):
    df = pd.read_csv("./pliki_csv/" + file, encoding='utf-8', sep=";", skip_blank_lines=True, skipinitialspace=True)
    dict = {"Nr_katalogowy": df['ean'], "qty": df['qty']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df['qty'] = df['qty'].astype(str).str.replace('.0','',regex=True)
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", index=False, mode="a", sep=";", header=False)


def addRabalux(date):
    df = pd.read_csv("./pliki_csv/Rabalux.csv", encoding="utf-8", sep=";", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df['EAN code'], 'qty': df['availability']}
    df = DataFrame(dict)
    df['qty'] = df['qty'].str.replace('available','20')
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", sep=";", index=False, mode="a", header=False)


def addTkLighting():
    with open("./pliki_csv/TkLight.csv", 'w', encoding='unicode') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    
def addZumaLine(date):
    df = pd.read_csv("./pliki_csv/ZumaLine.csv", encoding="utf-8", sep=";", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df["ean"], 'qty':df['stan magazynowy']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", sep=";", index=False, mode="a", header=False)

def addHoldBox(date):
    df = pd.read_csv("./pliki_csv/HoldBox.csv", encoding="utf-8", sep=";", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df["Nr_katalogowy"], 'qty':df['Qty']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", sep=";", index=False, mode="a", header=False)

def addMaytoni(date):
    df = pd.read_csv("./pliki_csv/Maytoni.csv", encoding="utf-8", sep=";", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df["Nr_katalogowy"], 'qty':df['Qty']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df = df.dropna()
    df.to_csv("tmp/Stany_Kaja" + date +".csv", encoding="utf-8", sep=";", index=False, mode="a", header=False)


def fixCSV(date):
    df = pd.read_csv("tmp/Stany_Kaja" + date + ".csv", encoding="utf-8", sep=";")
    dict = {'Nr_katalogowy': df["Nr_katalogowy"], 'Ilosc_produktow':df['Ilosc_produktow']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df['Ilosc_produktow'] = df['Ilosc_produktow'].round(decimals=0).astype('Int64')
    df = df.dropna()
    # df['Ilosc_produktow'] = df['Ilosc_produktow'].replace('.0', '', regex=True)
    # df['Ilosc_produktow'] = df['Ilosc_produktow'].astype(str).str.replace(r'.0','', regex=True)

    df.to_csv("tmp/Stany_Kaja" + date +"_Fixed.csv", encoding="utf-8", sep=";", index=False, mode="w")

def fixfixed(date):
    df = pd.read_csv("tmp/Stany_Kaja" + date +"_Fixed.csv", encoding="utf-8", sep=";")
    df = df.dropna()
    # df['Ilosc_produktow'] = df['Ilosc_produktow'].replace('.0', '', regex=True)
    # df['Ilosc_produktow'] = df['Ilosc_produktow'].astype(str).str.replace(r'.0','', regex=True)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].round(decimals=0).astype('Int64')
    df.to_csv("Stany_Kaja" + date +".csv", encoding="utf-8", sep=";", index=False, mode="w")

def timestamp():
    today = date.today()

    today = today.strftime("%d_%m_%Y")
    print(today)
    return today

def makeCSV():
    d = timestamp()
    addEglo(d)
    addCandelux(d)
    addHoldBox(d)
    addItalux(d)
    addLampex(d)
    addLedea(d)
    addLightPrestige(d)
    addMwGlasberg(d)
    addMaytoni(d)
    x = checkEkoLight()
    addEkoLight(x,d)
    addRabalux(d)
    # addTkLighting() pojebane kodowanie
    addZumaLine(d)
    fixCSV(d)
    fixfixed(d)




if __name__ == "__main__":
    makeCSV()