from fastapi import APIRouter,HTTPException
from database import *

checkin=APIRouter()

# METODOS PARA LOS CHECKINS
@checkin.get('/api/checkin')
async def get_checkins():
    bookings= await get_all_checkins()
    return bookings

@checkin.get('/api/checkin/{id}')
async def get_checkin(id:str):
    res =await get_one_checkin(id)

# crear checkin
@checkin.post('/api/checkin',response_model=Checkin)
async def create_checkin(checkin:Checkin):
    found_checkin=await get_one_checkin_by_code(checkin.code)
    print(found_checkin)
    if found_checkin:
        raise HTTPException(409,'checkin already exixts')

    response = await create_one_checkin(checkin.dict())
    print(response)

    if response:
        return response
    raise HTTPException(400,'something went wrong')

# actualizar checkin
@checkin.put('/api/checkin/{id}')
async def updtae_checkin(id:str,checkin:Checkin):
    res=await update_one_checkin(id,checkin)
    return res

# eliminar checkin
@checkin.delete('/api/checkin/{id}')
async def delete_checkin(id:str):
    res=await delete_one_checkin(id)
    return res

# obtener checkin por codigo de reserva
@checkin.get('/api/checkin/code/{code}',response_model=Checkin)
async def get_by_code(code:str):
    res=await get_one_checkin_by_code(code)
    return res
             