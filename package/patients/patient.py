import sys
import time

class Patient:
    def __init__(self, age, sex, height, weight):
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        #function for calculate BMI

    def add_leg_circumfences(self,leg_ankle, leg_calf, leg_knee):
        self.leg_ankle = leg_ankle
        self.leg_calf = leg_calf
        self.leg_knee = leg_knee

    def add_chest_circumfences(self,chest_upper, chest_lower):
        self.chest_upper = chest_upper
        self.chest_lower = chest_lower

    def print_patient_info(self):
        print("\n")
        print("Age:", self.age)
        print("Sex: ",self.sex)
        print("Height:", self.height)
        print("Weight:", self.weight)

        print("\n")
        print("Chest upper: ", self.chest_upper)
        print("Chest lower: ", self.chest_lower)

        print("\n")
        print("Leg ankle: ", self.leg_ankle)
        print("Leg calf: ", self.leg_calf)
        print("Leg knee: ", self.leg_knee)

    #def parse_csv_to_patient(self,csv_row):


    #function for checking if data is valid

