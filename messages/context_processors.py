from messages.models import Message


def message_count(request):

    if request.user.is_authenticated():
        message_count = Message.objects.filter(
            conversation__users=request.user
        ).exclude(
            seen_users=request.user
        ).count()

    else:
        message_count = None

    return {
        "message_count": message_count
    }
