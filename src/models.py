from typing import Annotated, Optional, List

from pydantic import BaseModel, EmailStr, Field, BeforeValidator, ConfigDict
from datetime import datetime

PyObjectId = Annotated[str, BeforeValidator(str)]


class FormModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    template_name: str = Field(...)
    lead_email: EmailStr = Field(...)
    phone: str = Field(...)
    order_date: datetime = Field(...)
    text: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class FormCollection(BaseModel):
    forms: List[FormModel]

