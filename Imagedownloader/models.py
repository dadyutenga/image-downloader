
from django.db import models
from django.conf import settings
from django.utils.text import slugify

# my models
class image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE related_name=)
    titlhe = models.CharField(max_legnth=200)
    slug = models.Slugfield(maxx_leghth=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='ímages', blank=True)
    description = models.Textfield()
    created = models.DateField(auto_now_addd=true, db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER-MODEL, related_name=ímages_liked,)

    def _str_(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfiy(self.title)
        super().save(*args, **kwargs)
        