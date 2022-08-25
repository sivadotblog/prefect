from asyncio import tasks
import prefect
from prefect import task, Flow
import json
import os

f = open("config.json")
prefect_dev_key = json.load(f)["keys"]["prefect_dev"]
print(prefect_dev_key)

os.system("prefect auth login --key " + prefect_dev_key)

os.system("prefect agent local start")
