# CIS Task
## Python 3.10.8
## to get django base files path in your PC
 - you should active your venv
 - run this command : python3 -c "import django; print(django.__path__)"
 
## after getting this repo in your pc :
 - for windows user :
    - open CMD in the (repo) folder
    - py -m venv venv
    - venv\Scripts\activate<br><br>
![Screenshot from 2023-01-09 03-02-27](https://user-images.githubusercontent.com/75578565/211227786-9b6699ac-db89-4b8e-9677-eb83edac4bc6.png)<br>
    - pip install -r requirements.txt
    - cd backend
    - py manage.py runserver   
 - for linux user :
    - open terminal in the (repo) folder
    - python3 -m venv venv
    - source venv/bin/activate <br><br>
![Screenshot from 2023-01-09 03-20-30](https://user-images.githubusercontent.com/75578565/211228495-7b24afa7-dfed-4005-beee-984cce8a5684.png)<br>
    - pip install -r requirements.txt
    - cd backend
    - python3 manage.py runserver<br><br>
![Screenshot from 2023-01-09 03-23-48](https://user-images.githubusercontent.com/75578565/211229438-201d5a6e-b4a6-42c6-ab5d-07d49b843eee.png)
<br><br>
## folders structure:
![Screenshot from 2023-01-09 03-52-21](https://user-images.githubusercontent.com/75578565/211230186-49dadc2d-1ded-45cc-a412-ba92d92bd007.png)
##  endpoint in py_client app make sure that venv is activate and the server is ready :
 - cd py_client &nbsp; &nbsp; &nbsp; &nbsp; (linux or windows)
 - py list.py &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  (windows)
 - python3 list.py &nbsp; (linux)<br>
 or <br>
 ![Screenshot from 2023-01-09 04-06-28](https://user-images.githubusercontent.com/75578565/211231062-4091a772-1fdb-4392-8446-9a202e00a1e9.png)

# Admin User :
 - username,password = ahmed
# Staff User : 
 - username = staff
 - password = staffstaff

