from django.contrib import admin
from collection.models import Thing, Social

# set up automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Thing, ThingAdmin)

class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('network', 'username',)

admin.site.register(Social, SocialAdmin)
