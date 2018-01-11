from django.contrib import admin

# Register your models here.
from.models import Z_hosts
from.models import Z_IP,Z_User

admin.site.register(Z_hosts)
admin.site.register(Z_IP)
admin.site.register(Z_User)