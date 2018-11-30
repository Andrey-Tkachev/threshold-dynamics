import os.path
import csv
import json
import numpy as np
import pickle

import constants

def Tabulate(func, rng: tuple):
    points = []
    for point in np.arange(*rng):
        points.append((point, func(point)))
    return points

def IsReal(string):
    try:
        float(string)
    except ValueError:
        return False

    return True

def safe(func):
    def wrap(filePath, mode='r'):
        if not os.path.isfile(filePath):
            return None

        try:
            with open(filePath, mode) as file:
                return func(file)
        except Exception as e:
            pass

        return None

    return wrap

def safe_dir(func):
    def wrap(filePath, obj, mode='w'):
        if not os.path.isdir(os.path.dirname(filePath)):
            return False

        with open(filePath, mode) as file:
            func(file, obj)
            return True
        return False

    return wrap

@safe
def loadCSV(file, mode='r'):
    result = []
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if not all([IsReal(x) for x in row]):
            return None
        result.append([float(x) for x in row])

    return result

@safe
def loadJson(file):
    return json.load(file)

@safe
def loadPickle(file, mode='rb'):
    return pickle.load(file)

@safe_dir
def dumpPickle(file, obj, mode='wb'):
    pickle.dump(obj, file)

@safe_dir
def dumpJson(file, obj, mode='wb'):
    json.dump(obj, file)

@safe_dir
def dumpCSV(file, obj, mode='wb'):
    writer = csv.writer(file, delimiter=',')
    for row in obj:
        writer.writerow(row)

def dumpFunc(func, filePath, mode=constants.INTERPOL, rng=None):
    if mode == constants.INTERPOL:
        dumpJson(filePath, func.dump_to_dict(), mode='w')
    else:
        dumpCSV(filePath, Tabulate(func, rng), mode='w')