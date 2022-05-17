from django.contrib import admin
from .models import User, Data, Pasport, Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'certificate_1', 'certificate_2', 'number_certificate')
    list_filter = ('user', 'certificate_1', 'certificate_2', 'number_certificate')
    search_fields = ('user', 'certificate_1', 'certificate_2', 'number_certificate')


# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'img')
#     list_filter = ('id', 'user', 'img')
#     search_fields = ('id', 'user', 'img')


class UserSearchAdmin(admin.ModelAdmin):

    list_display = ('name', 'id', 'email', 'phone_number')
    list_filter = ('name', 'email', 'phone_number')
    search_fields = ('name', 'id', 'email', 'phone_number')
    date_hierarchy = 'created_date'


AUTH_USER_MODEL = 'abstract_base_user_sample.CustomUser'


class DataAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'position')
    list_filter = ('user', 'organization', 'position')
    search_fields = ('user', 'organization', 'position')


class PasportAdmin(admin.ModelAdmin):
    list_display = ('user', 'pasport_1', 'pasport_1')
    list_filter = ('user', 'pasport_1', 'pasport_1')
    search_fields = ('user', 'pasport_1', 'pasport_1')


#admin.site.register(PhotoUser, PhotoAdmin)
admin.site.register(User, UserSearchAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Pasport, PasportAdmin)
admin.site.register(Certificate, CertificateAdmin)
