from django.db import models


class Follow(models.Model):
    follower_id=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="follower_id")
    followee_id=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="followee_id")

