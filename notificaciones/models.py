from __future__ import unicode_literals
from django.db import models


class MyModel(models.Model):
	field = models.CharField(max_length=45)
# end class