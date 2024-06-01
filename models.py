from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId as BsonObjectId
from typing import Optional


# Clase personalizada para ObjectId
class PyObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not BsonObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return BsonObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type='string')

# Modelo de datos Checkin usando Pydantic
class Checkin(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    code: str 
    number_id_person: str
    full_name: str
    email: str
    country:str
    city:str
    address:str
    number_phone: int
    date_checkin: str
    date_checkout:str

    class Config:
        json_encoders = {
            BsonObjectId: str
        }
        schema_extra = {
            "example": {
                "id": "60b8d295f1e5b6d7f8a6b7f3",
                "code": "CHK123",
                "number_id_person": "123456789",
                "full_name": "John",
                "email": "johndoe@example.com",
                "country":"colombia",
                "city":"cali",
                "address":"calle 212-4234",
                "number_phone": 1234567890,
                "date_checkin": "20/03/2024",
                "date_checkout": "23/03/2024"
            }
        }

# Modelo de datos Booking usando Pydantic
class Booking(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    code: str
    name: str

    class Config:
        json_encoders = {
            BsonObjectId: str
        }
        schema_extra = {
            "example": {
                "id": "60b8d295f1e5b6d7f8a6b7f3",
                "code": "BK123",
                "name": "John Doe"
            }
        }

