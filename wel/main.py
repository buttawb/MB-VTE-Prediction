


def mortality(feat1, feat2, feat3):
    import joblib
    
    if feat1!='' and feat2!='' and feat3!='':
        feat1=float(feat1)
        feat2=float(feat2)
        feat3=float(feat3)
        Ratio1_NLR=feat1/feat2
        Ratio2_PLR=feat3/feat2
        Ratio3_SII=(feat1*feat3)/feat2
        
        cl=joblib.load('./SII.pkl')
        prediction=cl.predict([[Ratio3_SII]])
        if prediction[0]==1:
            return '1'
        else:
            return '2'
    
    
def mb(feat1, feat2, feat3):
    import joblib
    if feat1!='' and feat2!='' and feat3!='':
        feat1=float(feat1)
        feat2=float(feat2)
        feat3=float(feat3)
        Ratio1_NLR=feat1/feat2
        Ratio2_PLR=feat3/feat2
        Ratio3_SII=(feat1*feat3)/feat2
        
        cl=joblib.load('./MB.pkl')
        prediction=cl.predict([[Ratio2_PLR, Ratio3_SII]])
        if prediction[0]==1:
            return '1'
        else:
            return '2'
    
def vte(feat1, feat2, feat3):
    import joblib
    if feat1!='' and feat2!='' and feat3!='':
        feat1=float(feat1)
        feat2=float(feat2)
        feat3=float(feat3)
        Ratio1_NLR=feat1/feat2
        Ratio2_PLR=feat3/feat2
        Ratio3_SII=(feat1*feat3)/feat2
        
        
        cl=joblib.load('./VTE.pkl')
        prediction=cl.predict([[Ratio3_SII]])
        if prediction[0]==1:
            return '1'
        else:
            return '2'

    