from django.contrib import admin
from cybersafe.models import Questions


class Admin(admin.ModelAdmin):
    help = 'Admin'
    list_display = ('id', 'question', 'answer')

    def handle(self, *args, **options):
        admin.site.register(Questions)

admin.site.register(Questions, Admin)