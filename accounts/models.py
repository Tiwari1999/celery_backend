import uuid

from dirtyfields import DirtyFieldsMixin
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

class GenericBaseModel(models.Model):
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if isinstance(self, DirtyFieldsMixin) and not self._state.adding and not self.get_deferred_fields():
            dirty_fields = self.get_dirty_fields(check_relationship=False)
            update_fields = dirty_fields.keys()

        return super().save(force_insert, force_update, using, update_fields)


class User(GenericBaseModel, DirtyFieldsMixin, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'id'

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'user'
