from django.db import models

# Create your models here.
class UserMessages(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user_email = models.EmailField()
    message = models.CharField(max_length=200)

    is_processed = models.BooleanField(default=False)
    send_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}{self.surname}-{self.user_email}: {self.message[:20]}'
