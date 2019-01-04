# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import re
from sklearn.feature_extraction.text import CountVectorizer
from TurkishStemmer import TurkishStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
stemmer = TurkishStemmer()
vectorizer = CountVectorizer()
# %% Methodlar baslangic

word_list = [] # kelimelerin tek yazilmasi için
examples = []
np_exmaples = []
 
myWords=['ali','bugun','okula','erken','ve','veya','gelmedi','sınıfa']

conjunctions = set(stopwords.words('turkish'))
x= None
dizi=[]
testSayisi = None
# %% Methodlar

def testingObject():
    global x,icerik, testSayisi
    files = filedialog.askopenfilenames(initialdir="/", title="Select file",filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    i = 1
    
    for file in files:
        Lb1.insert(i, file)
        file_content = open(file, "r").read()
        content = file_content.lower()
        kokDizi = re.findall(r'\w+', content)
 
        icerik=' '.join(kokDizi)
        dizi.append(icerik)
        testSayisi = len(dizi)
 
          
def tutorialObject():
        global x,icerik
      
        files = filedialog.askopenfilenames(initialdir="/", title="Select file",filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        i = 1
        for file in files:
            Lb1.insert(i, file)
            file_content = open(file, "r").read()
            content = file_content.lower()
            kokDizi = re.findall(r'\w+', content)
     
            icerik=' '.join(kokDizi)
            dizi.append(icerik)
    
        x = vectorizer.fit_transform(dizi).toarray()
        print(x)
        
def resultFunction():
    global x, testSayisi
    #n_neighbors=2 klavyeden alıcak
    number = int(e1.get())
    print(number)
    if testSayisi == number :
        nbrs = NearestNeighbors(n_neighbors=number, algorithm='auto', metric='cosine').fit(x[testSayisi:])
        distances, indices = nbrs.kneighbors(x[0:testSayisi])
        i = 0
        for distance in distances:
            j = 0
            for indice in indices:
                if i == j:
                    distance = distance -1
                    distance *= -1
                    distance *= 100
                    print("testin " +str(j)+": "+str(indice) +  " " + str(distance))
                j += 1
            i += 1
    else:
        messagebox.showinfo("Hata Mesajı", "Test Sayısı ile K değeri eşit değil")
# %% formu çiz
 
# %% Methodlar bitis
pencere = Tk()
pencere.title("Text Similarity 1.0")
pencere.geometry("700x320")
# grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()
# %% 1.Bolme
L1 = Label(uygulama, text="Dosyalar")
L1.grid(row=0,column=0)

Lb1 = Listbox(uygulama, width = 40)
Lb1.grid(row=1,column=0,padx=20)

btnFileTestObject = Button(uygulama, text="Test Verileri Yükle", width=20, command=testingObject)
btnFileTestObject.grid(row=2,column=0,padx=20,pady=15)
# %%  2.Bolme

L2 = Label(uygulama, text="Test Sonuçlari")
L2.grid(row=0,column=1)

Lb2 = Listbox(uygulama, width = 55)
Lb2.grid(row=1,column=1,padx=60)

btnFileTestObject = Button(uygulama, text=" Sonuçları Göster ", width=20, command=resultFunction)
btnFileTestObject.grid(row=2,column=1,padx=20,pady=15)

L3 = Label(uygulama, text="K Değerini Giriniz :")
L3.grid(row=3,column=1)

e1 = Entry(uygulama)
e1.grid(row=4, column=1)

btnResult = Button(uygulama, text="Eğitim Verileri Yükle", width=20, command=tutorialObject)
btnResult.grid(row=3,column=0,padx=10,pady=5)

# %% formu çiz
pencere.mainloop()