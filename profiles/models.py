from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # image = models.FileField(upload_to="images") # this file will NOT be stored in the DB since files should be stored in hard drives so this will store the path of the file after storing it somewhere in the drive
    image = models.ImageField(upload_to="images")

    # # Uploda to --> check project settings Media Root