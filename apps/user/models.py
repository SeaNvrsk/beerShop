from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDERS = (
        ('m', 'мужчина'),
        ('f', 'женщина'),
   )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/images/users', verbose_name='Изображение')
#    email = models.EmailField(unique=True, verbose_name="e-mail")
    birthDay = models.DateField(auto_now=False, verbose_name='День рождения', help_text='формат: 12.05.1990', null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default='', verbose_name="пол")
    phoneNum = models.CharField(max_length=12, default="+7", verbose_name='номер телефона')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)


