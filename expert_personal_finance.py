
class finance_expert(object):
  Age = 0
  Income = 0
  Food = 0
  Rent = 0
  Health_insurance = 0
  Vacations = 0
  Expensive_clothes = 0
  Entertainment = 0
  Real_estate = 0
  Stocks = 0
  Pf_retirement = 0
  age_finance_category=""
  income_category=""
  needs_total=0
  wants_total=0
  savings_total=0
  needs_per=0
  wants_per=0
  savings_per=0
  Food_per=0
  Rent_per=0
  Health_insurance_per=0
  Vacations_per=0
  Expensive_clothes_per=0
  Entertainment_per=0
  Real_estate_per=0
  Stocks_per=0
  Pf_retirement_per=0
  needs_category=""
  wants_category=""
  savings_category=""
  Food_category=""
  Rent_category=""
  Health_insurance_category=""
  Vacations_category=""
  Expensive_clothes_category=""
  Entertainment_category=""
  Real_estate_category=""
  Stocks_category=""
  Pf_retirement_category=""

  def __init__(self, age, income, food, rent, health_insurance, vacations, expensive_clothes, entertainment, real_estate, stocks, pf_retirement):
    finance_expert.Age = int(age)
    finance_expert.Income = int(income)
    finance_expert.Food = int(food)
    finance_expert.Rent = int(rent)
    finance_expert.Health_insurance = int(health_insurance)
    finance_expert.Vacations = int(vacations)
    finance_expert.Expensive_clothes = int(expensive_clothes)
    finance_expert.Entertainment = int(entertainment)
    finance_expert.Real_estate = int(real_estate)
    finance_expert.Stocks = int(stocks)
    finance_expert.Pf_retirement = int(pf_retirement)
    finance_expert.age_finance_category=""
    finance_expert.income_category=""
    finance_expert.needs_total=0
    finance_expert.wants_total=0
    finance_expert.savings_total=0
    finance_expert.needs_per=0
    finance_expert.wants_per=0
    finance_expert.savings_per=0
    finance_expert.Food_per=0
    finance_expert.Rent_per=0
    finance_expert.Health_insurance_per=0
    finance_expert.Vacations_per=0
    finance_expert.Expensive_clothes_per=0
    finance_expert.Entertainment_per=0
    finance_expert.Real_estate_per=0
    finance_expert.Stocks_per=0
    finance_expert.Pf_retirement_per=0
    finance_expert.needs_category=""
    finance_expert.wants_category=""
    finance_expert.savings_category=""
    finance_expert.Food_category=""
    finance_expert.Rent_category=""
    finance_expert.Health_insurance_category=""
    finance_expert.Vacations_category=""
    finance_expert.Expensive_clothes_category=""
    finance_expert.Entertainment_category=""
    finance_expert.Real_estate_category=""
    finance_expert.Stocks_category=""
    finance_expert.Pf_retirement_category=""

  def int_to_category(self):
    if finance_expert.Age <= 32:
      finance_expert.age_finance_category= "Junior"
    else:
      finance_expert.age_finance_category= "Senior"

    if finance_expert.Income<=2000:
      finance_expert.income_category ="lower_class"  
    elif finance_expert.Income>2000 and finance_expert.Income<=5500:
      finance_expert.income_category ="Middle_class" 
    else:
      finance_expert.income_category ="Upper_class"

    finance_expert.needs_total = finance_expert.Food+finance_expert.Rent+finance_expert.Health_insurance
    finance_expert.wants_total = finance_expert.Vacations+finance_expert.Expensive_clothes+finance_expert.Entertainment
    finance_expert.savings_total = finance_expert.Real_estate+finance_expert.Stocks+finance_expert.Pf_retirement

    finance_expert.needs_per=finance_expert.needs_total*100/finance_expert.Income
    finance_expert.wants_per=finance_expert.wants_total*100/finance_expert.Income
    finance_expert.savings_per=finance_expert.savings_total*100/finance_expert.Income

    finance_expert.Food_per = finance_expert.Food*100/finance_expert.needs_total
    finance_expert.Rent_per = finance_expert.Rent*100/finance_expert.needs_total
    finance_expert.Health_insurance_per = finance_expert.Health_insurance*100/finance_expert.needs_total

    finance_expert.Vacations_per=finance_expert.Vacations*100/finance_expert.wants_total
    finance_expert.Expensive_clothes_per=finance_expert.Expensive_clothes*100/finance_expert.wants_total
    finance_expert.Entertainment_per=finance_expert.Entertainment*100/finance_expert.wants_total

    finance_expert.Real_estate_per=finance_expert.Real_estate*100/finance_expert.savings_total 
    finance_expert.Stocks_per=finance_expert.Stocks*100/finance_expert.savings_total 
    finance_expert.Pf_retirement_per=finance_expert.Pf_retirement*100/finance_expert.savings_total 


    #--------------------Accumulated_finance_management_Section-----------------------------
    if finance_expert.age_finance_category=="Junior" :
      if finance_expert.needs_per>50:
        finance_expert.needs_category="redzone"
      else:
        finance_expert.needs_category="greenzone"  
      if finance_expert.wants_per>20:
        finance_expert.wants_category="redzone"
      else:
        finance_expert.wants_category="greenzone"
      if finance_expert.savings_per>30:
        finance_expert.savings_category="redzone"
      else:
        finance_expert.savings_category="greenzone"

    elif  finance_expert.age_finance_category=="Senior" :  
      if finance_expert.needs_per>40:
        finance_expert.needs_category="redzone"
      else:
        finance_expert.needs_category="greenzone"  
      if finance_expert.wants_per>20:
        finance_expert.wants_category="redzone"
      else:
        finance_expert.wants_category="greenzone"
      if finance_expert.savings_per>40:
        finance_expert.savings_category="redzone"
      else:
        finance_expert.savings_category="greenzone"  

    #---------------------NEEDS_Internal_Finance_Manage_section---------------------------------
    if finance_expert.Food_per>15:
      finance_expert.Food_category="redzone"
    else:
      finance_expert.Food_category="greenzone"  
    if finance_expert.Rent_per>35:
      finance_expert.Rent_category="redzone"
    else:
      finance_expert.Rent_category="greenzone"
    if finance_expert.Health_insurance_per>20:
      finance_expert.Health_insurance_category="redzone"
    else:
      finance_expert.Health_insurance_category="greenzone"
    

    #---------------------Wants_Internal_Finance_Manage_section---------------------------------

    if finance_expert.Vacations_per>13:
      finance_expert.Vacations_category="redzone"
    else:
      finance_expert.Vacations_category="greenzone"  

    if finance_expert.Expensive_clothes_per>10:
      finance_expert.Expensive_clothes_category="redzone"
    else:
      finance_expert.Expensive_clothes_category="greenzone"

    if finance_expert.Entertainment_per>5:
      finance_expert.Entertainment_category="redzone"
    else:
      finance_expert.Entertainment_category="greenzone"  
   

    #---------------------Savings_Internal_Finance_Manage_section---------------------------------


    if finance_expert.Real_estate_per>10:
      finance_expert.Real_estate_category="redzone"
    else:
      finance_expert.Real_estate_category="greenzone"  
    if finance_expert.Stocks_per>5:
      finance_expert.Stocks_category="redzone"
    else:
      finance_expert.Stocks_category="greenzone"
  
    if finance_expert.Pf_retirement_per>40:
      finance_expert.Pf_retirement_category="redzone"
    else:
      finance_expert.Pf_retirement_category="greenzone"  

