from motor.motor_asyncio import AsyncIOMotorClient
from models import Booking, Checkin


mongo_url='mongodb+srv://santi07:34321sd777rm10D@cluster0.qhxox.mongodb.net/?retryWrites=true&w=majority'
client=AsyncIOMotorClient(mongo_url)
database=client.bookingBatabase
booking_collection=database.bookings
checkin_collection=database.checkins

# obtener reserva exixtente
async def get_one_boooking(id):
    booking= await booking_collection.find_one({'_id':id})
    return booking

# obtener reserva por codigo
async def get_one_booking_by_code(code:str):
    booking=await booking_collection.find_one({'code':code})
    return booking


# crear reserva
async def create_one_booking(booking_data):
    new_booking=await booking_collection.insert_one(booking_data)
    created_booking= await booking_collection.find_one({'_id':new_booking.inserted_id})
    return created_booking

# obtener todas reserva
async def get_all_bookings():
    bookings=[]
    cursor= booking_collection.find()
    async for document in cursor:
        bookings.append(Booking(**document))
    return bookings

# actualizar reserva
async def update_one_booking(id:str,bookin_data):
    await booking_collection.update_one({'_id':id},{'$set':bookin_data})
    document= await booking_collection.find_one({'_id':id})
    return document






# obtener todss las checkin
async def get_all_checkins():
    checkins=[]
    cursor=  checkin_collection.find({})
    async for document in cursor:
        checkins.append(Checkin(**document))
    return checkins

# obtener checkin
async def get_one_checkin(id:str):
    booking= await checkin_collection.find_one({'_id':id})
    print(booking)
    return booking

# actulizar checkin
async def update_one_checkin(id:str,checkin):
    await checkin_collection.update_one({'_id':id},{'$set':checkin})
    document=await checkin_collection.find_one({'_id':id})
    return document

# crear checkin
async def create_one_checkin(checkin):
    new_checkin= await checkin_collection.insert_one(checkin)
    created_checkin =await checkin_collection.find_one({'_id':new_checkin.inserted_id})
    return created_checkin

# eliminar Checkin
async def delete_one_checkin(id:str):
    await checkin_collection.delete_one({'_id':id})
    return True

# obtener por codigo de reserva
async def get_one_checkin_by_code(code:str):
    booking=await checkin_collection.find_one({'code':code})
    return booking


