帳號紀錄:

superuser:
{
  superman
  super123
  super@fju.edu.tw
}
created from admin normal student:
{
  peter
  abc019283
}


cmd:

py manage.py help

py manage.py makemigrations users_mgt
py manage.py makemigrations club_mgt
py manage.py makemigrations activity_mgt
py manage.py makemigrations announcement_mgt
py manage.py makemigrations mainsite
py manage.py makemigrations
py manage.py migrate
py manage.py create_clubs
py manage.py create_groups
py manage.py createsuperuser

user = {
	ID: superman
	EMAIL: superman@mail
	USERTYPE: CENTERMEMBER
	FIRST NAME: spider
	LAST NAME: superman
	PWD: super123
	PWD2: super123
}
py manage.py create_posts