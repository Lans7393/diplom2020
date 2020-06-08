from django.contrib import admin
from .models import Activity, Product, Company


# class CompanyActivitiesInline(admin.TabularInline):
#     model = Company.activities.through
#     autocomplete_fields = ('activity',)
#     list_filter = ('is_main_activity',)
#     extra = 1


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'okved2')
    search_fields = ('name', 'okved2',)
    ordering = ('id',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'okpd2',)
    # list_filter = ('is_active', 'type',)
    search_fields = ('name', 'okpd2',)
    ordering = ('id',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post_index', 'address', 'get_activities')
    search_fields = ('name', 'post_index', 'address',)
    filter_horizontal = ('activities',)
    # autocomplete_fields = ('activities',)
    # date_hierarchy = 'created'
    # prepopulated_fields = {'slug': ('title',)} # поле slug не требуется вводить, оно заполняется автоматически значением поля title
    # raw_id_fields = ('author',) # foreign_key при редактировании объекта будет поле для поиска а не дропдаун лист
    # inlines = [CompanyActivitiesInline]

    def get_activities(self, obj):
        activities_str = ("\n".join([a.okved2+', ' for a in obj.activities.all()]))
        return activities_str[:-2]


