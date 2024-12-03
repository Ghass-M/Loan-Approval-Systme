from experta import *

class ExpertSystem(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        yield Fact(action="loan_grading")

    # Reading inputs from console
    @Rule(Fact(action='loan_grading'),NOT(Fact(Age=W())),salience=-999)
    def feature_0(self):
        self.declare(Fact(Age=int(input(" Age: "))))

    @Rule(Fact(action='loan_grading'),NOT(Fact(Salary=W())),salience=-999)
    def feature_1(self):
        self.declare(Fact(Salary=int(input(" Salary: "))))

    @Rule(Fact(action='loan_grading'),NOT(Fact(Property=W())),salience=-999)
    def feature_2(self):
        self.declare(Fact(Property=input(" Property: ")))

    @Rule(Fact(action='loan_grading'),NOT(Fact(Vehicule=W())),salience=-999)
    def feature_3(self):
        self.declare(Fact(Vehicule=input(" Vehicule: ")))  

    @Rule(Fact(action='loan_grading'),NOT(Fact(Reason=W())),salience=-999)
    def feature_4(self):
        self.declare(Fact(Reason=input(" Reason: ")))

    @Rule(Fact(action='loan_grading'),NOT(Fact(Amount=W())),salience=-999)
    def feature_5(self):
        self.declare(Fact(Amount=int(input(" Amount: "))))
    
    @Rule(Fact(action='loan_grading'),NOT(Fact(Other=W())),salience=-999)
    def feature_6(self):
        self.declare(Fact(Other=int(input(" Other: "))))


    @Rule(Fact(action='loan_grading'),
          Fact(Age=MATCH.Age),
          Fact(Salary=MATCH.Salary),
          Fact(Property=MATCH.Property),
          Fact(Vehicule=MATCH.Vehicule),
          Fact(Reason=MATCH.Reason),
          Fact(Amount=MATCH.Amount),
          Fact(Other=MATCH.Other),
          TEST(lambda Age: Age >= 25 and Age <= 60),
          TEST(lambda Salary: Salary >= 1000),
          TEST(lambda Property: Property == "Owner"),
          TEST(lambda Vehicule: Vehicule == "True"),
          TEST(lambda Reason: Reason == "Business"),
          TEST(lambda Amount: Amount <= 10000),
          TEST(lambda Other: Other == 0)
          )
    def Grade(self):
        self.declare(Fact(Grade="A"))
        print("A")

    @Rule(Fact(action='loan_grading'),
          Fact(Age=MATCH.Age),
          Fact(Salary=MATCH.Salary),
          Fact(Property=MATCH.Property),
          Fact(Vehicule=MATCH.Vehicule),
          Fact(Reason=MATCH.Reason),
          Fact(Amount=MATCH.Amount),
          Fact(Other=MATCH.Other),
          TEST(lambda Age: Age > 60),
          TEST(lambda Salary: Salary < 1000),
          TEST(lambda Property: Property == "Renter"),
          TEST(lambda Vehicule: False),
          TEST(lambda Reason: Reason == "Personal"),
          TEST(lambda Amount: Amount > 100000),
          TEST(lambda Other: Other >= 0)
          )
    def Grade(self):
        self.declare(Fact(Grade="G"))
    

    @Rule(Fact(action='loan_grading'),
          Fact(Age=MATCH.Age),
          Fact(Salary=MATCH.Salary),
          Fact(Property=MATCH.Property),
          Fact(Vehicule=MATCH.Vehicule),
          Fact(Reason=MATCH.Reason),
          Fact(Amount=MATCH.Amount),
          Fact(Other=MATCH.Other),
          Fact(Grade=MATCH.Grade))
    def Grade(self,Age,Salary,Property,Vehicule,Reason,Amount,Other,Grade):
        print("Age: "+Age)
        print("Salary: "+Salary)
        print("Property: "+Property)
        print("Vehicule: "+Vehicule)
        print("Reason: "+Reason)
        print("Amount: "+Amount)
        print("Other loans in payment: "+Other)
        print("Loan Grade: "+Grade)
        predictionResult["Age"]=Age
        predictionResult["Salary"]=Salary
        predictionResult["Property"]=Property
        predictionResult["Vehicule"]=Vehicule
        predictionResult["Reason"]=Reason
        predictionResult["Amount"]=Amount
        predictionResult["Other"]=Other
        predictionResult["Grade"]=Grade
        
        
    @Rule(Fact(action='loan_grading'),
          Fact(Age=MATCH.Age),
          Fact(Salary=MATCH.Salary),
          Fact(Property=MATCH.Property),
          Fact(Vehicule=MATCH.Vehicule),
          Fact(Reason=MATCH.Reason),
          Fact(Amount=MATCH.Amount),
          Fact(Other=MATCH.Other),
          Fact(Grade=MATCH.Grade),
          NOT(Fact(Crop=MATCH.Grade)))
    def not_matched(self,Age,Salary,Property,Vehicule,Reason,Amount,Other):
        print("Your features doesn't matches our record")
        predictionResult["Grade"]="Not defined in our knowledge engine"

    @Rule(Fact(action='loan_grading'),
          Fact(Age=MATCH.Age),
          Fact(Salary=MATCH.Salary),
          Fact(Property=MATCH.Property),
          Fact(Vehicule=MATCH.Vehicule),
          Fact(Reason=MATCH.Reason),
          Fact(Amount=MATCH.Amount),
          Fact(Other=MATCH.Other),
          Fact(Grade=MATCH.Grade))
    def not_matched(self,Age,Salary,Property,Vehicule,Reason,Amount,Other):
        print("Your features doesn't matches our record")
        predictionResult["Grade"]="Not defined in our knowledge engine"


global predictionResult
predictionResult={}

engine=ExpertSystem()
engine.reset()
engine.run()

"""


def main(inputU):
    if (not inputU):
        print("Enter user characteristics")
    engine=ExpertSystem()
    engine.reset()
    engine.run()
    return predictionResult
    
"""