# empapicrud
============

Procedure to create the project in Django with Postgres and RESTAPI:
=============================


1: Create Virtual Machine

python -m venv empapi   

C:\Users\ganes\Django-RESTAPI\empapi-crud>python -m venv empapi
 

3: Activate the virtual Machine 

.\empapi\scripts\activate

C:\Users\ganes\Django-RESTAPI\empapi-crud>.\empapi\scripts\activate
   

4: Install Django 

py -m pip install Django     

(empapi) C:\Users\ganes\Django-RESTAPI\empapi-crud>py -m pip install Django


6:  Create Folder

django-admin empapicrud

(empapi) C:\Users\ganes\Django-RESTAPI\empapi-crud>django-admin empapicrud


7: Create Project

django-admin startproject empapicrud

(empapi) C:\Users\ganes\Django-RESTAPI\empapi-crud>django-admin startproject empapicrud


8: Enter into project

cd empapicrud                        

(empapi) C:\Users\ganes\Django-RESTAPI\empapi-crud>cd empapicrud



9: Enter into Visual Studio through command prompt 

code .                               ==> to open visualstudio

(empapi) C:\Users\ganes\Django-RESTAPI\empapi-crud\empapicrud>code .


10: History command to check the flow 

press F7 to get the history of commands used


11. in Visual code, open terminal and create app,

PS C:\Users\ganes\Django-RESTAPI\empapi-crud\empapicrud> python manage.py startapp employeeapi


12. Update employeeapi -app name in setting.py(under empapicrud project)



13. Install django rest api framework

pip install djangorestframework


14 update setting.py with rest_framework ,

Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employeeapi', 
    'rest_framework',
]

15. install postgresql,

pip install psycopg2
	
	
16. create dtabase   restfulapiDB in pgAdmin

17. update sql details in settings.py,


DATABASES = {

	'default': {
        
	'ENGINE': 'django.db.backends.postgresql',
        
	'NAME': 'restfulapiDB',
        
	'USERNAME': 'postgres',
        
	'PASSWORD': 'postgres',
        
	'HOST':'localhost'
    
    }
    
}


18. in order to do the models, run python manage.py migrate , if you face fail error like user ganes doestnt exitst follow below steps,


type psql in start menu and create user and database,

postgres=# CREATE USER ganes WITH PASSWORD '19821983';

CREATE ROLE


postgres=# CREATE DATABASE restfulapiDB WITH OWNER ganes ENCODING 'utf-8';

CREATE DATABASE



19. 10 tables are created in postgres under restfulapidb, 


20 Creating employee table strutucre under models.py(employeeapi),

	class Employee(models.Model):
		
		EmployeeId   = models.CharField(max_length=4)
		
		EmployeeName =models.CharField(max_length=1000)
		
		EmployeeDesignation = models.CharField(max_length=1000)
		
		EmployeeSalary= models.CharField(max_length=10)
		
		EmployeeMobile = models.CharField(max_length=12)

21 python manage.py makemigrations employeeapi
		
		PS C:\Users\ganes\Django-RESTAPI\empapi-crud\empapicrud> python manage.py makemigrations employeeapi
		
		Migrations for 'employeeapi':
		
		employeeapi\migrations\0001_initial.py
		
		- Create model Employee
						

22 python manage.py migrate

23 python manage.py runserver  to run
