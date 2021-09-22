<img align="right" src="https://notion-emojis.s3-us-west-2.amazonaws.com/v0/svg-twitter/1f40d.svg" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="200" height="400" />

## **Technical task in Python for PixelField**

Made by **Denis Krepak**

## **Project Descrtiption**

### **English Brief** - [PixelField Junior Python Task](https://pebble-lily-5a3.notion.site/PixelField-Junior-Technical-Task-Eng-67ae46c4621a445790c5816836eed38d)

### **Russian Brief** - [PixelField Junior Python Task](https://pebble-lily-5a3.notion.site/PixelField-Junior-Technical-Task-Rus-32e6e3534ee44854b1236b1c4558f1f6)

Wrote on **Python** using **Django**, **Django Rest Framework**. **PostgreSQL** is used as a **DBMS**

## **Deployment on a local machine**
1. Connect to PostgreSQL:
```
psql -U postgres
```
Create DB with nane "pftaskdb":
```
CREATE DATABASE pftaskdb;
```
Connect to new DB:
```
\c pftaskdb;
```
2. Clone the repository:
```
git clone https://github.com/dvkrepak/pixelfieldtask.git
```
3. Create virtual environment with name "venv":
```
python3 -m venv venv
```
Activating venv:
```
source venv/bin/activate
```
4. Go to the folder with app:
```
cd pixelfieldtask/
```
5. Installing all packages from requirements.txt:
```
pip install -r requirements.txt
```
6. Make migrations:
```
python manage.py makemigrations && python manage.py migrate
```
7. Create superuser:
```
python manage.py createsuperuser
```
8. Launch project:
```
python manage.py runserver
```
9. Fill the DB(optional):
```
python manage.py loaddata blog/fixtures/categorydata.json
python manage.py loaddata blog/fixtures/tagdata.json
python manage.py loaddata blog/fixtures/userdata.json
python manage.py loaddata blog/fixtures/postdata.json
```

Project will be available at **http://127.0.0.1:8000/**

## **Views:**
#### **localhost/login/** - classic DRF authorization
#### **localhost/posts/** - list of posts
#### **localhost/post/post_slug/** - detail post view
#### **localhost/categories/** - list of categories
#### **localhost/tags/** - list of tags
#### **localhost/authors/** - list of authors
