from django.db import models
from datetime import datetime
# Create your models here.

class Stream_1(models.Model):
    name = models.CharField(max_length = 10000, blank=True, null=True)
    file_list = models.CharField(max_length = 10000, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(Stream_1, self).save(*args, **kwargs)
        print('[TIME : %s] Stream_1 save' % str(datetime.now()))

    def delete(self, *args, **kwargs):
        super(Stream_1, self).delete(*args, **kwargs)
        print('[TIME : %s] Stream_1 delete' % str(datetime.now())) 

class Stream_2(models.Model):
    name = models.CharField(max_length = 10000, blank=True, null=True)
    file_list = models.CharField(max_length = 10000, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(Stream_2, self).save(*args, **kwargs)
        print('[TIME : %s] Stream_2 save' % str(datetime.now()))

    def delete(self, *args, **kwargs):
        super(Stream_2, self).delete(*args, **kwargs)
        print('[TIME : %s] Stream_2 delete' % str(datetime.now()))  

class Stream_3(models.Model):
    name = models.CharField(max_length = 10000, blank=True, null=True)
    file_list = models.CharField(max_length = 10000, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(Stream_3, self).save(*args, **kwargs)
        print('[TIME : %s] Stream_3 save' % str(datetime.now()))

    def delete(self, *args, **kwargs):
        super(Stream_3, self).delete(*args, **kwargs)
        print('[TIME : %s] Stream_3 delete' % str(datetime.now()))  
