from fastapi import FastAPI, APIRouter, Body
from src.models import FormModel, FormCollection
from src.core.mongo import forms_collection
from fastapi import status

app = FastAPI(debug=True, title="Mongo+FASTApi", docs_url="/api/docs")


@app.post(
    "/forms",
    response_description="Add new form",
    response_model=FormModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_form(form: FormModel = Body(...)) -> FormModel:
    new_form = await forms_collection.insert_one(form.model_dump(by_alias=True, exclude={"id"}))
    created_form = await forms_collection.find_one({"_id": new_form.inserted_id})
    return created_form


@app.get(
    "/forms",
    response_description="Get all forms",
    response_model=FormCollection,
    response_model_by_alias=False,
)
async def forms_list() -> FormCollection:
    return FormCollection(forms=await forms_collection.find().to_list(1000))


@app.post(
    "/get_form",
    response_description="Find form by fields",
    response_model=FormModel,
    response_model_by_alias=False,
)
async def get_form():
    pass
