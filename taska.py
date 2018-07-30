from celery import Celery

app = Celery('taska', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test() every 10 seconds.
    sender.add_periodic_task(5.0, test.s(), name='add every 10')


@app.task
def test():
    return 8/2
