[![Build Status](https://travis-ci.org/Anonymike/APIum.svg?branch=master)](https://travis-ci.org/Anonymike/APIum)
=====
APIum
=====
Api·um : a genus of Eurasian herbs of the carrot family that includes celery


A simple task runner using flask and celery.

Installing with Docker
----------------------
Install [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04) and [Docker Compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04).


cd into the top apium directory and run:

```
  $ sudo docker-compose build
  $ sudo docker-compose up
```

This will launch 3 containers and look something like this:

```
$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
fb9c252fdfdd        apium_celery        "python runcelery...."   5 hours ago         Up 8 seconds                                 apium_celery_1
921fd0b853dc        apium_app           "python manage.py ..."   5 hours ago         Up 8 seconds                                 apium_app_1
0c5abc7285a0        redis               "docker-entrypoint..."   8 hours ago         Up 8 seconds        0.0.0.0:6379->6379/tcp   apium_redis_1
```

Installation without Docker
---------------------------
Sometimes it's helpful to run applications manually for testing, filling a large monitor with terminal windows, or running the application in a distributed manner.

#### Install Redis
Celery uses Redis as a queue for job tracking. To install Redis run the installation script in the parent directory.


**NOTE**: This is a very basic installation lacking configuration and security. You should check out [redis'](https://redis.io/) website for best practices.
 ```
 $ sudo ./install_redis.sh
 ```


 #### Install dependencies
 ```
 $ pip install -r requirements.txt
 ```

  #### Run!
  Redis must be installed and running before starting the flask server or celery worker.
  ```
  $ make server
  $ make celery
  ```


Configuration
-------------
You can define configuration variables by including a .env file. However, this is setup to run out of the box.

Usage
-----
To run parallel tasks on the backend simply add them to apium/tasks/jobs.py and add calling function in apium/tasks/controllers.py.
