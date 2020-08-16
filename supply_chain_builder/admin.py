# from django.contrib import admin
# from .models import Okved, Okpd, Company
# from django.utils.safestring import mark_safe

# from django.utils.html import format_html


# class CompanyActivitiesInline(admin.TabularInline):
#     model = Company.activities.through
#     autocomplete_fields = ('activity',)
#     list_filter = ('is_main_activity',)
#     extra = 1


# @admin.register(Okved)
# class ActivityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'okved2')
#     search_fields = ('name', 'okved2',)
#     ordering = ('id',)


# @admin.register(Okpd)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'okpd2',)
#     # list_filter = ('is_active', 'type',)
#     search_fields = ('name', 'okpd2',)
#     ordering = ('id',)


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'main_okved', 'get_sup_okveds', 'get_list_org_link')
#     search_fields = ('name', 'inn', 'list_org_link')
#     filter_horizontal = ('sup_okveds',)
#     raw_id_fields = ('main_okved',)

#     # autocomplete_fields = ('activities',)
#     # date_hierarchy = 'created'
#     # prepopulated_fields = {'slug': ('title',)} # поле slug не требуется вводить, оно заполняется автоматически значением поля title
#     # inlines = [CompanyActivitiesInline]


#     def get_sup_okveds(self, obj):
#         okveds_str = ("<br>".join([a.okved2 + ' ' + a.name for a in obj.sup_okveds.all()]))
#         return mark_safe(okveds_str[:-2])


#     get_sup_okveds.short_description = 'Виды деятельности'

#     # def get_site_link(self, obj):
#     #     return format_html("<a href='{url}'>{url}</a>", url=obj.site)
#     #
#     # get_site_link.short_description = 'Сайт компании'

#     def get_list_org_link(self, obj):
#         return format_html("<a href='{url}'>{url}</a>", url=obj.list_org_link)

#     get_list_org_link.short_description = 'Страница на list-org.com'
