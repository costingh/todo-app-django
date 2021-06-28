# todo-app-django

A todo app built with django

![First screen](https://github.com/costingh/todo-app-django/blob/master/1.png?raw=true)

![First screen](https://github.com/costingh/todo-app-django/blob/master/2.png?raw=true)

## Description

The app allows to the user to create, read, update and delete todos. The app offers some categories to user, like: music, travel, work, home, study, others, all, etc.
The user can add tasks in each of this categories.

## Dark-mode

The app has light/dark mode implemented. To achieve this, the local storage was used.

## Tech-stack:
* HTML
* CSS
* Python
* JavaScript

## Database

As database, sqlite one is used.

### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
$ git clone https://github.com/costingh/todo-app-django.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory 

```bash
$ cd todo-app-django
```

And run the following command

```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command

```bash
$ python manage.py migrate
```

One last step. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

```bash
$ python manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/ for the App.
