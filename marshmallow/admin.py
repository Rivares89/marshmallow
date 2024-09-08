from django.contrib import admin

from marshmallow.models import Marshmallow


@admin.register(Marshmallow)
class MarshmallowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', )
    list_filter = ('name', 'price', )
    search_fields = ('name', 'price', )
