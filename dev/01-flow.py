from asyncio import tasks
import prefect
import json
import os
import random

from prefect.triggers import all_successful, all_failed
from prefect import task, Flow

"""
f = open("config.json")
prefect_dev_key = json.load(f)["keys"]["prefect_dev"]

os.system(
    "prefect agent local start --api https://api.prefect.io --key prefect_dev_key"
)
"""


@task(name="task1")
def task1():
    os.system(r"mkdir C:\Users\sivan\Documents\task1")
    logger = prefect.context.get("logger")
    logger.info("task1")


@task(name="task2", trigger=all_successful)
def task2():
    os.system(r"mkdir C:\Users\sivan\Documents\task2")
    logger = prefect.context.get("logger")
    logger.info("task2")


@task(name="task3", trigger=all_failed)
def task3():
    os.system(r"mkdir C:\Users\sivan\Documents\task3 ")
    logger = prefect.context.get("logger")
    logger.info("task3")


with Flow("01-flow") as flow:
    success = task2(upstream_tasks=[task1])
    failed = task3(upstream_tasks=[task1])
flow.set_reference_tasks([success])
flow.register(project_name="dev")
# flow.run()
