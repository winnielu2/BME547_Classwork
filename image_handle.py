from tkinter import filedialog
import base64
from flask import Flask, request, jsonify
import requests


def upload_image():
    filename = get_image_file_name()
    b64_string = convert_file_to_b64(filename)
    upload_b64_to_server(b64_string)

def get_image_file_name():
    filename = filedialog.askopenfilename()
    return filename

def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding = 'utf-8')
    return b64_string

def upload_b64_to_server(b64_string):
    out_data = {"image": b64_string,
                "net_id": "wl138",
                "id_no": 1}
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image", json=out_data)
    print(r.status_code)
    print(r.text)

def save_image_from_server():
    r = requests.get("http://vcm-21170.vm.duke.edu/get_image/wl138/1")
    print(r.status_code)
    print(r.text)

def save_base64_string_to_file(b64_string):
    new_filename = "watermark.jpg"
    image_bytes = base64.b64decode(b64_string)
    with open(new_filename, "wb") as out_file:
        out_file.write(image_bytes)

if __name__ == "__main__":
    upload_image()
    save_image_from_server()