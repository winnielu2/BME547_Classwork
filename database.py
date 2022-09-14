def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient

def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    print_db(db)
    find_patient(db, 2)
    add_test(db, 2, "LDL", 200)
    print(db)
    return db

def print_db(db):
    for patient in db:
        print("Patient Name: " + patient[0] + ", " + 
        "Patient ID: " + str(patient[1]) + ", " + 
        "Patient Age: " + str(patient[2]))

def find_patient(db, id):
    for patient in db:
        if patient[1] == id:
            return patient
    return False

def add_test(db, id, test_name, test_value):
    patient = find_patient(db, id)
    patient[3].append((test_name, test_value))

if __name__ == "__main__":
    main()
