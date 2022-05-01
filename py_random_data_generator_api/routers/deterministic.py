from csv import DictReader

from fastapi import APIRouter

from fastapi.responses import FileResponse

def unpack_csv_file(csv_filepath):
    data = []
    with open(csv_filepath, 'r') as csvfile:
        some_reader = DictReader(csvfile)
        for row in some_reader:
            data.append(row)
    return data

router = APIRouter(prefix="/deterministic")

@router.get("/users")
async def get_data_user(data_format="json", amount=10):
    filepath = "csvs/deterministic/users.csv"
    if data_format == "csv":
        return FileResponse(filepath, filename="users.csv")
    return unpack_csv_file(filepath)

@router.get("/sensitive")
async def get_data_sensitive(data_format="json", amount=10):
    filepath = "csvs/deterministic/sensitive.csv"
    if data_format == "csv":
        return FileResponse(filepath, filename="sensitive.csv")
    return unpack_csv_file(filepath)

@router.get("/transactions")
async def get_transaction(data_format="json", amount=10):
    filepath = "csvs/deterministic/transactions.csv"
    if data_format == "csv":
        return FileResponse(filepath, filename="transactions.csv")
    return unpack_csv_file(filepath)

@router.get("/logs")
async def get_logs(data_format="json", amount=10):
    filepath = "csvs/deterministic/logs.csv"
    if data_format == "csv":
        return FileResponse(filepath, filename="logs.csv")
    return unpack_csv_file(filepath)
