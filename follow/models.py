from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from account.models import User

class Follow(models.Model):
    follower_id=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="follower_id")
    followee_id=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="followee_id")

