from urllib.parse import parse_qs
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

from joblib import Parallel, delayed
import joblib


def m(request):
    feat1 = 0
    feat2 = 0
    feat3 = 0
    result = 0
    result1 = 0
    final = 0
    ans = ''
    try:
        v1 = float(request.GET['n'])
        v2 = float(request.GET['l'])
        v3 = float(request.GET['p'])
        feat1 = v1
        feat2 = v2
        feat3 = v3
        final = mortality(feat1, feat2, feat3)
        result = final[0]
        result1 = final[1]
    except:
        pass
    return render(request, 'm.html', {'result': result, 'result1': result1})


def mb(request):
    feat1 = 0
    feat2 = 0
    feat3 = 0
    result = 0
    result1 = 0
    final = 0
    ans = ''
    try:
        v1 = float(request.GET['n'])
        v2 = float(request.GET['l'])
        v3 = float(request.GET['p'])
        feat1 = v1
        feat2 = v2
        feat3 = v3
        final = majorbleeding(feat1, feat2, feat3)
        result = final[0]
        result1 = final[1]
    except:
        pass
    return render(request, 'mb.html', {'result': result, 'result1': result1})


def v(request):
    feat1 = 0
    feat2 = 0
    feat3 = 0
    result = 0
    result1 = 0
    final = 0
    ans = ''
    try:
        v1 = float(request.GET['n'])
        v2 = float(request.GET['l'])
        v3 = float(request.GET['p'])
        feat1 = v1
        feat2 = v2
        feat3 = v3
        final = vte(feat1, feat2, feat3)
        result = final[0]
        result1 = final[1]
    except:
        pass
    return render(request, 'vte.html', {'result': result, 'result1': result1})


def main(request):
    return render(request, 'main.html')


def mortality(v1, v2, v3):
    feat1 = v1
    feat2 = v2
    feat3 = v3
    if feat1 != '' and feat2 != '' and feat3 != '':
        feat1 = float(feat1)
        feat2 = float(feat2)
        feat3 = float(feat3)
        Ratio1_NLR = feat1 / feat2
        Ratio2_PLR = feat3 / feat2
        Ratio3_SII = (feat1 * feat3) / feat2

        cl = joblib.load('./S.pkl')

        prediction = cl.predict_proba([[Ratio3_SII]])
        return prediction[0]


def majorbleeding(v1, v2, v3):
    feat1 = v1
    feat2 = v2
    feat3 = v3
    if feat1 != '' and feat2 != '' and feat3 != '':
        feat1 = float(feat1)
        feat2 = float(feat2)
        feat3 = float(feat3)
        Ratio1_NLR = feat1 / feat2
        Ratio2_PLR = feat3 / feat2
        Ratio3_SII = (feat1 * feat3) / feat2

        cl = joblib.load('./MB.pkl')
        prediction = cl.predict_proba([[Ratio2_PLR, Ratio3_SII]])
        return prediction[0]


def vte(v1, v2, v3):
    feat1 = v1
    feat2 = v2
    feat3 = v3
    if feat1 != '' and feat2 != '' and feat3 != '':
        feat1 = float(feat1)
        feat2 = float(feat2)
        feat3 = float(feat3)
        Ratio1_NLR = feat1 / feat2
        Ratio2_PLR = feat3 / feat2
        Ratio3_SII = (feat1 * feat3) / feat2

        cl = joblib.load('./VTE.pkl')
        prediction = cl.predict_proba([[Ratio3_SII]])
        return prediction[0]
