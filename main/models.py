# from django.db import models
from django.db.models import *
"""
fs = FileSystemStorage(location='/media/photos')

class Car(models.Model):
    ...
    photo = models.ImageField(storage=fs)
"""

# class User(Model):
#     name = CharField(max_length=100)
#     nickname = CharField(max_length=100)
#     phone = CharField(max_length=12)
#     email = CharField(max_length=100)
#     city = CharField(max_length=100)
#     date_reg = DateField()
#     date_hb = DateField()
#     password = CharField(max_length=100)
#     language = CharField(max_length=100)
#     sex = BooleanField(default=True)
#     card = CharField(max_length=100)


class SEO(Model):
    title = CharField(max_length=100)
    text = TextField(max_length=200)
    keywords = CharField(max_length=100)
    url = CharField(max_length=100)
    description = CharField(max_length=100)


class Gallery(Model):
    pass


class Image(Model):
    image = ImageField()
    gallery_id = ForeignKey(Gallery, on_delete=PROTECT, blank=True, null=True)


class Film(Model):
    title = CharField(max_length=100)
    description = TextField()
    banner = OneToOneField(Image, on_delete=RESTRICT)
    gallery = OneToOneField(Gallery, on_delete=RESTRICT, null=True)
    link = CharField(max_length=100)
    type_3d = BooleanField(default=False)
    type_2d = BooleanField(default=False)
    type_imax = BooleanField(default=False)
    date = DateField()
    seo = OneToOneField(SEO, on_delete=RESTRICT)


class Show(Model):
    date_start = DateTimeField()
    date_end = DateTimeField()
    film = ManyToManyField(Film)
    price = FloatField(default=100.0)


class Ticket(Model):
    pass
# class Ticket(Model):
#     buyer = ForeignKey(User, on_delete=CASCADE)
#     position = IntegerField(default=0)
#     date_buy = DateTimeField()
#     collection = ForeignKey(Show, on_delete=CASCADE)


class Room(Model):
    title = CharField(max_length=100)
    description = TextField()
    plan = OneToOneField(Image, on_delete=RESTRICT, related_name='plan')
    banner = OneToOneField(Image, on_delete=RESTRICT, null=True)
    gallery = OneToOneField(Gallery, on_delete=RESTRICT, null=True)
    seo = OneToOneField(SEO, on_delete=RESTRICT)
    show = ForeignKey(Show, on_delete=RESTRICT)


class Cinema(Model):
    title = CharField(max_length=100)
    address = CharField(max_length=100)
    city = CharField(max_length=100)
    description = TextField()
    condition = TextField()
    logo = ForeignKey(Image, on_delete=RESTRICT)
    banner = ForeignKey(Image, on_delete=RESTRICT, related_name='banner', null=True)
    gallery = OneToOneField(Gallery, on_delete=RESTRICT, null=True)
    phone = CharField(max_length=100)
    seo = OneToOneField(SEO, on_delete=RESTRICT)
    room = ForeignKey(Room, on_delete=RESTRICT)


class Contact(Model):
    title = CharField(max_length=100)
    # PROTECT¶
    # Запобігайте видаленню об'єкта, на який посилається, піднявши ProtectedErrorпідклас django.db.IntegrityError.
    #
    # RESTRICT¶
    # Запобігання видаленню об’єкта, на який посилається, шляхом підвищення
    # RestrictedError(підклас django.db.IntegrityError). На відміну від PROTECT, видалення об’єкта, на який
    # посилається, дозволено, якщо він також посилається на інший об’єкт, який видаляється в тій самій операції,
    # але через CASCADE зв’язок.
    banner = ForeignKey(Image, on_delete=RESTRICT)
    gallery = OneToOneField(Gallery, on_delete=RESTRICT, null=True)
    address = CharField(max_length=100)
    map = CharField(max_length=100)
    using = BooleanField(default=False)


class ContactPage(Model):
    seo = OneToOneField(SEO, on_delete=RESTRICT)
    contact = OneToOneField(Contact, on_delete=CASCADE)


# class Choice(Model):
#     question = ForeignKey(on_delete=CASCADE)
#     choice_text = CharField(max_length=200)
#     votes = IntegerField(default=0)
