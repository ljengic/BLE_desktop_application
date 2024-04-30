import sys
import time
import csv

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

    def add_medications(self, medications):
        self.medications = medications

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

        print("Med list: ", self.medications)

    def write_to_csv(self, patient_file_path):
        print("Writing patient data to file.")
        with open( patient_file_path, 'w', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(["Age",    self.age])
            self.writer.writerow(["Sex",    self.sex])
            self.writer.writerow(["Height", self.height])
            self.writer.writerow(["Weight", self.weight])

            #write medication at the end, each in one row
            self.writer.writerow(["Meds, one in each row:"])
            for med in self.medications:
                self.writer.writerow([med])

            #zapisi i ostalo
            file.close()

    #function for checking if data is valid

