from django.db import models

# Create your models here.
# DTO(vo)와 유사
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField(editable=True) # editable=True을 넣으면 편집이 가능
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True) # auto_now_add=True 지금시간이 자동으로 들어가게
    
    