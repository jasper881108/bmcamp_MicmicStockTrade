from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.



class MyAccountManager(BaseUserManager):
    ###### create user
    def create_user(self,email,username,password = None):
        if not email:
            raise ValueError('Users must have an email')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    ###### create super user
    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

def get_profile_image_path(self,filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return 'my_pic/icon.jpeg.jpeg'

class Account(AbstractBaseUser):
    email                       = models.EmailField(verbose_name='Email',max_length=60,unique = True)
    username                    = models.CharField(verbose_name='User',max_length=20,unique = True)
    money                       = models.FloatField(verbose_name='Money',default=1000.00)
    date_joined                 = models.DateField(verbose_name='Join Date',auto_now_add=True)
    last_login                  = models.DateField(verbose_name='Last Used', auto_now=True)
    is_admin                    = models.BooleanField(verbose_name='Admin',default=False)
    is_active                   = models.BooleanField(verbose_name='Active',default=True)
    is_staff                    = models.BooleanField(verbose_name='Staff', default=False)
    is_superuser                = models.BooleanField(verbose_name='SuperUser',default=False)
    profile_image               = models.ImageField(max_length=255,upload_to=get_profile_image_path,null=True,blank=True,default = get_default_profile_image)
    AAPL                        = models.PositiveIntegerField(verbose_name='AAPL',default=0)
    Google                      = models.PositiveIntegerField(verbose_name='Google', default=0)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_image/{self.pk}/'):]

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True