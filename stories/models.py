from django.db import models




class Story(models.Model):

    title       = models.CharField('story title',max_length=255)
    story_text  = models.TextField(default='')
    pub_date    = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    tags        = models.TextField(default='',blank=True,null=True)
    seen        = models.IntegerField(default=0)
    votes       = models.IntegerField(default=0)
    featured    = models.BooleanField(default=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'stories'
        ordering = ['-pub_date', 'title']
