from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
@app.route('/')
def man():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')    

@app.route('/predict', methods=['GET','POST'])
def after():
    data1 = request.form.get('Dependents')
    data2 = request.form.get('Self_Employed')
    data3 = request.form.get('applicantincome')
    data4 = request.form.get('coapplication')
    data5 = request.form.get('loanamount')
    data6 = request.form.get('credit_history')
    data7 = request.form.get('Property_Area')

    #sample1 = model.predict[['Male', '0', 'Graduate', 'No', 4583, 1508.0, 128.0, 360.0, 1.0, 'Rural']]

    pred = model.predict([[data1, data2, data3, data4, data5, data6, data7]])
    #pred = sample1

    # if(pred=='N'):
    #     prediction = "Not Appreoved"
    # else:
    #     prediction = "Approved"

    return render_template('after.html', data=str(pred[0]))

if __name__ == "__main__":
     app.run(debug=True)




# from re import I
# from flask import Flask, render_template

# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)

