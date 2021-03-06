from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Thing(Timestamp):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)

    def __unicode__(self):
        return self.name

    # new helper method
    def get_absolute_url(self):
        return "/things/%s/" % self.slug

class Social(models.Model):
    SOCIAL_TYPES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('pinterest', 'Pinterest'),
        ('instagram', 'Instagram'),
    )
    network = models.CharField(max_length=255, choices=SOCIAL_TYPES)
    username = models.CharField(max_length=255)
    thing = models.ForeignKey(Thing, related_name="social_accounts")

    class Meta:
        verbose_name_plural = "Social Media Links"

# our helper, add above the new model
def get_image_path(instance, filename):
    return '/'.join(['thing_images', instance.thing.slug, filename])

class Upload(models.Model):
    thing = models.ForeignKey(Thing, related_name="uploads")
    image = models.ImageField(upload_to=get_image_path)

    def save(self, *args, **kwargs):
        # this is required when you override save functions
        super(Upload, self).save(*args, **kwargs)

        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (1000, 1000)

            if i_width > 1000:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)
