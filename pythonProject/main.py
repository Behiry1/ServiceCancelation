from tkinter import *
import tkinter as tk
import pickle
import numpy as np
import pandas as pd
root = Tk()


root.geometry("1000x500")


root.title('Service Cancelation Predictor')

algorithmChoiceLabel = Label(
    root, text="Methodology", width=20, font=("bold", 10))
algorithmChoiceLabel.place(x=5, y=10)

Mmsc = pickle.load(
    open('D:/Project/AI/ServiceCancelation/pythonProject/MinMaxScale.sav', 'rb'))


##########   Check Boxes    ###########
logisticRegressionChoice = IntVar()

loaded_model = pickle.load(open(
    'D:/Project/AI/ServiceCancelation/pythonProject/Logestic Regression.sav', 'rb'))


def Logistic_regression():
    filename = 'D:/Project/AI/ServiceCancelation/pythonProject/Logestic Regression.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print(loaded_model)


Checkbutton(root, text="Logistic Regression", variable=logisticRegressionChoice,
            command=Logistic_regression).place(x=100, y=40)


def SVM():
    filename = 'D:/Project/AI/ServiceCancelation/pythonProject/SVM.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print(loaded_model)


svmChoice = IntVar()
Checkbutton(root, text="SVM", variable=svmChoice,
            command=SVM).place(x=300, y=45)


def ID3():
    filename = 'D:/Project/AI/ServiceCancelation/pythonProject/Decision Tree.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print(loaded_model)


id3Choice = IntVar()
Checkbutton(root, text="ID3", variable=id3Choice,
            command=ID3).place(x=500, y=45)

##########   Check Boxes    ###########

##########   Buttons    ###########
trainButton = Button(root, text='Train', width=20,
                     bg="black", fg='white').place(x=20, y=80)
testButton = Button(root, text='Test', width=20,
                    bg="black", fg='white').place(x=200, y=80)
##########   Buttons    ###########


customerLabel = Label(root, text="Customer Data", width=20,
                      font=("bold", 10)).place(x=10, y=120)


###########          1                ####################
customerIdLabel = Label(root, text="Customer Id", width=20, font=("bold", 10))
customerIdLabel.place(x=30, y=150)
customerIdEntry = Entry(root)
customerIdEntry.place(x=160, y=150)


genderLabel = Label(root, text="Gender", width=20, font=("bold", 10))
genderLabel.place(x=300, y=150)
genderEntry = Entry(root)
genderEntry.place(x=430, y=150)


seniorCitzenLabel = Label(root, text="Senior Citzen",
                          width=20, font=("bold", 10))
seniorCitzenLabel.place(x=570, y=150)
seniorCitzenEntry = Entry(root)
seniorCitzenEntry.place(x=720, y=150)
###########          2               ####################
partenerLabel = Label(root, text="Partener", width=20, font=("bold", 10))
partenerLabel.place(x=30, y=180)
partenerEntry = Entry(root)
partenerEntry.place(x=160, y=180)


dependentLabel = Label(root, text="Dependent", width=20, font=("bold", 10))
dependentLabel.place(x=300, y=180)
dependentEntry = Entry(root)
dependentEntry.place(x=430, y=180)


tenureLabel = Label(root, text="Tensure", width=20, font=("bold", 10))
tenureLabel.place(x=570, y=180)
tenureEntry = Entry(root)
tenureEntry.place(x=720, y=180)
###########          3               ####################

phoneServiceLabel = Label(root, text="Phone Service",
                          width=20, font=("bold", 10))
phoneServiceLabel.place(x=30, y=210)
phoneServiceEntry = Entry(root)
phoneServiceEntry.place(x=160, y=210)


multipleLinesLabel = Label(root, text="Multiple Lines",
                           width=20, font=("bold", 10))
multipleLinesLabel.place(x=300, y=210)
multipleLinesEntry = Entry(root)
multipleLinesEntry.place(x=430, y=210)


internetServiceLabel = Label(
    root, text="Internet Service", width=20, font=("bold", 10))
