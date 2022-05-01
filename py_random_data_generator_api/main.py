from os import remove
from random import randint

from fastapi import FastAPI
from fastapi.responses import FileResponse

from starlette.background import BackgroundTask

from py_random_data_generator.py_random_data_generator.generate_random import get_users_list, get_sensitive_users_list, get_transactions_list, get_logs_list
from py_random_data_generator.py_random_data_generator.random_writer import write_dict_list_to_csv

app = FastAPI()

def remove_file(path):
    remove(path)

@app.get("/random/users")
async def get_data_user(data_format="json", amount=10):
    if data_format == "csv":
        filepath = "csvs/temp/{}random-data.csv".format(randint(1000,1000000))
        write_dict_list_to_csv(filepath, get_users_list(int(amount)))
        remove_task = BackgroundTask(remove_file, path=filepath)
        return FileResponse(filepath, filename="random-users.csv", background=remove_task)
    return get_users_list(int(amount))

@app.get("/random/sensitive")
async def get_data_sensitive(data_format="json", amount=10):
    if data_format == "csv":
        filepath = "csvs/temp/{}random-data.csv".format(randint(1000,1000000))
        write_dict_list_to_csv(filepath, get_sensitive_users_list(int(amount)))
        remove_task = BackgroundTask(remove_file, path=filepath)
        return FileResponse(filepath, filename="random-sensitive.csv", background=remove_task)
    return get_sensitive_users_list(int(amount))

@app.get("/random/transactions")
async def get_transaction(data_format="json", amount=10):
    if data_format == "csv":
        filepath = "csvs/temp/{}random-data.csv".format(randint(1000,1000000))
        write_dict_list_to_csv(filepath, get_transactions_list(int(amount)))
        remove_task = BackgroundTask(remove_file, path=filepath)
        return FileResponse(filepath, filename="random-transactions.csv", background=remove_task)
    return get_transactions_list(int(amount))

@app.get("/random/logs")
async def get_logs(data_format="json", amount=10):
    if data_format == "csv":
        filepath = "csvs/temp/{}random-data.csv".format(randint(1000,1000000))
        write_dict_list_to_csv(filepath, get_logs_list(int(amount)))
        remove_task = BackgroundTask(remove_file, path=filepath)
        return FileResponse(filepath, filename="random-logs.csv", background=remove_task)
    return get_logs_list(int(amount))
