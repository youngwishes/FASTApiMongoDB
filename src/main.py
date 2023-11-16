from __future__ import annotations
from typing import Dict, List, Optional
from fastapi import FastAPI
from src.core.mongo import forms_collection
from fastapi import status
from fastapi.exceptions import RequestValidationError

app = FastAPI(debug=True, title="MongoDB+FASTApi", docs_url="/api/docs")


@app.post("/forms", response_description="Add new form", status_code=status.HTTP_201_CREATED)
async def create_form(form: Dict[str, str]) -> Dict:
    if "template_name" not in form:
        raise RequestValidationError("Please check if you specify <template_name> parameter for your form")
    new_form = await forms_collection.insert_one(form)
    return await forms_collection.find_one({"_id": new_form.inserted_id}, projection={"_id": False})


@app.get("/forms", response_description="Get all forms", status_code=status.HTTP_200_OK)
async def forms_list() -> List[Dict[str, Optional[str]]]:
    return await forms_collection.find(projection={"_id": False}).to_list(20)


@app.post(
    "/get_form",
    response_description="Get form template name by field types and field values",
    status_code=status.HTTP_200_OK
)
async def get_form(form: Dict[str, str]) -> str:
    return await forms_collection.find_one(...)
