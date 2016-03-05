from actstream.feeds import CustomJSONActivityFeed


class CustomUserJSONActivityFeed(CustomJSONActivityFeed):
    """
    Feed for Manager feeds that need the user as the first arg
    """
    def dispatch(self, request, *args, **kwargs):
        return super(CustomUserJSONActivityFeed, self).dispatch(request,
                                                                sender=request.user,
                                                                *args, **kwargs)
