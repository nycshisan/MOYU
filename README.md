# MOYU
Fudan University 2018 SE group project

2018.10.23:add func for models.
1)MODELNAME.Create_MODELNAME.For instance,User.Create_User()
2)User.Login()

2018.10.22:add database  model for backend
func:Django with model
database configuration:
sample:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moyu',
        'HOST':'',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'password',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}
change if needed in MOYU-master/backend/moyu/moyu/settings.py,line 78





