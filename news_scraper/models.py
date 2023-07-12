from django.db import models

# Create your models here.


class NewsArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, db_collation="utf8mb4_0900_ai_ci", blank=True, null=True, unique=True)
    url_md5 = models.CharField(max_length=255, db_collation="utf8mb4_0900_ai_ci", blank=True, null=True, unique=True)
    title = models.CharField(max_length=255, db_collation="utf8mb4_0900_ai_ci", blank=True, null=True)
    content = models.TextField(db_collation="utf8mb4_0900_ai_ci", blank=True, null=True)
    section = models.CharField(max_length=255, db_collation="utf8mb4_0900_ai_ci", blank=True, null=True)
    image_url = models.TextField(db_collation="utf8mb4_0900_ai_ci", blank=True, null=True)
    portal = models.CharField(max_length=255, db_collation="utf8mb4_0900_ai_ci", blank=True, null=True)
    media = models.CharField(max_length=255, db_collation="utf8mb4_0900_ai_ci", blank=True, null=True)
    published = models.CharField(max_length=255, db_collation="utf8mb4_0900_ai_ci", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "news_article"
        app_label = "news_scraper"
