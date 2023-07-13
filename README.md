# Selenium-Django-Celery-RabbitMQ-MySQL Demo

- This repo includes a demo of resource-manageable Selenium web scraping tasks.
    - See the test.log file for more information.
- You can fully containerize the project as needed by modifying the `docker-compose.yml` file. There are a number of examples on the web.
- I hope this demo helps people starting out. Cheers!

## How to run the project

1. Set up the environment.
2. Launch the containers using the `docker-compose.yml` file.

Here are some essential commands:

```
docker-compose up # to launch the containers
docker-compose down # to stop the containers
docker-compose down -v # to delete the volumes with the containers.
```

3. Log in to MySQL server as root user to set up databases and privileges.

```
CREATE DATABASE manager;
CREATE DATABASE news_scraper;
GRANT ALL ON manager.* TO 'jake';
GRANT ALL ON news_scraper.* TO 'jake';
```

4. Open up a new terminal and run the following command to create database migrations:

```
python manage.py makemigrations && python manage.py migrate && python manage.py migrate --database=news_scraper news_scraper
```

5. Launch the Django server:

```
python manage.py runserver
```

6. Open up another new terminal and run the following command to ready the task workers:
    - Make sure to adjust the auto-scale settings to avoid resource problems.

```
celery -A manager worker -l INFO --autoscale=2,4 --without-heartbeat --without-gossip --without-mingle
```

7. Open up another new terminal and run the following command to cue the task workers for the schedule:

```
celery -A manager beat -l INFO
```

Once you have completed these steps, the project should be up and running.
