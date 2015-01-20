import uuid
from django.db import models


class UUIDField(models.CharField) :
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 255 )
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)
    
    def pre_save(self, model_instance, add):
        if add :
            value = uuid.uuid4()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)

    def south_field_triple(self):
        '''Returns a suitable description of this field for South.'''
        from south.modelsinspector import introspector
        field_class = '%s.%s' % (self.__class__.__module__, self.__class__.__name__)
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    campaign_id = UUIDField(editable=False)
    expired = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s: %s' % (self.name, self.campaign_id)


class ClickTracking(models.Model):
    campaign = models.ForeignKey(Campaign)
    link = models.CharField(max_length=255)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s: %s - %s' % (self.campaign, self.link, self.count)
