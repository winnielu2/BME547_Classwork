from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

server = "http://vcm-7631.vm.duke.edu:5002"

ids = requests.get(server + "/get_patients/wl138")
print(ids.status_code)
print(ids.text)

idslist = ids.text.split('"')
id1 = idslist[3]
id2 = idslist[7]

bloodtype1 = requests.get(server + "/get_blood_type/" + str(id1))
print(bloodtype1.text)

bloodtype2 = requests.get(server + "/get_blood_type/" + str(id2))
print(bloodtype2.text)

if bloodtype1 == "O-":
    answer = "Yes"
elif bloodtype1 == "O+" and "+" in bloodtype2:
    answer = "Yes"
elif bloodtype1 == "A+" and (bloodtype2 == "A+" or bloodtype2 == "AB+"):
    answer = "Yes"
elif bloodtype1 == "A-" and "A" in bloodtype2:
    answer = "Yes"
elif bloodtype1 == "B+" and "B+" in bloodtype2:
    answer = "Yes"
elif bloodtype1 == "B-" and "B" in bloodtype2:
    answer = "Yes"
elif bloodtype1 == "AB+" and bloodtype2 == "AB+":
    answer = "Yes"
elif bloodtype1 == "AB-" and "AB" in bloodtype2:
    answer = "Yes"
else:
    answer = "No"

out = {"Name": "wl138", "Match": answer}
checkanswer = requests.post(server + "/match_check", json = out)
print(checkanswer.text)