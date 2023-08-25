from django.db import models


class Comment(models.Model):
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(to=Post,on_delete=models.CASCADE)
    content=models.TextField(verbose_name="내용")
    createdAt=models.DateTimeField(verbose_name="작성시일",auto_now_add=True)
