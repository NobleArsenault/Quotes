from __future__ import unicode_literals
from ..login.models import User, cite
from django.db import models
from datetime import datetime

# class citeManager(models.Manager):
#     def add(self, quoter, quote):

#         response = {
#             "errors": [],
#             "is_valid": True,
#             "user": User
#         }

#         if len(quoter) < 1:
#             response["errors"].append("quoter name is required")
#         elif len(quoter) < 2:
#             response["errors"].append("quoter name must be at least 2 characters long")

#         if len(quote) < 1:
#             response["errors"].append("quote is required")
#         elif len(quote) < 2:
#             response["errors"].append("quote description must be 2 characters or more")

#         return response




# class cite(models.Model):
#         quoter = models.CharField(max_length=255)
#         quote = models.CharField(max_length=255)
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#         uploader = models.ForeignKey(User, related_name="quote_uploader")

# 	def __str__(self):
# 		return self.quoter

#         objects = citeManager()

# class cite(models.Model):
# 	content = models.CharField(max_length = 255)
# 	author = models.CharField(max_length = 255)
# 	poster = models.ForeignKey(User, related_name = 'uploader_cite')
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)
# 	objects = citeManager()
