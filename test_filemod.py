from werkzeug import datastructures

def samplefilemod(file: datastructures.FileStorage):
    print(file.stream, type(file.stream))

