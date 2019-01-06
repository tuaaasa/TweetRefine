from django.contrib import admin

from .models import Account, RefineTweet
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(RefineTweet)
class RefineTweet(admin.ModelAdmin):
    pass
