## Showcase of some problems with django-activity-stream

I tried to produce a minimal Django test project to showcase two problems.

Probably best to use a clean virtual env.

### Setup
    
    pip install -r requirements.txt
    python manage.py migrate

### Issue number 1

    python manage.py makemigrations

It will attempt to create an unwanted migration inside actstream.

    Migrations for 'actstream':
      0002_remove_action_data.py:
        - Remove field data from action

### Issue number 2

    python manage.py test

It will break with a DB error `No operator matches the given name and argument type(s).` (see `managers.py`).

It's because `action_object_object_id` (CharField) cannot be compared with `notification.id` (IntegerField).