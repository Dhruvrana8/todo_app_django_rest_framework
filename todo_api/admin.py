from django.contrib import admin

from .models import TODO
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    # This is the list of fields we want to display on the django admin
    # The sequence of field will be same on the django admin
    list_display = ['pk', 'task_title', 'task_description', 'created_at',
                    'is_completed']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    # This function helps in removing the delete button from the django admin
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(TODO, TodoAdmin)
