from typing import Annotated, Optional, List
from pydantic import BaseModel, EmailStr, Field, BeforeValidator, ConfigDict
from datetime import datetime

PyObjectId = Annotated[str, BeforeValidator(str)]


class FormModelTemplate(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    template_name: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "template_name": "OrderForm",
                "lead_email": "email",
                "phone": "phone",
                "order_date": "date",
                "text": "Some info in any format you want",
            }
        },
    )


class FormCollection(BaseModel):
    forms: List[dict]

