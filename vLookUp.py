
from datetime import time
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.io.pytables import Fixed
from pandas.io.sql import DatabaseError
import os
import shutil
import time





def makeDF():
    df1 = pd.read_csv("data/maytoni.csv", sep=";", encoding="utf-8", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Nr_katalogowy': df1['Nr_katalogowy'], 'Kod_producenta': df1['Kod_producenta']}
    df1 = DataFrame(dict)
    df1.to_csv("tmp/maytoni/MaytoniKaja.csv", encoding="utf-8", index=False, mode='w', sep=";")
    print(df1)

def makeDF1():
    df2 = pd.read_csv("pliki_sku/Maytoni.csv",sep=";", encoding="utf-8", skip_blank_lines=True, skipinitialspace=True)
    dict = {'Kod_producenta': df2['ItemNumber'], 'Qty':df2['ItemQuantityOnHand']}
    df2 = DataFrame(dict)
    df2.to_csv('tmp/maytoni/MaytoniExit.csv', sep=';', index=False, encoding='utf-8', mode="w")


def merge():
    df1 = pd.read_csv("tmp/maytoni/MaytoniKaja.csv", sep=";", encoding="utf-8", skip_blank_lines=True, skipinitialspace=True)
    df2 = pd.read_csv("tmp/maytoni/MaytoniExit.csv",sep=";", encoding="utf-8", skip_blank_lines=True, skipinitialspace=True)

    inner_join = pd.merge(
        df2,
        df1,
        on='Kod_producenta',
        how='left'
    )
    print(inner_join)
    # inner_join.dropna()
    # inner_join.astype("str")
    inner_join.to_csv("tmp/maytoni/test.csv", sep=';', encoding="utf-8", mode='w', index=False)

def mergeCSV():
    df = pd.read_csv('tmp/maytoni/test.csv', sep=";", encoding='utf-8')
    dict = {'Nr_katalogowy': df['Nr_katalogowy'], 'Qty':df['Qty']}
    df = DataFrame(dict)
    df = df.astype(str).dropna()
    df.to_csv("tmp/maytoni/StanyFixed.csv", sep=";", encoding="utf-8", mode='w', index=False)

def fixCSV():
    df = pd.read_csv('tmp/maytoni/StanyFixed.csv', sep=";", encoding='utf-8')
    dict = {'Nr_katalogowy': df['Nr_katalogowy'], 'Qty': df['Qty']}
    df = DataFrame(dict)
    # df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df = df.dropna()
    df.to_csv("tmp/maytoni/StanyFixedV2.csv", sep=";", encoding="utf-8", mode='w', index=False)

def fixDecimal():
    df = pd.read_csv('tmp/maytoni/StanyFixedV2.csv', sep=";", encoding='utf-8')
    dict = {'Nr_katalogowy': df['Nr_katalogowy'], 'Qty': df['Qty']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df.to_csv("pliki_csv/Maytoni.csv", sep=";", encoding="utf-8", mode='w', index=False)

def makedir():
    if os.path.isdir('tmp'):
        print("Exist")
    else:
        os.mkdir('tmp')

def cleartmp():
    try:
        shutil.rmtree('/tmp', ignore_errors=True)
    except:
        print("Błąd")

def makeHoldBox():
    df = pd.read_csv('data/holdbox.csv', sep=';', encoding="utf-8")
    dict = {'Nr_katalogowy': df['Nr_katalogowy'], 'Kod_producenta': df['Kod_producenta']}
    df = DataFrame(dict)
    df.to_csv("tmp/holdbox/HoldboxKaja.csv", encoding="utf-8", index=False, mode='w', sep=";")
    print(df)

def makeHoldBoxSku():
    df = pd.read_csv("pliki_sku/Holdbox.csv",sep=";", encoding="utf-8", skip_blank_lines=True, skipinitialspace=True)
    print(df.iloc[:, 0])
    kodProducenta = df.iloc[:, 0]
    stan = df.iloc[:, 2]
    dict = {'Kod_producenta': kodProducenta, 'Qty': stan}
    df = DataFrame(dict)
    df.to_csv('tmp/holdbox/HoldboxExit.csv', sep=';', index=False, encoding='utf-8', mode="w")
    print(df)


def mergeHoldbox():
    df1 = pd.read_csv("tmp/holdbox/HoldboxKaja.csv", sep=";", encoding="utf-8", skip_blank_lines=True, skipinitialspace=True)
    df2 = pd.read_csv("tmp/holdbox/HoldboxExit.csv",sep=";", encoding="utf-8", skip_blank_lines=True, skipinitialspace=True)

    inner_join = pd.merge(
        df2,
        df1,
        on='Kod_producenta',
        how='left'
    )
    print(inner_join)
    # inner_join.dropna()
    # inner_join.astype("str")
    inner_join.to_csv("tmp/holdbox/holdbox.csv", sep=';', encoding="utf-8", mode='w', index=False)

def mergeCSVHoldBox():
    df = pd.read_csv('tmp/holdbox/holdbox.csv', sep=";", encoding='utf-8')
    dict = {'Nr_katalogowy': df['Nr_katalogowy'], 'Qty':df['Qty']}
    df = DataFrame(dict)
    df = df.dropna()
    df.to_csv("tmp/holdbox/HoldboxFixed.csv", sep=";", encoding="utf-8", mode='w', index=False)

def fixHoldbox():
    df = pd.read_csv('tmp/holdbox/holdbox.csv', sep=";", encoding='utf-8')
    dict = {'Nr_katalogowy': df['Nr_katalogowy'], 'Qty':df['Qty']}
    df = DataFrame(dict)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df.to_csv("tmp/holdbox/FixedHoldbox.csv", sep=";", encoding="utf-8", mode='w', index=False)

def hotfixHoldbox():
    df = pd.read_csv('tmp/holdbox/FixedHoldbox.csv', sep=";", encoding='utf-8')
    dict = {'Nr_katalogowy': df['Nr_katalogowy'], 'Qty':df['Qty']}
    df = DataFrame(dict)
    df.dropna(inplace=True)
    df['Nr_katalogowy'] = df['Nr_katalogowy'].astype(str).str[0:13]
    df['Qty'] = df['Qty'].str.replace('Powyżej 500', '500')
    df['Qty'] = df['Qty'].str.replace('Powyżej 450', '450')
    df['Qty'] = df['Qty'].str.replace('Powyżej 400', '400')
    df['Qty'] = df['Qty'].str.replace('Powyżej 350', '350')
    df['Qty'] = df['Qty'].str.replace('Powyżej 300', '300')
    df['Qty'] = df['Qty'].str.replace('Powyżej 250', '250')
    df['Qty'] = df['Qty'].str.replace('Powyżej 200', '200')
    df['Qty'] = df['Qty'].str.replace('Powyżej 150', '150')
    df['Qty'] = df['Qty'].str.replace('Powyżej 100', '100')
    df['Qty'] = df['Qty'].str.replace('Powyżej 50', '50')
    df['Qty'] = df['Qty'].str.replace('Powyżej 50', '50')
    df['Qty'] = df['Qty'].str.replace('Powyżej 20', '20')
    df['Qty'] = df['Qty'].str.replace('Poniżej 20', '20')
    df['Qty'] = df['Qty'].str.replace('Poniżej 10', '10')
    df['Qty'] = df['Qty'].str.replace('wymaga potwierdzenia', '0')
    df.to_csv("pliki_csv/HoldBox.csv", sep=";", encoding="utf-8", mode='w', index=False)

def vLookUp():
    makedir()
    makeDF()
    makeDF1()
    merge()
    mergeCSV()
    fixCSV()
    fixDecimal()

    makeHoldBox()
    makeHoldBoxSku()
    mergeHoldbox()
    mergeCSVHoldBox()
    fixHoldbox()
    hotfixHoldbox()

    # Dodać maina do wcześniejszego programu2




if __name__ == "__main__":
    vLookUp()