from django.contrib import admin
from myapp.models import Book, Country, Comment


class InlineCommentAdmin(admin.StackedInline):
    model = Comment
    extra = 2
    readonly_fields = ["like"]


class BookAdmin(admin.ModelAdmin):
    inlines = [InlineCommentAdmin]


admin.site.register(Book, BookAdmin)
admin.site.register(Country)

