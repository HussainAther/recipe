# Recipe Management

Calling all cook enthusiasts! Create and add your own recipes. 

It's recommended to use this app in a virtual environment. One can be made, for example, with:

```
python3 -m venv env
```

and activated with

Windows: 
```
env\Scripts\activate
```

Mac: 
```
source env/bin/activate
```

Set the 'postgresql://username:password@hostname/database' in app.config['SQLALCHEMY_DATABASE_URI'] to your actual PostgreSQL database connection URL. 

Replace username, password, hostname, and database with your database credentials and details. For example:

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myusername:mypassword@localhost/mydatabase'

Make sure you've set the Flask app environment variable in your terminal. 

* For Windows (PowerShell): $env:FLASK_APP = "app"
* For macOS/Linux: export FLASK_APP=app

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
    * static/: This directory is used for static files like CSS, JavaScript, and images.
        * css/: This directory contains CSS files. You can place your styles.css file here.
    * templates/: This directory contains HTML template files for your views.
        * base.html: This is the base template that other templates can extend.
        * register.html: This is the template for the user registration page.
        * login.html: This is the template for the login page.

    * __init__.py: This is the initialization file for the Flask application.
    * models.py: This file contains the model classes for your database tables.
    * routes.py: This file contains the route definitions and view functions for your application.
    * helpers.py: This file contains your helper functions for common tasks.
    * config.py: This file contains your configuration variables.
    * requirements.txt: This file lists the Python packages required by your app.
    * run.py: This file is used to run your Flask application.

## Testing with Insomnia REST API:

1. Download and install Insomnia, a popular REST API client, from their official website: https://insomnia.rest/
* Set Up Insomnia Workspace:

2. Launch Insomnia and create a new workspace for your project.
* Organize your API endpoints into folders for better organization.

3. Create Requests:
* Create requests for various CRUD operations like creating, retrieving, updating, and deleting recipes.
* Set the HTTP method, URL, request headers, and body (if required) for each request.
* Add necessary authentication headers or tokens for protected routes.
* Send Requests and Verify Responses:

4. Send the requests to your Flask app's API endpoints and observe the responses.
* Verify that the responses match the expected behavior according to your API specifications.
* Insomnia will provide detailed response information, including headers, status codes, and response bodies.


## Testing with ElephantSQL:

Visit the ElephantSQL website: https://www.elephantsql.com/

1. Sign up for a free account or choose a suitable plan depending on your needs.
* Follow their instructions to create a new PostgreSQL database instance.

2. Obtain Database Connection Details:
* Once your database instance is set up, you'll receive connection details such as the database URL, username, password, etc.
* Note down this information as you'll need it to connect your Flask app to the ElephantSQL database.

3. Configure Flask App for ElephantSQL:
* Update your Flask app's configuration to use the ElephantSQL database.
* Use the provided connection details to set up the database connection string or URL.
* Update your model classes or database configuration to match the ElephantSQL database schema.

4. Test Database Operations:
* Run your Flask app and test the CRUD operations against the ElephantSQL database.
* Verify that data is being created, retrieved, updated, and deleted as expected.
* Inspect the database directly using tools like pgAdmin or connect to it via command-line tools to confirm the changes.

## Troubleshooting
If you run into issues, you could try changing the file versions on packages such as

```
pip install psycopg3
```

for Mac. 