"""## EXPERTA"""

from random import choice
from experta import *
import types

class ReturningEngine(KnowledgeEngine):
    def run(self, steps=float('inf'), generate=False):
        if not generate:
            to_return = list()
            for rhs in self._run_activations(steps=steps):
                res = rhs()
                if res is not None:
                    if isinstance(res, types.GeneratorType):
                        to_return.extend(res)
                    else:
                        return res
            return to_return
        else:
            def _run_as_generator():
                for rhs in self._run_activations(steps=steps):
                    res = rhs()
                    if res is not None:
                        if isinstance(res, types.GeneratorType):
                            yield from res
                        else:
                            return res
            return _run_as_generator()

    def _run_activations(self, steps=float('inf')):
        """
        Execute agenda activations
        """

        self.running = True
        activation = None
        execution = 0
        try:
            while steps > 0 and self.running:

                added, removed = self.get_activations()
                self.strategy.update_agenda(self.agenda, added, removed)

                if watchers.worth('AGENDA', 'DEBUG'):  # pragma: no cover
                    for idx, act in enumerate(self.agenda.activations):
                        watchers.AGENDA.debug(
                            "%d: %r %r",
                            idx,
                            act.rule.__name__,
                            ", ".join(str(f) for f in act.facts))

                activation = self.agenda.get_next()

                if activation is None:
                    break
                else:
                    steps -= 1
                    execution += 1

                    watchers.RULES.info(
                        "FIRE %s %s: %s",
                        execution,
                        activation.rule.__name__,
                        ", ".join(str(f) for f in activation.facts))

                    yield lambda: activation.rule(
                        self,
                        **{k: v
                           for k, v in activation.context.items()
                           if not k.startswith('__')})
        except:
            raise
        finally:
            self.running = False

