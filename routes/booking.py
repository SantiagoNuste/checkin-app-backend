from fastapi import APIRouter, HTTPException
from database import *
from models import Booking

booking=APIRouter()

@booking.get('/api/booking/code/{code}',response_model=Booking)
async def get_booking_by_code(code:str):
    res=await get_one_booking_by_code(code)
    return res


# obtener una reserva
@booking.get('/api/booking/{id}')
async def get_bookinhg(id:str):
    booking= await get_one_boooking(id)
    if booking:
        return booking
    return {'msg':'error'}

# obtener todas las reservas 
@booking.get('/api/booking')
async def get_bookings():
    res=await get_all_bookings()
    return res

# crear checkin
@booking.post('/api/booking')
async def create_booking(booking:Booking):
    response = await create_one_booking(booking.dict())
    print(response)
    return 'checkin created'

# actualizar reserva
@booking.put('/api/booking/{id}')
async def updtae_booking(id:str,booking:Booking):
    res=await update_one_booking(id,booking)
    return res

#