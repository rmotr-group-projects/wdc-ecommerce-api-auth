<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Ecommerce Authentication, Permissions and Pagination

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3) ecommerce
$ pip install -r requirements.txt
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

### Description

The main goal of this project is to practice all the concepts related with Authentication and Permissions, and learn how you can easily deal with them using Django REST Framework.

We'll make use of the Ecommerce project that we've been working on, and add authentication and permission layers to all the endpoints related with `Product` model.


### Your tasks

All the tasks will be focused on Authentication, Permissions and Pagination. Description for each task are divided into different parts below.

Make sure to check the tests inside `api/tests.py`. Those are the ones that have to pass in order to consider the project finished.

Execute the following line in your command line to run the tests:

```bash
$ make test
```

##### PART 1 - Authentication:

For this first part you'll have to add three different types of authentication methods:

- Basic Authentication
- Token Authentication
- Custom Authentication

Basic and Token auth are standard methods that are already implemented by DRF. Make sure to configure them properly inside `ecommerce/settings.py`.

For Custom authentication, one of the most commonly use cases is to have an API Client with accesskey and secretkey credentials. You can find the `APIClient` model inside `api/models.py`.

You'll find more hints about this task inside `api/authentication.py`, which is the module you have to work on.


##### PART 2 - Permissions:

This part will include the usage of some permissions implemented by DRF, and some other custom permissions that you'll have to implement yourself (both view level and object level permissions).

The conditions that must be satisfied are the following ones:

- All endpoints will require the user to be authenticated (see `IsAuthenticated` permission from DRF) and not being a hacker (see `IsNotHacker` permission inside `api/permissions.py`)

- All endpoints that modify the database will require the user to be admin (see `IsAdminUser` permission from DRF). This endpoints are the create, update, partial update and delete.

- The retrieve endpoint will need the user to pass the `IsOddProductID` permission (must also be implemented inside `api/permissions.py`)


##### PART 3 - Pagination:

Changing the way that the JSON response is formatted is pretty simple while using DRF.

For this task you'll have to configure the DRF settings inside `ecommerce/settings.py` in order to have `PageNumberPagination` as default pagination class, and a page size of 3 products for each page.
