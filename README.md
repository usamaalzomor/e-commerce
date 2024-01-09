# E-commerce API
This API serves as the backend for an e-commerce application. It provides endpoints for managing orders, products, images, and reviews, and it's secured with JSON Web Token (JWT) authentication.

> Live demo [_here_](https://e-commerce-production-5fdc.up.railway.app/). 

## Table of Contents
* [Walkthrough and Usage Guide](#walkthrough-and-usage-guide)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
  * [Standard Setup](#standard-setup)
  * [Docker compose Setup](#docker-compose-setup)
* [Testing](#testing)
* [Authentication](#authentication)
* [API Documentation](#api-documentaion)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->

## Walkthrough and Usage Guide

   [<img src="https://img.youtube.com/vi/DVOPrgHvg4I/hqdefault.jpg" width="500" height="300" />](https://www.youtube.com/embed/DVOPrgHvg4I) 

## Technologies Used
- Django 5.0.1
- Django REST Framework 0.1.0
- MySQL 8.0.35
- Celery 5.3.6
- Redis 5.0.1
- Docker 7.0.0

> You can find dependencies full list inside the `Pipfile`.

## Setup

### Standard Setup:
#### Prerequisites:
* Python 3.10 or later
* Pipenv 
* MySQL
* Docker (needed for running redis server)
  
#### Steps:
1. Clone the repository:
   ```
   git clone https://github.com/usamaalzomor/e-commerce.git
   cd e-commerce
   ```

2. Install dependencies using Pipenv:
   ```
   pipenv install --dev
   ```
3. Activate your virtual environment `pipenv shell`.

4. Set the python interpreter attached to your new virtual environment at your code editor. 

5. Configure the database settings 
   * Create DATABASE with name and password of your choosen.
   * Edit `NAME`, `USER` and `PASSWORD` keys at `DATABASE` dict in the `settings/dev.py` for proper database connection.
   
6. Apply database migrations:
   ```
   python manage.py migrate
   ```

7. Start the Django development server:
   ```
   python manage.py runserver
   ```

8. start redis server using docker image:
   ```
   docker run -d -p 6379:6379 redis
   ```

9. In a separate terminal, run Celery for background task processing:
   ```
   celery -A ecommerce worker --loglevel=info
   ```

10. In another separate terminal, run Celery Beat for periodic tasks:
    ```
    celery -A ecommerce beat --loglevel=info
    ```
   
11. Create super user:
    ```
    python manage.py createsuperuser
    ```
12. Populate you database with sample data:
    ```
    python manage.py seed_db
    ```
  The application will be available on http://localhost:8000/.

#### Notes:
- Ensure MySQL and Redis servers are running and accessible.
- Update Django settings in `settings/dev.py` to match you database .
- If you want to monitor Celery tasks using Flower, run the following command in a separate terminal:
  `celery -A ecommerce flower`
    Access Flower's web interface at http://localhost:5555.

- For development purposes, you can use SMTP4Dev to catch and view emails. Run the following command:
  `docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev`

    Access SMTP4Dev's web interface at http://localhost:3000.



### Docker Compose Setup:

#### Prerequisites:
* Docker
* Docker-compose
  
#### Steps:
1. Clone the repository:
   ```
   git clone https://github.com/usamaalzomor/e-commerce.git
   cd e-commerce
   ```

2. Swich to the docker-dev branch:
   ```
   git checkout docker-dev
   ```
3. Configure the database:
   * Create DATABASE with name and password of your choosen.
   * In the `settings/dev.py` alter `NAME`, `USER` and `PASSWORD` keys inside `DATABASE` dict for porper database connection. 
   * In the `docker-compose.yml` alter `MYSQL_DATABASE` and `MYSQL_ROOT_PASSWORD` for proper database connection.
     
5. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

6. create super user:
   ```
   docker-compose run web python manage.py createsuperuser
   ```

7. Populate you database with sample data:
    ```
    docker-compose run web python manage.py seed_db
    ```
    
The application will be available on http://localhost:8000/

#### Notes:
- If you are running local MySQL service on localhost and port 3306, please ensure to stop it before starting your Docker Compose setup.
- Access Flower's web interface at http://localhost:5555.
- Access SMTP4Dev's web interface at http://localhost:5000.


## Testing
- Apply all created test cases:
    ```
    pytest
    ```
- Apply continuous testing:
    ```
    ptw
    ```

   
## API Documentaion
Explore the API's endpoints:

   * API Documentation [(Swagger)](https://e-commerce-production-5fdc.up.railway.app/api/schema/swagger-ui/)
   * API Documentation [(Redoc)](https://e-commerce-production-5fdc.up.railway.app/api/schema/redoc/)
   * You can access the api documentation at your local after installation at these urls: http://localhost:8000/api/schema/swagger-ui/ , http://localhost:8000/api/schema/redoc/

## Authentication
- This API uses JWT authentication. Include the JWT token in the Authorization header with the prefix "JWT" when making authenticated requests.

#### Authentication Endpoints:

* Create JWT Token Endpoint -> /auth/jwt/create/ (POST)

     * Description: Takes user credentials and returns an access and refresh JSON web token pair for authentication (superuser credentials needed)

     * Request Body:
   
        `
        json:
        {
          "username": "your_username",
          "password": "your_password"
        }`
        
     * Response:
      HTTP 200 OK
      
       `json:
       {
         "access": "your_access_token",
         "refresh": "your_refresh_token"
       }`

## Project Status
Project is: _complete_.


## Acknowledgements
- This project was based on [The Ultimate Django Series Course](https://codewithmosh.com/p/the-ultimate-django-series).


## Contact
Created by [Usama Alzomor](https://www.linkedin.com/in/usama-alzomor/)- feel free to contact me!
