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

if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()