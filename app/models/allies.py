from pydantic import BaseModel

class Ally(BaseModel):
    dni: str
    full_name: str
    phone: str
    commerce_name: str
    mail: str
    commerce_type: str
    suscription: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "dni": "123456789",
                    "full_name": "John Doe",
                    "phone": "555-555-5555",
                    "commerce_name": "Example Store",
                    "mail": "john@example.com",
                    "commerce_type": "Retail",
                    "suscription": 1,
                }
            ]
        }
    }