class planselection(Fact):
  pass

class needcheck(Fact):
  pass
  
class wantcheck(Fact):
  pass

class savecheck(Fact):
  pass

class Incomebase(Fact):
  pass  
  
class Light(Fact):
  pass  

#Needs all check 
class Foodcheck(Fact):
  pass

class Rentcheck(Fact):
  pass

class Health_insurancecheck(Fact):
  pass


#Wants all check 
class Vacationscheck(Fact):
  pass

class Expensive_clothescheck(Fact):
  pass

class Entertainmentcheck(Fact):
  pass

#Savings and investment all check 
class Real_estatecheck(Fact):
  pass

class Stockscheck(Fact):
  pass


class Pf_retirementcheck(Fact):
  pass



class personalfinancemanagement(ReturningEngine, finance_expert):
  
#--------------------------Plan Selection------------------------------  
  @Rule(planselection(age = "Junior"))
  def age_junior(self):
    yield ("As per your age you come under 50-30-20 rule")
   
  @Rule(planselection(age = "Senior"))
  def age_senior(self):
    yield ("As per your age you come under 40-20-40 rule")

#--------------------------Income base class------------------------------  
  @Rule(Incomebase(inclas = "lower_class" ))
  def income_lower(self):
    yield ("-As per your income invest in recurring ac and small period fixed deposits and take interest each smaller saving can give compound returns-")
   
  @Rule(Incomebase(inclas = 'Middle_class'))
  def income_middle(self):
    yield ("\n-As per your income invest in Share market and mutual funds and you are also advice to look into the term deposit-")

  @Rule(Incomebase(inclas = 'Upper_class'))
  def income_upper(self):
    yield ("-As per your income invest in bigger investment bonds and in companies treasury bills-")  

