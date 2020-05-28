from django.db import models

class Cafe(models.Model):#상속
    product_name = models.CharField(max_length=20) #이름넣기 table에(class에) 넣을 요소들 만드는것! 지금 만든걸 migrations해야 sql의 시트의 열로 만듬
    product_price = models.IntegerField()

    
