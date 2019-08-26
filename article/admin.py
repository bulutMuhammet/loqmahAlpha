from django.contrib import admin

from .models import Article,Comment,Product,help

#dmin.site.register(Comment)
admin.site.site_header = "Loqmah Yönetimi "
admin.site.site_title = "UNIDECIMAL"





# Register your models here.
#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date","article_aciklama"]
    list_display_links=["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    

    class Meta:
        model = Article

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ["comment_author","comment_date","comment_oy"]
    list_display_links=["comment_author","comment_date"]

    search_fields = ["comment_author"]

    list_filter = ["comment_date"]
    

    class Meta:
        model = Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ["title","pro_date","prohelp"]
    list_display_links=["title","pro_date"]

    search_fields = ["pro_date"]

    list_filter = ["pro_date"]
    

    class Meta:
        model = Product

@admin.register(help)
class helpAdmin(admin.ModelAdmin):
    
    list_display = ["help_name","help_date","help_title"]
    list_display_links=["help_title","help_date"]

    search_fields = ["help_date"]

    list_filter = ["help_date"]
    

    class Meta:
        model = help


