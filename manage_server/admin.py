from django.contrib import admin
from .models import ManagedPC
from .models import ManagedPCUser
from .models import AccessToken
from .models import OperationLog
from .models import ManagedPCUserRelation

# Register your models here.

class ManagedPCAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'device_id', 'management_id', 'updated_at')
    list_filter = ['updated_at']

class ManagedPCUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_displayname', 'updated_at')
    list_filter = ['updated_at']

class ManagedPCUserRelationAdmin(admin.ModelAdmin):
    list_display = ('managed_pc', 'managed_user', 'updated_at')
    list_filter = ['updated_at']

class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('access_token', 'managed_user', 'created_at', 'expires_in')
    list_filter = ['created_at']

class OperationLogAdmin(admin.ModelAdmin):
    list_display = ('managed_user', 'managed_pc', 'operation', 'operation_status', 'operation_result', 'operation_time', 'updated_at')
    list_filter = ['operation_time', 'updated_at']

admin.site.register(ManagedPC, ManagedPCAdmin)
admin.site.register(ManagedPCUser, ManagedPCUserAdmin)
admin.site.register(ManagedPCUserRelation, ManagedPCUserRelationAdmin)
admin.site.register(OperationLog, OperationLogAdmin)
admin.site.register(AccessToken, AccessTokenAdmin)

admin.site.site_header = '貸与PC管理システム'