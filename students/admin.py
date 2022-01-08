from django.contrib import admin

from students.models import Student


class StudentsAdmin(admin.ModelAdmin):
    fields = [
        ('first_name', 'last_name'),
        ('age', 'birthday'),
        'phone_number',
        'group',
        ('enroll_date', 'graduate_date'),
    ]
    readonly_fields = ['age']
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
        'group',
    ]
    list_display_links = list_display
    list_per_page = 20
    search_fields = ['first_name', 'last_name']
    list_filter = ('group',)

    def get_queryset(self, request):
        """An attempt to avoid unnecessary requests"""
        qs = Student.objects.all().select_related('group')
        return qs


admin.site.register(Student, StudentsAdmin)
