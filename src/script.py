from httpx import AsyncClient
from src.enums import FormTypes
import asyncio

FORMS = [
    {
        "template": {
            "template_name": "OrderForm",
            "lead_email": FormTypes.EMAIL,
            "delivery_date": FormTypes.DATE,
            "order_date": FormTypes.DATE,
            "message": FormTypes.TEXT,
        },
        "instances": [
            {
                "lead_email": "example@mail.ru",
                "delivery_date": "17.01.2024",
                "order_date": "2024-01-01",
                "message": "Order message",
            },
            {
                "lead_email": "example@mail.ru",
                "delivery_date": "17.01.2024",
                "message": "Order message",
            }
        ]
    },
    {
        "template": {
            "template_name": "RegisterForm",
            "username": FormTypes.EMAIL,
            "password": FormTypes.TEXT,
            "born_date": FormTypes.DATE,
            "sex": FormTypes.TEXT,
        },
        "instances": [
            {
                "username": "example@mail.ru",
                "password": "12345",
                "born_date": "17.01.2002",
                "sex": "Male",
            },
            {
                "username": "example@mail.ru",
                "password": "12345",
                "born_date": "17.01.2002",
            }
        ]
    },
    {
        "template": {
            "template_name": "LoginForm",
            "username": FormTypes.EMAIL,
            "phone": FormTypes.PHONE,
            "password": FormTypes.TEXT,
        },
        "instances": [
            {
                "username": "example@mail.ru",
                "password": "1234",
                "phone": "+7 909 298 11 81",
            },
            {
                "password": "1234",
                "phone": "+7 909 298 11 81",
            },
        ]
    },
    {
        "template": {
            "template_name": "TicketForm",
            "tickets_send_to_email": FormTypes.EMAIL,
            "password": FormTypes.TEXT,
        },
        "instances": [
            {
                "tickets_send_to_email": "example@mail.ru",
                "password": "1234",
            },
            {
                "password": "1234",
            }
        ]
    }
]


FORMS_NOT_IN_DATABASE = [
    {
        "instance": {
            "username_first": "example@mail.ru",
            "username_second": "example@mail.ru",
            "born_date": "17.01.2002",
            "sex": "Male",
        },
        "expected_response": {
            "username_first": FormTypes.EMAIL,
            "username_second": FormTypes.EMAIL,
            "born_date": FormTypes.DATE,
            "sex": FormTypes.TEXT
        }
    },
    {
        "instance": {
            "username": "example@mail.ru",
            "first_name": "Danil",
            "last_name": "Fedorov",
            "phone": "+7 909 298 11 91"
        },
        "expected_response": {
            "username": FormTypes.EMAIL,
            "first_name": FormTypes.TEXT,
            "last_name": FormTypes.TEXT,
            "phone": FormTypes.PHONE,
        }
    }

]

BASE_URL = "http://0.0.0.0:8000"


async def add_forms():
    """Наполнить БД формами"""
    async with AsyncClient(base_url=BASE_URL) as client:
        for form in FORMS:
            await client.post(url="/forms", json=form["template"])


async def get_form():
    """Скрипт для создания запросов и проверки работоспособности приложения"""
    async with AsyncClient(base_url=BASE_URL) as client:
        for form in FORMS:
            template_name = form["template"]["template_name"]
            for instance in form["instances"]:
                response = await client.post(url="/get_form", json=instance)
                assert response.json() == template_name


async def get_form_not_in_database():
    """Скрипт для создания запросов с формами, которых нет в БД"""
    async with AsyncClient(base_url=BASE_URL) as client:
        for form in FORMS_NOT_IN_DATABASE:
            response = await client.post(url="/get_form", json=form["instance"])
            assert response.json() == form["expected_response"]


if __name__ == "__main__":

    """Здесь тестировать"""

    # asyncio.run(add_forms())
    # asyncio.run(get_form())
    # asyncio.run(get_form_not_in_database())
