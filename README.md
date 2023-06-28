# Recipe Management

Create and add your own recipes. 

Set the 'postgresql://username:password@hostname/database' in app.config['SQLALCHEMY_DATABASE_URI'] to your actual PostgreSQL database connection URL. Replace username, password, hostname, and database with your database credentials and details. For example:

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myusername:mypassword@localhost/mydatabase'

```
recipe/
    ├── static/
    │   ├── css/
    │   │   └── styles.css
    ├── templates/
    │   ├── base.html
    │   ├── register.html
    │   └── login.html
    ├── app.py
    ├── models.py
    ├── helpers.py
    ├── config.py
    ├── requirements.txt
    └── run.py
```

Here's a breakdown of the structure:

* app/: This directory contains the main application logic.
** static/: This directory is used for static files like CSS, JavaScript, and images.
*** css/: This directory contains CSS files. You can place your styles.css file here.
** templates/: This directory contains HTML template files for your views.
*** base.html: This is the base template that other templates can extend.
*** register.html: This is the template for the user registration page.
*** login.html: This is the template for the login page.
***__init__.py: This is the initialization file for the Flask application.
*** models.py: This file contains the model classes for your database tables.
*** routes.py: This file contains the route definitions and view functions for your application.
*** helpers.py: This file contains your helper functions for common tasks.
** config.py: This file contains your configuration variables.
** requirements.txt: This file lists the Python packages required by your app.
** run.py: This file is used to run your Flask application.



