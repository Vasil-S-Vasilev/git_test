from django.contrib import admin
from accounts.authentication import get_user_model
# Register your models here.


UserModel = get_user_model()

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass
