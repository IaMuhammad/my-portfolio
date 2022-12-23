from datetime import datetime, date

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, DateField, TextChoices, TextField, ImageField, ForeignKey, SET_NULL, \
    EmailField, DateTimeField, CASCADE, IntegerField, URLField
from django.utils.text import slugify


# Create your models here.


class User(AbstractUser):
    class Degree(TextChoices):
        JUNIOR = 'junior', 'junior',
        MIDDLE = 'middle', 'middle',
        SENIOR = 'senior', 'senior'

    birthday = DateField(auto_now_add=True)
    phone = CharField(max_length=30)
    degree = CharField(max_length=20, choices=Degree.choices, default=Degree.JUNIOR)
    majority = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    photo = ImageField(default='users/default_user')

    @property
    def get_portfolio_count(self):
        return Portfolio.objects.all().count()

    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def get_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

    @property
    def get_hour_support(self):
        now = datetime.now()
        return (datetime.now().date() - self.date_joined.date()).days

    @property
    def get_phone_number(self):
        return


class Social(Model):
    name = CharField(max_length=255)
    url = URLField(max_length=255)
    user = ForeignKey(User, CASCADE)


class Skill(Model):
    name = CharField(max_length=255)
    percentage = IntegerField()
    user = ForeignKey(User, CASCADE)


class Education(Model):
    title = CharField(max_length=255)
    timedelta = CharField(max_length=20)
    place = CharField(max_length=255)
    description = TextField(max_length=255)


class Category(Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=255)
    slug = CharField(max_length=255)


    @property
    def portfolio_count(self):
        return self.portfolio_set.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            while Category.objects.filter(slug=self.slug).exists():
                slug = Category.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            sp = slug.split('-')
                            self.slug = '-'.join(sp[:-1]) + '-' + str(int(sp[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(Model):
    title = CharField(max_length=255)
    client = CharField(max_length=255)
    category = ForeignKey('apps.Category', SET_NULL, blank=True, null=True)
    slug = CharField(max_length=255)
    description = TextField()
    project_date = DateField(auto_now_add=True)
    project_url = CharField(max_length=255)
    picture = ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Category.objects.filter(slug=self.slug).exists():
                slug = Category.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            sp = slug.split('-')
                            self.slug = '-'.join(sp[:-1]) + '-' + str(int(sp[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)


class FeedBack(Model):
    author = ForeignKey('apps.User', CASCADE)
    feedback = TextField()
    written_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

class Message(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    subject = CharField(max_length=255)
    message = TextField()
    written_at = DateTimeField(auto_now_add=True)
    answered = DateTimeField(null=True, blank=True)
