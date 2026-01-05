from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Conversation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='conversations')
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return f"Conversation about {self.item.name}"
    
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"