import re
import phonenumbers

from datetime import datetime
from src.enums import FormTypes


class FormFieldsValidationService:
    async def get_field_type(self, value: str):
        if field_type := await self.validate_date(value=value):
            return field_type
        if field_type := await self.validate_phone(value=value):
            return field_type
        if field_type := await self.validate_email(value=value):
            return field_type
        return FormTypes.TEXT

    @staticmethod
    async def validate_date(value: str) -> FormTypes | None:
        possible_date_formats = ("%Y-%m-%d", "%d.%m.%Y")
        for date_format in possible_date_formats:
            try:
                datetime.strptime(value, date_format)
                return FormTypes.DATE
            except ValueError:
                pass

    @staticmethod
    async def validate_email(value: str) -> FormTypes | None:
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):
            return FormTypes.EMAIL
        return

    @staticmethod
    async def validate_phone(value: str) -> FormTypes | None:
        try:
            number = phonenumbers.parse(value)
            return FormTypes.PHONE if phonenumbers.is_possible_number(number) else None
        except phonenumbers.NumberParseException:
            return


async def get_validation_service() -> FormFieldsValidationService:
    return FormFieldsValidationService()
