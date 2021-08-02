# GreatKart
## An Ecommerece Store

![Screenshot from 2021-08-02 16-45-25](https://user-images.githubusercontent.com/49125971/127854127-7c02ae0f-ac36-43b0-96fc-2ae475b954cd.png)


## Features:
    * Two Factor Authenticaton
    * Payment-gateway Integration
    * Cart functionality
    * Variation of products
    * Inovice Generation and delivery
    * Frontend for PC and Mobile use
    * Dynamic backend:
              * Add/Remove Products,Categories,Variations
              * Item stock
              * View Orders and Payments
	

## Security Mesures
    * User verification
    * HoneyPot to track unauthoried activity
    * Mail Encryption
    * Session Timeout on Inactivity
    * Hashing and salting Password for storage
    * User/Admin Account Permissoins


## Tech Stack

### Backend
	   * Django
	   * sqlite3
	   * smtp.gmail
	   * Paypal API

### Frontend 
	   * Bootstrap
	   * CSS


### Instructions
1. Change working directory to this directory.
2. Chane directory of static files in ./greatkart/settings.py
3. Run the server using "python manage.py runserver"
4. By default server runs on port 8000
5. To change pass port number in 2.
6. To access admin panel use ~/adminsk
7. Honeypot at path ~/admin

### Requirements
* asgiref==3.2.10
* certifi==2021.5.30
* charset-normalizer==2.0.3
* Django==3.1
* django-admin-honeypot==1.1.0
* django-session-timeout==0.1.0
* idna==3.2
* Pillow==8.3.1
* psycopg2-binary==2.9.1
* python-decouple==3.4
* pytz==2021.1
* requests==2.26.0
* six==1.16.0
* sqlparse==0.4.1
* urllib3==1.26.6

## Contributor
 Saksham Kapoor
