from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {'message':'fastapi working'}
@app.get("/about")
def about():
    return {'message':'it is an about section'}
@app.get("/division")
def division(x:int, y:int):
   return (x/y)
a=division(10,2)
print (a)
b=division(5,2)
print (b)




 