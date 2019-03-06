import os 

array=[
'flask',
'flask-admin',
'flask-login',
'enum',
'requests',
'python-dateutil',
'sqlalchemy'
]

for package in array:
	os.system('pip install '+package)
