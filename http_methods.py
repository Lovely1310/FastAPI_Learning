from fastapi import FastAPI
import json
app = FastAPI()

def load_patients():
    with open('patients.json') as f:
        data = json.load(f)
        return data

@app.get("/patients")
def get_patients():
    return {'message':'patients data'  }

@app.get("/about")
def get_about():
    return {'message':'About page'  }

@app.get("/view")
def view_patients():
    data = load_patients()
    return data