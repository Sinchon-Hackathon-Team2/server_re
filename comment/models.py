from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from post.models import Post


from account.models import User
from post.models import Post

class Comment(models.Model):
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="user_id")
    nickName=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="nickName")
    post_id=models.ForeignKey(to=Post,on_delete=models.CASCADE)
    content=models.TextField(verbose_name="내용")
    createdAt=models.DateTimeField(verbose_name="작성시일",auto_now_add=True)