#-------------------------------------------------------- 
  @Rule(needcheck(ncheck = "redzone" ))
  def ncheck_red(self):     
    yield ("-------Red Alert------","Your expenditure percentage of NEEDS is {}.which is violating  the rule".format(finance_expert.needs_per))

  @Rule(needcheck(ncheck = "greenzone" ))
  def ncheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of NEEDS is {} and it in the rule frame well done".format(finance_expert.needs_per))
     
  @Rule(wantcheck(wcheck = "redzone" ))
  def wheck_red(self):     
    yield ("-------Red Alert------", "Yor expenditure percentage of WANTS is {}.which is violating  the rule".format(finance_expert.wants_per))

  @Rule(wantcheck(wcheck = "greenzone" ))
  def wcheck_green(self):
    yield ("-------Appreciation------","Your expenditure percentage of WANTS is {} and it in the rule frame well done".format(finance_expert.wants_per))

  @Rule(savecheck(scheck = "redzone" ))
  def scheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Savings and Investment is {}.which is violating  the rule".format(finance_expert.savings_per))

  @Rule(savecheck(scheck = "greenzone" ))
  def scheck_green(self):
    yield ("-------Appreciation------","Your expenditure percentage of Savings and Investment is {} and it in the rule frame well done".format(finance_expert.savings_per))
    
  @Rule(Foodcheck(fcheck = "redzone" ))
  def fcheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Grocery & Bills is {}.which is violating  the rule".format(finance_expert.Food_per))

  @Rule(Foodcheck(fcheck = "greenzone" ))
  def fcheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Grocery & Bills is {} and it in the rule frame well done".format(finance_expert.Food_per))

  @Rule(Rentcheck(rcheck = "redzone" ))
  def rcheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Rent & Utilities is {}.which is violating  the rule".format(finance_expert.Rent_per))

  @Rule(Rentcheck(rcheck = "greenzone" ))
  def rcheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Rent & Utilities is {} and it in the rule frame well done".format(finance_expert.Rent_per))

  @Rule(Health_insurancecheck(hcheck = "redzone" ))
  def hcheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Insurances is {}.which is violating  the rule".format(finance_expert.Health_insurance_per))

  @Rule(Health_insurancecheck(hcheck = "greenzone" ))
  def hcheck_green(self):
    yield ("-------Appreciation------","Your expenditure percentage of Insurance is {} and it in the rule frame well done".format(finance_expert.Health_insurance_per))
     
 

######Wants Internal  
       
  @Rule(Vacationscheck(vaccheck = "redzone" ))
  def vaccheck_red(self):     
    yield ("-------Red Alert------","Your expenditure percentage of Vacations is {}.which is violating  the rule".format(finance_expert.Vacations_per) )

  @Rule(Vacationscheck(vaccheck = "greenzone" ))
  def vaccheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Vacations is {} and it in the rule frame well done".format(finance_expert.Vacations_per))
 
  @Rule(Expensive_clothescheck(expccheck = "redzone" ))
  def expccheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Leisure is {}.which is violating  the rule".format(finance_expert.Expensive_clothes_per))

  @Rule(Expensive_clothescheck(expccheck = "greenzone" ))
  def expccheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Leisure is {} and it in the rule frame well done".format(finance_expert.Expensive_clothes_per))
             
 
  @Rule(Entertainmentcheck(entcheck = "redzone" ))
  def entcheck_red(self):     
    yield ("\n-------Red Alert------", "Your expenditure percentage of Entertainment & Hobbies is {}.which is violating  the rule".format(finance_expert.Entertainment_per))

  @Rule(Entertainmentcheck(entcheck = "greenzone" ))
  def entcheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Entertainment & Hobbies  is {} and it in the rule frame well done".format(finance_expert.Entertainment_per))

 
######Savings And investment Internal

  @Rule(Real_estatecheck(realcheck = "redzone" ))
  def realcheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Savings is {}.which is violating  the rule".format(finance_expert.Real_estate_per))

  @Rule(Real_estatecheck(realcheck = "greenzone" ))
  def realcheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Savings is {} and it in the rule frame well done".format(finance_expert.Real_estate_per))

  @Rule(Stockscheck(stoccheck = "redzone" ))
  def stoccheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Stocks & Mutual Funds is {}.which is violating  the rule".format(finance_expert.Stocks_per))

  @Rule(Stockscheck(stoccheck = "greenzone" ))
  def stoccheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Stocks & Mutual Funds is {} and it in the rule frame well done".format(finance_expert.Stocks_per))

 
  @Rule(Pf_retirementcheck(pfrcheck = "redzone" ))
  def pfrcheck_red(self):     
    yield ("-------Red Alert------", "Your expenditure percentage of Pf_retirement & Fixed Deposits is {}.which is violating  the rule".format(finance_expert.Pf_retirement_per))

  @Rule(Pf_retirementcheck(pfrcheck = "greenzone" ))
  def pfrcheck_green(self):
    yield ("-------Appreciation------", "Your expenditure percentage of Pf_retirement & Fixed Deposits is {} and it in the rule frame well done".format(finance_expert.Pf_retirement_per))
