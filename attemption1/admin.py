from django.contrib import admin
from .models import Activity, Product, Company, CompanyActivities

admin.site.register(Activity)
# admin.site.register(Product)
# admin.site.register(Company)


class CompanyActivitiesInline(admin.TabularInline):
    model = CompanyActivities
    raw_id_fields = ('activity_id',)
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'okpd2',)
    # list_filter = ('is_active', 'type',)
    search_fields = ('name', 'okpd2',)
    ordering = ('id',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # filter_horizontal = ('activities',)
    list_display = ('id', 'name', 'post_index', 'address', 'get_activities')
    search_fields = ('name', 'post_index', 'address',)
    # date_hierarchy = 'created'
    # prepopulated_fields = {'slug': ('title',)} # поле slug не требуется вводить, оно заполняется автоматически значением поля title
    # raw_id_fields = ('author',) # foreign_key при редактировании объекта будет поле для поиска а не дропдаун лист
    inlines = [CompanyActivitiesInline]

    def get_activities(self, obj):
        return "\n".join([a.okved2+', ' for a in obj.activities.all()])
