def create_patient_entry(patient_first_name, patient_last_name, patient_id, patient_age):
    new_patient = {"First Name": patient_first_name,
    "Last Name": patient_last_name,
    "ID": patient_id,
    "Age": patient_age,
    "Tests": []}
    return new_patient

def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 30))
    db.append(create_patient_entry("Bob", "Boyles", 2, 34))
    db.append(create_patient_entry("Chris", "Chou", 3, 25))
    find_patient(db, 2)
    add_test(db, 2, "LDL", 200)
    print_db(db)
    print("Patient {} is a {}".format(get_full_name(db[2]), adult_or_minor(db[2])))

def print_db(db):
    for patient in db:
        print("Patient Name: " + get_full_name(patient) + ", " + 
        "Patient ID: " + str(patient["ID"]) + ", " + 
        "Patient Age: " + str(patient["Age"]) + ", " +
        "Tests: " + str(patient["Tests"]))

def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name

def find_patient(db, id):
    for patient in db:
        if patient["ID"] == id:
            return patient
    return False

def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"

def add_test(db, id, test_name, test_value):
    patient = find_patient(db, id)
    patient["Tests"] = patient["Tests"].append((test_name, test_value))

if __name__ == "__main__":
    main()
