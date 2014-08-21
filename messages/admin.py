from django.contrib import admin
from messages.models import Message, Conversation


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    fields = ['sender', 'text',]


class ConversationAdmin(admin.ModelAdmin):
    inlines = [MessageInline]


admin.site.register(Message)
admin.site.register(Conversation, ConversationAdmin)
