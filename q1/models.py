from django.db import models




class SaveImage(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)