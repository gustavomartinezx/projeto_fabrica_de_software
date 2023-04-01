from django.contrib import admin
from .models import Cliente
from .models import Loja
from .models import Album

admin.site.register(Cliente)
admin.site.register(Album)
admin.site.register(Loja)

# Register your models here.
