import prefect
from prefect import task, Flow


@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")


flow = Flow("hello-world", tasks=[hello_task])
flow.register(project_name="dev")
# flow.run()
