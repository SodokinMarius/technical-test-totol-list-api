from django.db import models

from django.utils.functional import cached_property
# Module for safedelete
from safedelete.models import SafeDeleteModel

from django.conf import settings

from .enums import ProgressChoiceEnum


import datetime 
from django.utils import timezone


class Task(SafeDeleteModel):  
    title = models.CharField(max_length=250,null=False)  
    description = models.TextField(max_length=500,null=True)
    date_start = models.DateField(default=datetime.datetime.now)
    date_end = models.DateField(null=False)
    progress_status = models.CharField(choices=ProgressChoiceEnum.items(),max_length=200,default="Pending")
    file = models.FileField(null=True,upload_to="tasks_files")
    is_cancelled = models.BooleanField(default=False)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    
    def save(self, *args, **kwargs):
        current_time = timezone.now().date()
        if self.is_cancelled:
            self.progress_status = ProgressChoiceEnum.Cancelled.value
        elif current_time > self.date_end:
            if current_time > self.date_end:
                self.progress_status = ProgressChoiceEnum.Delayed.value
            else:
                self.progress_status = ProgressChoiceEnum.Completed.value
        elif self.date_start <= current_time <= self.date_end:
            self.progress_status = ProgressChoiceEnum.InProgress.value
        else:
            self.progress_status = ProgressChoiceEnum.Pending.value
        super(Task, self).save(*args, **kwargs)
        
    def __str__(self) :
        return f'{self.title} | {self.progress_status}'
