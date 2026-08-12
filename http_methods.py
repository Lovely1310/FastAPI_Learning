from fastapi import FastAPI,Path,HTTPException,Query
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
        raise HTTPException(status_code=404, detail='Patient not Found')

@app.get('/sort')
def sort_patients(sort_by:str=Query(...,decsription='sort on the basis of height, weight, BMI'),order:str=Query('asc',decsription='SORT IN ASC OR DESC ORDER')):
    valid_fields = ['height','weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid Field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400 , detail = 'Inavlid Field select from asc & desc')
    data = load_patients()
    sort_order = True if order =='desc' else False
    sorted_data = sorted(data.values(), key = lambda x:x.get(sort_by,0),reverse = sort_order)
    return sorted_data