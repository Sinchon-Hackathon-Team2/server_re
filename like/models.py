from django.db import models

from account.models import User
from post.models import Post

class Like(models.Model):
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(to=Post,on_delete=models.CASCADE)
