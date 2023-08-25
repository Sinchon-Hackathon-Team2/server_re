from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from post.models import Post

from account.models import User
from post.models import Post

class Like(models.Model):
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(to=Post,on_delete=models.CASCADE)
