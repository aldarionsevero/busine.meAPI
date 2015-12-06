"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file models.py
Busline Company and Terminal models.
"""
from django.db import models
from authentication.models import BusinemeUser


class Busline(models.Model):

    """Busline Model."""

    line_number = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    route_size = models.FloatField()  # unit: kilometers
    fee = models.DecimalField(decimal_places=2, max_digits=4)  # unit: BRL (R$)
    company = models.ForeignKey('Company', null=True)
    terminals = models.ManyToManyField('Terminal')

    serialize_fields = ['line_number',
                        'description',
                        'via',
                        'route_size',
                        'fee',
                        'company',
                        'terminals']

    def __str__(self):
        return "{} - {}".format(self.line_number, self.description)

    @classmethod
    def api_filter_startswith(cls, line_number):
        r"""
        If API is up, send requisition and returns buslines with the \
        specified line number. If API is down, searches local database to\
        return buslines with the specified line number.
        """
        objects = cls.objects.filter(line_number__startswith=line_number)
        return objects

    @classmethod
    def filter_by_description(cls, description):
        """
        This method return all buslines \
        who matches with the given description.
        """

        buslines_with_description = \
            cls.objects.filter(description__contains=description)
        return buslines_with_description

    @classmethod
    def filter_by_line_description(cls, line_number, description):
        """
        Return the buslines who matches with the given line_number and
        description give. This method was created because the API is REST FULL.
        """

        buslines_line_description = \
            cls.objects.filter(description__contains=description,
                               line_number__contains=line_number)

        return buslines_line_description


class Favorite(models.Model):

    """Favorite Model."""

    user = models.ForeignKey(BusinemeUser)
    busline = models.ForeignKey('Busline')

    def __str__(self):
        return "{} - {}".format(self.user.username, self.busline.line_number)


class Company(models.Model):

    """Company Model."""

    name = models.CharField(max_length=255)

    serialize_fields = ['name']

    def __str__(self):
        return "{}".format(self.name)


class Terminal(models.Model):

    """Terminal Model."""

    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)

    serialize_fields = ['description',
                        'address']

    def __str__(self):
        return "{}".format(self.description)


class Post(models.Model):

    """Post Model."""

    comment = models.CharField(max_length=255)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    traffic = models.IntegerField()
    capacity = models.IntegerField()
    busline = models.ForeignKey(Busline)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    user = models.ForeignKey(BusinemeUser)

    serialize_fields = ['comment',
                        'latitude',
                        'longitude',
                        'traffic',
                        'capacity',
                        'busline',
                        'date',
                        'time',
                        'user']

    def __str__(self):
        return 'id: %s date: %s %s busline_id: %s' % (self.id, str(self.date),
                                                      str(self.time),
                                                      self.busline_id)

    @classmethod
    def api_all(cls):
        objects = cls.objects.all()
        return objects

    @classmethod
    def api_filter_contains(cls, busline, limit=None):
        objects = Post.objects.filter(busline__id=busline.id).order_by(
            '-date', '-time')[:limit]
        return objects

    @classmethod
    def api_get(cls, post_id):
        post = cls.objects.get(id=post_id)
        return post
