import joblib

classifier = joblib.load('survival_pred.pkl')
print("Enter the following details to make the predictions:- n")

pclass = int(input("Enter The Passenger Class [1, 2, 3]:- "))
sex = int(input("Enter The Sex [0 for Male, 1 for Female]:- "))
fare = int(input("Enter The Fare [Float Value from 0 to 600]:- "))

passenger_prediction = classifier.predict([[pclass, sex, fare]])

if passenger_prediction == 0:
    print("Did Not Survive")
else:
    print("Survived")