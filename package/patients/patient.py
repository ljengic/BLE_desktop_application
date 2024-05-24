import sys
import time
import csv
from numbers import Number

def get_patient_from_csv(patient_file_path):

    rows = []

    with open( patient_file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
            file.close()

    patient = Patient(rows[0][1],rows[1][1],rows[2][1],rows[3][1])
    patient.add_chest_circumfences(rows[4][1], rows[5][1])
    patient.add_leg_circumfences(rows[6][1], rows[7][1], rows[8][1])
    patient.medications = []

    for row in rows[10:]:
        patient.medications.append(row[0])

    return patient

class Patient:
    def __init__(self, age, sex, height, weight):
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight

    def add_leg_circumfences(self,leg_ankle, leg_calf, leg_knee):
        self.leg_ankle = leg_ankle
        self.leg_calf = leg_calf
        self.leg_knee = leg_knee

    def add_chest_circumfences(self,chest_upper, chest_lower):
        self.chest_upper = chest_upper
        self.chest_lower = chest_lower

    def add_medications(self, medications):
        self.medications = medications

    def calculate_bmi(self):
        #function for calculate BMI
        self.bmi_float = float(self.weight) / (float(self.height) / 100.0)**2
        self.bmi = str(round(self.bmi_float, 2))

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

            self.writer.writerow(["Chest upper", self.chest_upper])
            self.writer.writerow(["Chest lower", self.chest_lower])

            self.writer.writerow(["Leg ankle", self.leg_ankle])
            self.writer.writerow(["Leg calf", self.leg_calf])
            self.writer.writerow(["Leg knee", self.leg_knee])             

            #write medication at the end, each in one row
            self.writer.writerow(["Meds, one in each row:"])
            for med in self.medications:
                self.writer.writerow([med])

            #zapisi i ostalo
            file.close()

    def check_patient_data(self):

        if(False == self.age.isnumeric()):
            return "Age is empty or invalid!"

        if(False == self.height.isnumeric()):
            return "Height is empty or invalid!"

        if(False == self.weight.isnumeric()):
            return "Weight is empty or invalid!"

        if(self.sex != 'M' and self.sex != 'F'):
            return "Please choose patient sex!"            

        #chest circumfence
        if(False == self.chest_upper.isnumeric()):
            return "Chest upper is empty or invalid!"

        if(False == self.chest_lower.isnumeric()):
            return "Chest lower is empty or invalid!"         

        #leg circumfence
        if(False == self.leg_ankle.isnumeric()):
            return "Leg ankle is empty or invalid!"

        if(False == self.leg_calf.isnumeric()):
            return "Leg calf is empty or invalid!"

        if(False == self.leg_knee.isnumeric()):
            return "Leg knee is empty or invalid!"

        return "Ok"