internetServiceLabel.place(x=570, y=210)
internetServiceEntry = Entry(root)
internetServiceEntry.place(x=720, y=210)
###########          4               ####################

onlineSecurityLabel = Label(
    root, text="Online Security", width=20, font=("bold", 10))
onlineSecurityLabel.place(x=30, y=240)
onlineSecurityEntry = Entry(root)
onlineSecurityEntry.place(x=160, y=240)


onlineBackupLabel = Label(root, text="Online Backup",
                          width=20, font=("bold", 10))
onlineBackupLabel.place(x=300, y=240)
onlineBackupEntry = Entry(root)
onlineBackupEntry.place(x=430, y=240)

deviceProtectionLabel = Label(
    root, text="Device Protection", width=20, font=("bold", 10))
deviceProtectionLabel.place(x=570, y=240)
deviceProtectionEntry = Entry(root)
deviceProtectionEntry.place(x=720, y=240)
###########          5               ####################

techSupportLabel = Label(root, text="Tech Support",
                         width=20, font=("bold", 10))
techSupportLabel.place(x=30, y=270)
techSupportEntry = Entry(root)
techSupportEntry.place(x=160, y=270)

streamingTvLabel = Label(root, text="Streaming TV",
                         width=20, font=("bold", 10))
streamingTvLabel.place(x=300, y=270)
streamingTvEntry = Entry(root)
streamingTvEntry.place(x=430, y=270)


streamingMoviesLabel = Label(
    root, text="Device Protection", width=20, font=("bold", 10))
streamingMoviesLabel.place(x=570, y=270)
streamingMoviesEntry = Entry(root)
streamingMoviesEntry.place(x=720, y=270)
###########          6               ####################

contractsLabel = Label(root, text="Contracts", width=20, font=("bold", 10))
contractsLabel.place(x=30, y=300)
contractsEntry = Entry(root)
contractsEntry.place(x=160, y=300)


paperlessBillingLabel = Label(
    root, text="Paperless Billing", width=20, font=("bold", 10))
paperlessBillingLabel.place(x=290, y=300)
paperlessBillingEntry = Entry(root)
paperlessBillingEntry.place(x=430, y=300)


paymentMethodLabel = Label(root, text="Payment Method",
                           width=20, font=("bold", 10))
paymentMethodLabel.place(x=570, y=300)
paymentMethodEntry = Entry(root)
paymentMethodEntry.place(x=720, y=300)

###########          7               ####################

monthlyChargesLabel = Label(
    root, text="Monthly Charges", width=20, font=("bold", 10))
monthlyChargesLabel.place(x=20, y=330)
monthlyChargesEntry = Entry(root)
monthlyChargesEntry.place(x=160, y=330)


totalChargesLabel = Label(root, text="Total Charges",
                          width=20, font=("bold", 10))
totalChargesLabel.place(x=300, y=330)
totalChargesEntry = Entry(root)
totalChargesEntry.place(x=430, y=330)


def predict():
    rowinput = [float(seniorCitzenEntry.get()), float(tenureEntry.get()), float(monthlyChargesEntry.get()), float(genderEntry.get()), float(totalChargesEntry.get()), float(partenerEntry.get()), float(dependentEntry.get()), float(phoneServiceEntry.get()), float(multipleLinesEntry.get()), float(internetServiceEntry.get(
    )), float(onlineSecurityEntry.get()), float(onlineBackupEntry.get()), float(deviceProtectionEntry.get()), float(techSupportEntry.get()), float(streamingTvEntry.get()), float(streamingMoviesEntry.get()), float(contractsEntry.get()), float(paperlessBillingEntry.get()), float(paymentMethodEntry.get())]
    del rowinput[3]
    del rowinput[7]
    pred = loaded_model.predict([rowinput])
    print(pred)


predictButton = Button(root, text='Predict', width=20,
                       bg="black", fg='white', command=predict)
predictButton .place(x=380, y=400)


root.mainloop()
