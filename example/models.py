from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from actstream.models import Action


class Notification(models.Model):
    text = models.TextField(default='')
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Reverse relation to action to be able to query for notification in feeds
    action = GenericRelation(Action,
                             content_type_field='action_object_content_type',
                             object_id_field='action_object_object_id',
                             related_query_name='notification')
