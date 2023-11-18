from __future__ import annotations
from typing import Dict, List, Optional, TYPE_CHECKING
from fastapi import FastAPI, Depends
from src.core.mongo import get_collection
from fastapi import status
from fastapi.exceptions import RequestValidationError
from src.script import add_forms
from src.validation_service import get_validation_service


if TYPE_CHECKING:
    from src.validation_service import FormFieldsValidationService
    from motor.motor_asyncio import AsyncIOMotorCollection


app = FastAPI(debug=True, title="MongoDB+FASTApi", docs_url="/api/docs")


@app.post("/forms", response_description="Add new form", status_code=status.HTTP_201_CREATED)
async def create_form(
        form: Dict[str, str],
        forms_collection: AsyncIOMotorCollection = Depends(get_collection)
) -> Dict:
    if "template_name" not in form:
        raise RequestValidationError("Please check if you specify <template_name> parameter for your form")
    new_form = await forms_collection.insert_one(form)
    return await forms_collection.find_one({"_id": new_form.inserted_id}, projection={"_id": False})


@app.get("/forms", response_description="Get all forms", status_code=status.HTTP_200_OK)
async def forms_list(
        forms_collection: AsyncIOMotorCollection = Depends(get_collection)
) -> List[Dict[str, str]]:
    return await forms_collection.find(projection={"_id": False}).to_list(100)


@app.delete("/forms", description="Clear database", status_code=status.HTTP_204_NO_CONTENT)
async def delete_forms(form_collection: AsyncIOMotorCollection = Depends(get_collection)):
    await form_collection.delete_many({})


@app.post(
    "/get_form",
    response_description="Get form template name by field types and field values",
    status_code=status.HTTP_200_OK
)
async def get_form(
        template: Dict[str, str],
        forms_collection: AsyncIOMotorCollection = Depends(get_collection),
        service: FormFieldsValidationService = Depends(get_validation_service)
):
    input_type_fields = {}
    for field_name, field_value in template.items():
        field_type = await service.get_field_type(value=field_value)
        input_type_fields[field_name] = field_type

    forms = await forms_collection.find(input_type_fields, projection={"_id": False}).to_list(100)
    forms_by_match = sorted(forms, key=lambda _form: len(_form) - len(template))
    return forms_by_match[0]["template_name"] if forms_by_match else input_type_fields
