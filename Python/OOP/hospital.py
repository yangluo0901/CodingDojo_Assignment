from random import *
class hospital(object):
    def __init__(self, patient_list,hospital_name, capacity):
        self.patient_list = patient_list
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.assigned_bed = []; # list of assigned beds
    def admit(self,patient):

        if len(self.patient_list) > self.capacity:
            print "Full!"
        else:
            new_bed_number = randint(1,self.capacity)
            if not new_bed_number in self.assigned_bed:
                self.assigned_bed.append(new_bed_number)
                patient.bed_number = new_bed_number
                new_patient = [patient.id, patient.name, patient.allergies, patient.bed_number]
                print "Patient #{} admitted to bed #{}".format(patient.id, new_bed_number)
            self.patient_list.append(new_patient)
    def discharge(self,patient):
        dischage_number = patient.id - 1
        self.assigned_bed.remove(patient.bed_number)
        self.patient_list.pop(dischage_number)
        patient.bed_number = None
        print "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_number)
        print "Below beds are not available: "
        print " ".join(map(str,self.assigned_bed))
    def info(self):
        print "Hospital: " + self.hospital_name
        print "Capacity: " +str(self.capacity)
        print self.patient_list

class patient(object):
    num = 1
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        self.id = patient.num
        patient.num += 1
    def info(self):
        print "Name: " +self.name
        print "Allergies: " + self.allergies
        print "Bed Number: " + str(self.bed_number)

h = hospital([],"LA hospital",100)
p_1 = patient("Yang","peanut")
p_2 = patient("Ran","cat")
p_3 = patient("kieu","intelligence")
h.admit(p_1)
h.admit(p_2)
h.admit(p_3)
h.discharge(p_1)
h.info()
p_1.info()
