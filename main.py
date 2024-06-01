from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.checkin import checkin
from routes.booking import booking



app=FastAPI()

origin=[
    'http://localhost:5173',
    'http://localhost:5173/booking',
    'http://localhost:5173/checkIn',
    'http://localhost:5173/detail'

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )


# METODOS PARA LAS RESERVAS
@app.get('/')
def welcome():
    return {'msg':'welcome to server'}

app.include_router(checkin)
app.include_router(booking)




