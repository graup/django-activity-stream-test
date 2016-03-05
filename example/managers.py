from actstream.managers import ActionManager, stream


class NotificationManager(ActionManager):
    @stream
    def unread_notifications(self, sender, recipient=None):
        # Version 1: Fails because of missing reverse relation
        # filters = {'action_object__read': False, 'action_object__deleted': False}

        # Version 2: Fails because of not matching db column types
        filters = {'notification__read': False, 'notification__deleted': False}

        return sender.actor_actions.filter(**filters)
