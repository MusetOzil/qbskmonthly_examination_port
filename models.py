from django.db import models

class Qbsk2(models.Model):
    details_title = models.CharField(max_length=255, blank=True, null=True)
    details_date = models.CharField(max_length=255, blank=True, null=True)
    details_funny = models.CharField(max_length=255, blank=True, null=True)
    details_content = models.TextField(blank=True, null=True)
    details_published_address = models.CharField(db_column='details_Published_address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qbsk_2'


class Qbsk3(models.Model):
    user_name = models.CharField(max_length=125, blank=True, null=True)
    user_pic = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    funny = models.CharField(max_length=125, blank=True, null=True)
    comment_count = models.CharField(max_length=125, blank=True, null=True)
    comment_user = models.CharField(max_length=255, blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)
    comment_dianzhan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qbsk_3'


class Qbsk4(models.Model):
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_pic = models.CharField(max_length=255, blank=True, null=True)
    recommendations = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    liveness = models.CharField(max_length=125, blank=True, null=True)
    date_publish = models.CharField(max_length=255, blank=True, null=True)
    likesm = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qbsk_4'


class Qsbk1(models.Model):
    article_title = models.CharField(max_length=255, blank=True, null=True)
    article_video = models.CharField(max_length=255, blank=True, null=True)
    article_tag = models.CharField(max_length=20, blank=True, null=True)
    article_funny = models.CharField(max_length=20, blank=True, null=True)
    article_comment = models.CharField(max_length=255, blank=True, null=True)
    article_author = models.CharField(max_length=125, blank=True, null=True)
    article_author_profile = models.CharField(max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qsbk_1'