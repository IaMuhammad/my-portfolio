from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from apps.models import User, Portfolio, Message, Category, Skill, Education, Social


# Register your models here.

@register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'fullname')

    def fullname(self, obj):
        f = obj.first_name + obj.last_name
        if f:
            return f
        return 'null'




@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')

    exclude = ('slug',)


@register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    list_display = ('title', 'main_picture', 'client',
                    'project_date', 'project_url_site')
    list_filter = ('client', 'project_date',)
    readonly_fields = ('headshot_image',)

    def main_picture(self, obj):
        return format_html(
            f'''<img style="border-radius: 5px;" width="100px" height="30px" src="{obj.picture.url}"/>''')

    def project_url_site(self, obj):
        return format_html(f'''<a href="https://{obj.project_url}">{obj.project_url}</a>''')

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.picture.url,
            width=obj.picture.width,
            height=obj.picture.height,
        ))

@register(Education)
class EducationAdmin(ModelAdmin):
    list_display = ("title", "timedelta")

@register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('name', 'user')

@register(Social)
class SocialAdmin(ModelAdmin):
    list_display = ('name', 'url')


@register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'written_at', 'answered',)
