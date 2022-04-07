# Fazla Gıda Challenge

## How to run
1. Clone the project
2. Create and activate virtual environment

        python -m venv venv
        source venv/bin/activate (Unix)
       .\venv\Scripts\activate.bat (Windows)
3. Install dependencies

        pip install -r requirements.txt
4. Initialize the database
   1. With postgresql command line tool
   
           psql postgres
           create database fazla_gida with owner postgres;
           \c fazla_gida
           \i initialize.sql
   2. With django's manage.py, provided you created a database named fazla_gida
      
          python manage.py makemigrations
          python manage.py migrate
        
5. Run the server

        python manage.py runserver

> To access the admin panel of django we need to create a super user:
>   
>       python manage.py createsuperuser



## API

BASE_URL: http://localhost:8000/rest/favorites 

Type = (Store, Product)
#### GET
**Inputs:** id: int, type: Enum

**Outputs:** 200: Object of given type, 40x: Relevant error message

#### DELETE
**Inputs:** id: int, type: Enum

**Outputs:** 200: OK, 40x: Relevant error message


## Structure Overview
- **Models**  
  Describe the database tables using django orm.
- **Services**  
  Contain the business logic
- **Views**  
    Map the business logic to certain views. Any filtering operation for display purposes would also belong here.
- **Templates**  
    Html templates of the project.

