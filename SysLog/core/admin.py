from django.contrib import admin
from .models import Cliente, Empresa, ClienteEmpresa

admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(ClienteEmpresa)
