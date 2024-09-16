import re
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError



class UserForm(BaseModel):


    username: str = Field(..., min_length=2)
    phonenumber: int
    email: EmailStr


    @field_validator("phonenumber")
    @classmethod
    def validate_phonenumber(cls, value):
        if not re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', str(value)):
            raise ValidationError
        
        return value