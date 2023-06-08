import re
from flask import Flask, request, render_template
import pickle

model = pickle.load(open('knn (1).pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('main.html')
@app.route('/audit', methods=['GET', 'POST'])
def audit():
    return render_template('audit.html')

@app.route('/riskpred', methods=['GET', 'POST'])
def riskpred():
    if request.method == "POST":
        Sector_score = request.form['Sector_score']
        PARA_A = request.form['PARA_A']
        Risk_A = request.form['RISK_A']
        PARA_B = request.form['PARA_B']
        Risk_B = request.form['RISK_B']
        
        numbers = request.form['numbers']
        Money_Value = request.form['Money_Value']
        District_Loss = request.form['District_Loss']
        History = request.form['History']
      
        Inherent_Risk = request.form['Inherent_Risk']
        Audit_Risk = request.form['Audit_Risk']

        pred = [[float(Sector_score), float(PARA_A), float(Risk_A), float(PARA_B), float(Risk_B), float(numbers),
                 float(Money_Value), float(District_Loss), float(History), float(Inherent_Risk), float(Audit_Risk)]]

        print(pred)
        output = model.predict(pred)
        print(output)
        return render_template('result.html', predict="The Predicted Risk value is: " + str(output[0]))

if __name__ == "__main__":
    app.run(debug=True, port=8000)