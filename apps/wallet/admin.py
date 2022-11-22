from django.contrib import admin
from .models import Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'balance')


admin.site.register(Wallet, WalletAdmin)
# Register your models here.
