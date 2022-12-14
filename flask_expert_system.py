import expert_personal_finance as eps

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
  print("heredsdsdsd")
  age=int(request.form['age'])
  Income=int(request.form['income'])
  Food=int(request.form['food'])
  Rent=int(request.form['rent'])
  Health_insurance=int(request.form['health_insurance'])
  Vacations=int(request.form['vacations'])
  Expensive_clothes=int(request.form['expensive_clothes'])
  Entertainment=int(request.form['entertainment'])
  Real_estate=int(request.form['real_estate'])
  Stocks=int(request.form['stocks'])
  Pf_retirement=int(request.form['pf_retirement'])
  finance = eps.finance_expert(age, Income, Food, Rent, Health_insurance,  Vacations, Expensive_clothes, Entertainment,Real_estate, Stocks, Pf_retirement)
  finance.int_to_category()
  engine = eps.personalfinancemanagement()
  engine.reset()
  engine.declare(eps.Pf_retirementcheck(pfrcheck=finance.Pf_retirement_category))
  engine.declare(eps.Stockscheck(stoccheck=finance.Stocks_category))
  engine.declare(eps.Real_estatecheck(realcheck=finance.Real_estate_category))
  engine.declare(eps.Entertainmentcheck(entcheck=finance.Entertainment_category))
  engine.declare(eps.Expensive_clothescheck(expccheck=finance.Expensive_clothes_category))
  engine.declare(eps.Vacationscheck(vaccheck=finance.Vacations_category))
  engine.declare(eps.Health_insurancecheck(hcheck=finance.Health_insurance_category))
  engine.declare(eps.Rentcheck(rcheck=finance.Rent_category))
  engine.declare(eps.Foodcheck(fcheck=finance.Food_category))
  engine.declare(eps.savecheck(scheck=finance.savings_category))
  engine.declare(eps.wantcheck(wcheck=finance.wants_category))
  engine.declare(eps.needcheck(ncheck=finance.needs_category))
  engine.declare(eps.Incomebase(inclas=finance.income_category))
  engine.declare(eps.planselection(age=finance.age_finance_category))
  
  out_str = ""
  for row in engine.run(generate=True):
    if type(row) == tuple:
      for in_row in range(0,len(row)):
        out_str = out_str + "AIDI" + row[in_row] + "AIDI"
    else:
      out_str = out_str + "AIDI" + row
    out_str = out_str + " "
  # engine.age_junior

  return out_str

if __name__=='__main__':
  app.run()
