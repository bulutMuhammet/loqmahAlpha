from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    article_aciklama=models.CharField(default="Açıklamalar Burada Görünür",max_length=50)
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name ="Yazar")
    title = models.CharField(max_length = 50,default="Başlık")
       
    
    content = RichTextField()
    
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="Oluşturulma Tarihi") 
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article= models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length=200,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    comment_oy=models.CharField(max_length=50,default="Oy",blank=False,null=False)
    comment_script=models.CharField(max_length=100,default=" ")
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']

class help(models.Model):
    article= models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale", blank=True, null=True)
    help_name=models.CharField(default="isim",max_length=50)
    help_mail=models.EmailField(default="Email",max_length=50)
    help_date=models.DateField(auto_now_add=True)
    help_title=models.CharField(default="konu",max_length=50)
    help_content=models.TextField(default="Sizi dinliyoruz",max_length=500)
    
    
    
    
    def __str__(self):
        return self.help_content

    class Meta:
        ordering = ['-help_date']



class Product(models.Model):
    prohelp=models.CharField(default="Buraya bir uyarı bırak.(Sadece sen göreceksin)",max_length=50)
    title = models.CharField(max_length = 50,default="Ürün Adı")
    pro_content = RichTextField()
    pro_date=models.DateTimeField(auto_now_add=True)
    pro_image = models.FileField(blank = True,null = True,verbose_name="Bir fotoğraf ekle. (Unidecimal 180*180 boyutları tavsiye ediyor)")
    def __str__(self):
        return self.pro_content

    class Meta:
        ordering = ['pro_date']