from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from .models import Book
from .forms import BookForm

# Custom Admin Site
class CustomAdminSite(AdminSite):
    site_header = 'My Custom Admin'
    site_title = 'Custom Admin Site'
    index_title = 'Welcome to My Custom Admin Site'

# Registering the custom admin site
admin_site = CustomAdminSite(name='myadmin')

# Customizing the Book model admin
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'author')
    ordering = ('-published_date',)
    list_editable = ('author',)
    list_display_links = ('title',)

# Register the model with the custom admin site
admin_site.register(Book, BookAdmin)
