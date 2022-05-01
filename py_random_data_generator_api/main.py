from fastapi import FastAPI

from routers import random, deterministic

api_description = """
The Random Data Generator API is a tool that creates random datasets around four themes:

- mock user data
- mock sensitive user account data
- mock transaction data
- mock log data

For the course being built, this API allowed students to make requests for data using `curl` or `wget` and then practice searching and transforming the data with `grep` and `sed`.

However, the data can be used however you want, it's just random data.

## Usage

Make **GET** requests to the API to request a data set. Each endpoint can be configured with one optional query parameter:

- **data_format**: the format of the response body

The **data_format** query parameter defaults to `json` and can only be changed to `csv`.

Additionally, the `/random` endpoints can be configured with the optional query parameter:

- **amount**: the number of random data to be included in the response body

The **amount** query parameter defaults to 10, and is capped at 500.

## Pre Generated Data

There is one dataset per category that is pre-generated and includes 50000 records. You can access these at the base path: `api/deterministic`. This was a necessary inclusion for our class to give students large deterministic data sets so we could give them specific problems and would **know** the answers.

## Warning

**DO NOT EXECUTE THE `/deterministic` endpoints from the OpenAPI docs you are currently viewing**. 

It will crash your web browser as it attempts to load all **50000** records in this UI. Instead make the request with `curl`, or `postman`, or you know any of the million HTTP request libraries.

The `/random` endpoints are all safe to consume from the docs you are viewing, but larger datasets will take longer to load and could possible crash based on your personal machine.
"""

tags_metadata = [
    {
        "name": "random",
        "description": "Randomly generated datasets between **1 and 500** records."
    },
    {
        "name": "deterministic",
        "description": "Deterministic datasets containing exactly **50000** records."
    }
]

app = FastAPI(
    openapi_url = "/api/openapi.json",
    docs_url = "/api/docs",
    redoc_url = "/api/redoc",
    title = "Random Data Generator API",
    description = api_description,
    contact = {
        "name": "Paul Matthews",
        "url": "https://paulmatthews.dev",
        "email": "paul@paulmatthews.dev"
    }    
)

app.include_router(random.router)
app.include_router(deterministic.router)
