from django.db import models



class Like(models.Model):
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(to=Post,on_delete=models.CASCADE)
