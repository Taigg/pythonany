from django.contrib import admin
from appFive.models import UserProfileInfo


# from appFive.models import YourModel
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'portfolio_site', 'profile_pic')  # Hiển thị các trường trên trang danh sách
    search_fields = ('user__username', 'portfolio_site')  # Thêm chức năng tìm kiếm cho các trường
    fields = [ 'portfolio_site','name']
    list_editable = ['name']

admin.site.register(UserProfileInfo, UserProfileInfoAdmin)




