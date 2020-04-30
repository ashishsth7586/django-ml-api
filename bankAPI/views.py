from django.shortcuts import render
from .forms import ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Approval
from .serializers import ApprovalSerializer
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
import os
from django.contrib import messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ApprovalView(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer


def ohevalue(df):
    ohe_col = ['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', \
                'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Gender_Male', \
                'Married_No', 'Married_Yes', 'Education_Graduate', 'Education_Not Graduate', \
                'Self_Employed_No', 'Self_Employed_Yes', 'Property_Area_Rural', \
                'Property_Area_Semiurban', 'Property_Area_Urban']
    cat_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf

def approveReject(unit):
    try:
        model = joblib.load(BASE_DIR + '/model/loan_model.pkl')
        scalers = joblib.load(BASE_DIR + '/model/scalers.pkl')
        x = scalers.transform(unit)
        y_pred = model.predict(x)
        y_pred = (y_pred > 0.52)
        # print(y_pred)
        # if y_pred[0][0] == False: 
        #     result = 'Rejected'
        # else:
        #     result = "Approved"
        newdf = pd.DataFrame(y_pred, columns=['status'])
        newdf = newdf.replace({True: 'Approved', False:'Rejected'})
        # return JsonResponse(f'{newdf}', safe=False)
        return newdf.values[0][0]
    except ValueError as e:
        return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)

def cxcontact(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['firstname']
            Lastname = form.cleaned_data['lastname']
            Dependants = form.cleaned_data['Dependents']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']

            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer = approveReject(ohevalue(df))
            messages.success(request, 'Application Status: {}'.format(answer))
    form = ApprovalForm()

    return render(request, 'csform.html', {'form': form})