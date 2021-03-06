<p align="center">
<img src="/static/images/icon.png" height=100 width=100/>
</p>

<h3 align='center'>Programming Club Website</h3>

<p align='center'>
    This website was build under a competition organised by the Programming Club of School of Engineering and Applied Science (SEAS), Ahmedabad University (AU) 
</p>

-------------

<h3>Table of Contents</h3>

* [About The Project](#about-the-project)
  * [Build with](#build-with)
  * [Database Used](#database-used)
* [Getting Started](#getting-started)
  * [Installation](#installation)
  * [Dependencies](#dependencies)
* [Usage](#usage)
* [Contributing](#contributing)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)


<br>

### About The Project

#### Build With

* Django
* JavaScript
* HTML
* CSS/SCSS
* Bootstrap
* JQuery

#### Database Used

* [PostgreSQL](https://www.postgresql.org/) (To install postgres click on it)


<br>

### Getting Started

#### Installation

* Clone

  ````bash
  git clone https://github.com/NamitS27/PClub-Website.git
  ````

* Database (If you are using Postgres)

  * Settings.py code 
  ```python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'USER': '<new_user>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '',
    }
  }
  ```

  * Creating the databse
    ```sql
    CREATE DATABASE <database_name>;
    ```
  * Creating a user for the database
    ```sql
    CREATE USER <new_user> WITH PASSWORD '<password>';
    ```
  * Altering roles for timezones,encoding and default transaction isolation
    ```sql
    ALTER ROLE <new_user> SET client_encoding TO 'utf8';
    ALTER ROLE <new_user> SET default_transaction_isolation TO 'read committed';
    ALTER ROLE <new_user> SET timezone TO '<timezone>';
    ```

* Project
  * Creating Virtual Environment 
    ```sh
    virtualvenv myvenv
    ```
  * Install the required packages to run the project
    ````sh
    pip install requirements.txt
    ````

  * Following are the commands to create the tables
    ```sh
    python manage.py makemigrations
    ``` 
    * If the above part doesn't work, do makemigrations for all the apps individually
    ```sh
    python manage.py makemigrations <app_name>
    ```
    ```
    python manage.py migrate
    ````
  * Create Super User for the Admin Panel (Enter username/password as per your wish)
    ```sh
    python manage.py createsuperuser
    ```
  * Final command to run the server
    ```sh
    python manage.py runserver
    ```

#### Dependencies 

* CSS
  * [https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css)
  * [https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css](https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css)
  * [https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css](https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css)


* JavaScript
  * [https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js](https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js)
  * [https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TweenMax.min.js](https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TweenMax.min.js)
  * [https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js](https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js)
  * [https://cdnjs.cloudflare.com/ajax/libs/jquery.touchswipe/1.6.4/jquery.touchSwipe.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery.touchswipe/1.6.4/jquery.touchSwipe.min.js)
  * [https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js](https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js)



<br>

### Usage

Any educational institutions who wants a website to showcase the activities done by the club. 


<br>

### Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

   
<br>

### Authors

* [Suhanee Patel](https://github.com/sp2605)
* [Namit Shah](https://github.com/NamitS27)

<br>

### Acknowledgements

* [Codeforces API](https://codeforces.com/apiHelp)
* [Contest API by Clist](https://clist.by/)
* [Font Awsome](https://fontawesome.com)
* [JQuery for Countdown](http://hilios.github.io/jQuery.countdown/)
* [Email verification API](https://isitarealemail.com/)
* [Particle.js](https://github.com/VincentGarreau/particles.js/)


