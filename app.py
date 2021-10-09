import datetime
import pymongo
from flask import Flask, request, jsonify

# Flask constructor takes the name of
# current module (__name__) as argument
app = Flask(__name__)

def get_mongo_conn():
    return pymongo.MongoClient("mongodb://34.125.100.172:27017")

@app.route("/pet/<petId>/record", methods = ["POST"])
def record(petId):
    m = get_mongo_conn()
    db = m["taller3"]
    col = db["pets"]
    record = request.json
    record["petId"] = petId
    record["datetime"] = datetime.datetime.now()
    col.insert_one(record)
    return "Se agrego un nuevo registro para la mascota {petId}".format(petId = petId), 201

@app.route("/pet/vitals")
def vitals_out_of_range():
    m=get_mongo_conn()
    db = m["taller3"]
    col = db["pets"]
    petId = int(request.args.get('petId'))
    timestamp1 =  request.args.get('date1')
    timestamp2 =  request.args.get('date2')
    cursor = col.find({"petId": petId, "datetime": {"$in":[timestamp1, timestamp2]}})
    if cursor is not None:
        cursor_temp = col.find({"temperature": {"$not": {"$in": [38.3, 39.2]}}}, {"_id": 0})
        '''cursor_hr = col.find({"heart-rate": {"$not": {"$in": [60, 120]}}}, {"_id": 0})
        cursor_breath = col.find({"breathing-frecuency": {"$not": {"$in": [10, 30]}}}, {"_id": 0})'''
        pets = []
        for pet in cursor_temp:
            pets.append(pet)
        return { "result": pets }
    else:
        return "No existe esta mascota en el registro"



if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()