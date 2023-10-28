from pydantic import BaseModel

class Suscription(BaseModel):
    name: str
    value: str
    time: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "normal",
                    "value": "100,000",
                    "time": "1 mes",
                }
            ]
        }
    }