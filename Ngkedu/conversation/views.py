from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Conversation
from .forms import NewMessageForm
from item.models import Item

@login_required
def new_conversation(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    conversation = Conversation.objects.filter(item=item, members__in=[request.user])

    if conversation.exists():
        return redirect('conversation:detail', pk=conversation.first().id)

    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect('conversation:detail', pk=conversation.id)
    else:
        form = NewMessageForm()
    return render(request, 'conversation/new_conversation.html', {
        'form': form,
        'item_id': item_id,
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user])
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk, members__in=[request.user])
    messages = conversation.messages.all()
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect('conversation:detail', pk=pk)
    else:
        form = NewMessageForm()
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'messages': messages,
        'form': form,
    })