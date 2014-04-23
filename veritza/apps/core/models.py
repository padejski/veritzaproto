from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import UUIDField


# CORE VERITZA MODELS ##################################
class User(AbstractUser):
    uuid = UUIDField()
    subscriptions = models.ManyToMany("Veritza")

    def subscribe(self, veritza):
        self.subscriptions.add(veritza)

    def unsubscribe(self, veritza):
        self.subscriptions.remove(veritza)


class VeritzaBaseModel(models.Model):
    """
    Base abstract model for the Veritza's core models
    """
    class Meta:
        abstract = True

    uuid = UUIDField()
    created_by = models.ForeignKey('User')
    modified_by = models.ForeignKey('User')
    created = models.DateTimeField(_("Created Timestamp"), auto_add_now=True)
    updated = models.DateTimeField(_("Last Modified"), auto_now=True)
    active = models.BooleanField(_("Active"), default=True)

class DummyProfile(models.Model):
    """
    Needed for django-userena AUTH_PROFILE_MODEL setting
    """
    pass

class Person(VeritzaBaseModel):
    national_id = models.CharField(_("National ID"), max_length=40, null=True, blank=True)
    national_id_type = models.CharField(_("National ID Type"), max_length=40, null=True, blank=True)
    first_name = models.CharField(_("First Name"), max_length=255)
    middle_names = models.CharField(_("Middle Names"), max_length=1024, null=True, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255)
    birth_date = models.DateTimeField(_("Birth Date"), null=True, blank=True)

    def __unicode__(self):
        return "%s %s - %s" % (self.first_name, self.last_name, self.national_id)

class Official(VeritzaBaseModel):
    person = models.OneToOneField(Person, null=True, blank=True)

    def __unicode__(self):
        return self.__repr__()

class Dataset(VeritzaBaseModel):
    name = models.CharField(_("Name"), max_length=255)
    source = models.CharField(_("Source"), max_length=512)
    description = models.TextField(_("Description"), null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)
    tags = models.ManyToMany("Tag", null=True, blank=True)

    def __unicode__(self):
        return self.name

class Veritza(VeritzaBaseModel):
    name = models.CharField(_("Name"), max_length=255)
    sources = models.ManyToMany(_("Sources"))
    description = models.TextField(_("Description"), null=True, blank=True)
    notes = models.TextField(_("Notes"), null=True, blank=True)


# ADDITIONAL MODELS ##################################
class UserSettings(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class Alert(models.Model):
    user = models.ForeignKey("User")
    veritza = models.ForeignKey("Veritza", null=True, blank=True)
    text

class Tag(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)