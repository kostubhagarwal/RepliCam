from werkzeug import datastructures
from flask import send_file
from io import BytesIO

def samplefilemod(file: datastructures.FileStorage):
    proxy = BytesIO(file.read().upper())
    proxy.seek(0)
    return proxy
        
    

