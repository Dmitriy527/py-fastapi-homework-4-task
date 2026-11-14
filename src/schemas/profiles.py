from datetime import date

from fastapi import UploadFile, Form, File, HTTPException
from pydantic import BaseModel, field_validator, HttpUrl

from validation import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date,
    validate_info
)

class ProfileSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    gender: str | None = None
    birth_date: date
    info: str | None = None
    avatar: str | None = None

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, value):
        try:
            validate_name(value)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=e.__str__())

        return value


    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, value):
        try:
            validate_name(value)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=e.__str__())

        return value


    @field_validator("gender")
    @classmethod
    def validate_gender(cls, value):
        try:
            validate_gender(value)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=e.__str__())

        return value


    @field_validator("birth_date")
    @classmethod
    def validate_birth_date(cls, value):
        try:
            validate_birth_date(value)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=e.__str__())

        return value


    @field_validator("info")
    @classmethod
    def validate_info(cls, value):
        try:
            validate_info(value)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=e.__str__())

        return value


    @field_validator("avatar")
    @classmethod
    def validate_avatar(cls, value):
        try:
            validate_image(value)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=e.__str__())

        return value
