from django.db import models
from account.models import Univ, User




class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_id")
    nickName=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_id")
    univ_id = models.ForeignKey(Univ, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    ballad_tag =  models.BooleanField(default=False)
    dance_tag = models.BooleanField(default=False)
    rap_tag =  models.BooleanField(default=False)
    RandB_tag =  models.BooleanField(default=False)
    indie_tag =  models.BooleanField(default=False)
    rock_tag = models.BooleanField(default=False)

    music_name1 = models.CharField(max_length=100, null=True, blank=True)
    music_url1 = models.CharField(max_length=200, null=True, blank=True)
    thumnail1 = models.CharField(max_length=200, null=True, blank=True)
    music_name2 = models.CharField(max_length=100, null=True, blank=True)
    music_url2 = models.CharField(max_length=200, null=True, blank=True)
    thumnail2 = models.CharField(max_length=200, null=True, blank=True)
    music_name3 = models.CharField(max_length=100, null=True, blank=True)
    music_url3 = models.CharField(max_length=200, null=True, blank=True)
    thumnail3 = models.CharField(max_length=200, null=True, blank=True)
    music_name4 = models.CharField(max_length=100, null=True, blank=True)
    music_url4 = models.CharField(max_length=200, null=True, blank=True)
    thumnail4 = models.CharField(max_length=200, null=True, blank=True)
    music_name5 = models.CharField(max_length=100, null=True, blank=True)
    music_url5 = models.CharField(max_length=200, null=True, blank=True)
    thumnail5 = models.CharField(max_length=200, null=True, blank=True)
    music_name6 = models.CharField(max_length=100, null=True, blank=True)
    music_url6 = models.CharField(max_length=200, null=True, blank=True)
    thumnail6 = models.CharField(max_length=200, null=True, blank=True)
    music_name7 = models.CharField(max_length=100, null=True, blank=True)
    music_url7 = models.CharField(max_length=200, null=True, blank=True)
    thumnail7 = models.CharField(max_length=200, null=True, blank=True)
    music_name8 = models.CharField(max_length=100, null=True, blank=True)
    music_url8 = models.CharField(max_length=200, null=True, blank=True)
    thumnail8 = models.CharField(max_length=200, null=True, blank=True)
    music_name9 = models.CharField(max_length=100, null=True, blank=True)
    music_url9 = models.CharField(max_length=200, null=True, blank=True)
    thumnail9 = models.CharField(max_length=200, null=True, blank=True)
    music_name10 = models.CharField(max_length=100, null=True, blank=True)
    music_url10 = models.CharField(max_length=200, null=True, blank=True)
    thumnail10 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.content