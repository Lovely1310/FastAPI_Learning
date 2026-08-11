from fastapi import FastAPI,Path
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
def view():
    data = load_patients()
    return data

@app.get('/patients/{patient_id}')
def view_patients(patient_id:str = Path(...,decsription = 'ID of the patients in the DB',example='P001')):
        data = load_patients()

        if patient_id in data:
          return data[patient_id]
        return{'error':'patient not found'}