## How to run this project
### 1. Clone the project
 ```
 git clone https://github.com/SodokinMarius/todo-list-api.git

 
 cd todo-list-api
 ```

### 2. Creating the  virtuel environnement 
```
 virtualenv venv or python3 -m venv venv

 source venv/bin/activate
```

### 3. Installing the project requirements /dependencies
```
pip install -r requirements.txt
```

## 4. The project is built with docker.You have the choice to run it, Then make sure that docker is 
## installed on your computer

```
consult the doc here
https://docs.docker.com/get-started/
```

### 5. Creating a virtual container (Make sure that docker service is running on your computer)
```
sudo docker-compose up -d --build
```

### 6. Migrations executions 
```
sudo docker-compose exec todo python3 manage.py makemigrations
sudo docker-compose exec todo python3 manage.py migrate
```
### without docker 
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### 7. Running the project (with docker)
```
sudo docker-compose exec todo python3 manage.py runserver or
sudo docker-compose exec todo python manage.py runserver


```
### without docker 
```
python3 manage.py runserver
```
