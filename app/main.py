from fastapi import FastAPI, status
from pydantic import BaseModel
import MySQLdb

app = FastAPI()


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


# Create the connection object
connection = MySQLdb.connect(
    host="db",
    user="admin",
    password="admin",
    db="mydatabase",
)
# Create cursor
cursor = connection.cursor()


@app.get("/")
async def root():
    return {"message": "Hola mundo"}


@app.get("/allys")
async def get_allys():
    # SQL statement to select all records from the "allys" table
    sql = "SELECT * FROM Allys"

    try:
        cursor.execute(sql)
        allies = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]  # Get column names

        # Convert the result to a list of dictionaries with column names as keys
        allies_list = [dict(zip(column_names, ally)) for ally in allies]

        return {"allies": allies_list}
    except Exception as e:
        return {"Error": str(e)}


@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(ally: Ally):
    # SQL statement with placeholders (%s)
    sql = "INSERT INTO Allys (dni, full_name, phone, commerce_name, mail, commerce_type, suscription) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    try:
        cursor.execute(
            sql,
            (
                str(ally.dni),
                str(ally.full_name),
                str(ally.phone),
                str(ally.commerce_name),
                str(ally.mail),
                str(ally.commerce_type),
                int(ally.suscription),
            ),
        )
        new = dict(ally)
        new["id"] = cursor.lastrowid
        print(new)
        connection.commit()  # Commit the changes to the database
        return {"Successful": new}
    except Exception as e:
        return {"Error": str(e)}


@app.get("/suscription")
async def get_allys():
    # SQL statement to select all records from the "suscriptions" table
    sql = "SELECT * FROM Suscriptions"

    try:
        cursor.execute(sql)
        allies = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]  # Get column names

        # Convert the result to a list of dictionaries with column names as keys
        allies_list = [dict(zip(column_names, ally)) for ally in allies]

        return {"suscriptions": allies_list}
    except Exception as e:
        return {"Error": str(e)}


@app.post("/suscription", status_code=status.HTTP_201_CREATED)
async def register(suscription: Suscription):
    # SQL statement with placeholders (%s)
    sql = "INSERT INTO Suscriptions (name, value, time) VALUES (%s, %s, %s)"

    try:
        cursor.execute(
            sql,
            (
                str(suscription.name),
                str(suscription.value),
                str(suscription.time),
            ),
        )
        new = dict(suscription)
        new["id"] = cursor.lastrowid
        print(new)
        connection.commit()  # Commit the changes to the database
        return {"Successful": new}
    except Exception as e:
        return {"Error": str(e)}
