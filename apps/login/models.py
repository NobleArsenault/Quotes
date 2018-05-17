# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, first, last, email, password, confirm, dob):

        response = {
            "errors": [],
            "valid": True,
            "user": None
        }

        if len(first) < 1:
            response["errors"].append("First name is required")
        elif len(first) < 2:
            response["errors"].append("First name must be at least 2 characters long")

        if len(last) < 1:
            response["errors"].append("Last name is required")
        elif len(last) < 2:
            response["errors"].append("Last name must be at least 2 characters long")

        if len(email) < 1:
            response["errors"].append("Email is required")
        elif not EMAIL_REGEX.match(email):
            response["errors"].append("Invalid email")
        else:
            email_list = User.objects.filter(email=email.lower())
            if len(email_list) > 0:
                response["errors"].append("Email already exists")

        if len(password) < 1:
            response["errors"].append("Password is required")
        elif len(password) < 8:
            response["errors"].append("Password must be 8 characters or more")

        if len(confirm) < 1:
            response["errors"].append("Confirm password is required")
        elif password != confirm:
            response["errors"].append("Confirm password must match Password")

        if len(dob) < 1:
            response["errors"].append("Date of Birth is required")
        else:
            date = datetime.strptime(dob, "%Y-%m-%d")
            today = datetime.now()
            if date > today:
                response["errors"].append("Date of Birth must be in the past")

        if len(response["errors"]) > 0:
            response["valid"] = False
        else:
            response["user"] = User.objects.create(
                first_name=first,
                last_name=last,
                email=email.lower(),
                password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                dob=date
            )

        return response

    def login(self, email, password):

        response = {
            "errors": [],
            "valid": True,
            "user": None
        }

        if len(email) < 1:
            response["errors"].append("Email is required")
        elif not EMAIL_REGEX.match(email):
            response["errors"].append("Invalid email")
        else:
            email_list = User.objects.filter(email=email.lower())
            if len(email_list) == 0:
                response["errors"].append("Email does not exist")

        if len(password) < 1:
            response["errors"].append("Password is required")
        elif len(password) < 8:
            response["errors"].append("Password must be 8 characters or more")

        if len(response["errors"]) == 0:
            hashed_pw = email_list[0].password
            if bcrypt.checkpw(password.encode(), hashed_pw.encode()):
                response["user"] = email_list[0]
            else: response["errors"].append("Incorrect Password")

        if len(response["errors"]) > 0:
            response["valid"] = False

        return response

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    favorites = models.ManyToManyField("cite", related_name="favorites", default=None)
    dob = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
class citeManager(models.Manager):
    def add(self, quoter, quote):

        response = {
            "errors": [],
            "valid": True,
            "user": User
        }

        if len(quoter) < 1:
            response["errors"].append("quoter name is required")
        elif len(quoter) < 2:
            response["errors"].append("quoter name must be at least 2 characters long")

        if len(quote) < 1:
            response["errors"].append("quote is required")
        elif len(quote) < 2:
            response["errors"].append("quote description must be 2 characters or more")
        
        if len(response["errors"]) > 0:
            response["valid"] = False


        return response




class cite(models.Model):
        quoter = models.CharField(max_length=255)
        quote = models.CharField(max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        uploader = models.ForeignKey(User, related_name="quote_uploader")

	def __str__(self):
		return self.quoter

        objects = citeManager()