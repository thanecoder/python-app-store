from django.db import models


# Create your models here.
class App(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    # Required
    app_name = models.CharField(
        max_length=1000,
        null=False,
        blank=False
    )

    # Required
    app_id = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )

    # Required
    category = models.CharField(
        max_length=1000,
        null=False,
        blank=False
    )

    # Required
    version = models.CharField(
        max_length=6,
        null=False,
        blank=False,
        default='1.0.0'
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1
    )

    rating_count = models.IntegerField()

    # Required
    free = models.BooleanField(
        default=True
    )

    price = models.DecimalField(
        null=False,
        default=0.0,
        decimal_places=2,
        max_digits=6
    )

    currency = models.CharField(
        max_length=3,
        null=False,
        default='INR'
    )

    # Required
    size = models.CharField(
        max_length=5,
        null=False,
        blank=False
    )

    # Required
    developer_id = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    developer_website = models.URLField(
        default=""
    )

    # Required
    developer_email = models.EmailField(
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'apps'
        constraints = [
            models.UniqueConstraint(fields=['app_name', 'app_id'], name='unique_app')
        ]


class User(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    # Required
    username = models.CharField(
        max_length=250,
        null=False,
        blank=False
    )

    # Required
    emailid = models.EmailField(
        max_length=1000,
        null=False,
        blank=False,
    )

    # Required
    password = models.CharField(
        max_length=1000,
        null=False,
        blank=False
    )

    type = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        default="User"
    )

    class Meta:
        db_table = 'users'
        constraints = [
            models.UniqueConstraint(fields=['username', 'emailid'], name='unique_user')
        ]
