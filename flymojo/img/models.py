from __future__ import unicode_literals
from django.db import models


ACTIVE = ((0,'Inactive'), (2, 'Active'),)
class Base(models.Model):
    
    active = models.PositiveIntegerField(choices = ACTIVE, default=2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    def switch(self):
        self.active = {0: 2, 2: 0}[self.active]
        self.save()
        return self.active

    class Meta:
        abstract = True


class Kyc(Base):
    merchant = models.ForeignKey('Merchant')

    name = models.CharField(max_length=100)
    pan_no = models.CharField(max_length=100)
    dob = models.DateField()

    image = models.ImageField()
    confidence_level = models.IntegerField()

    check_count = models.IntegerField(default=0)
    verified = models.BooleanField()


class Moderator(models.Model):
    user = models.ForeignKey('auth.User')

    def get_points(self):
        feedbacks = FeedBack.objects.filter(master__moderator=self)
        return sum(i.action.points for i in feedbacks)


class Merchant(models.Model):
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return str(self.user)


class Action(models.Model):
    ACTION_CHOICES = ((0,'Nothing'), (1, 'Correct'),
                      (2, 'Wrong'), (3, 'Rectify'))
    action = models.IntegerField(choices=ACTION_CHOICES)
    points = models.IntegerField()


class MasterFeedBack(models.Model):
    moderator = models.ForeignKey('Moderator')
    kyc = models.ForeignKey('Kyc')
    

class FeedBack(models.Model):
    FIELD_CHOICES = ((0, 'Name'), (1, 'Pan No'),
                      (2, 'dob'))
    master = models.ForeignKey('MasterFeedBack')
    action = models.ForeignKey('Action')
    old_info = models.CharField(max_length=100)
    field = models.IntegerField(choices=FIELD_CHOICES)
