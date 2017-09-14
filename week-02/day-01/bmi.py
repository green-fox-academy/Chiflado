massInKg = 95
heightInM = 1.83

#Print the Body mass index (BMI) based on these values

def bmi_calulation(massInKg, heightInM):
    bmi = massInKg / (heightInM ** 2)
    print(bmi)

bmi_calulation(massInKg, heightInM)