from celery_app import task1

task1.add.delay(2,4)
print('end')