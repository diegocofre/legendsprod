import uuid
from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
from django.contrib.auth.models import User


class Appointment(models.Model):
    """This is an appointments between one takeruser and one giveruser"""

    STATUS = (
        ('C', 'Created'),
        ('A', 'Accepted'),
        ('P', 'Paid'),
        ('T', 'Taken'),
        ('X', 'Cancelled'),
        ('R', 'Reprogrammed'),
    )

    # Fields
    id = models.UUIDField(
        max_length=32,
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    # externalid = models.UUIDField(max_length=32)

    description = models.CharField(
        max_length=640,
        help_text='Description of the appointment')

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='c',
        help_text='Appointment Current Status',
    )

    taker_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_taker_user',
        help_text='Taker user')
    giver_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_giver_user',
        help_text='Giver user')
    starting_at = models.DateTimeField(help_text='Start datetime')
    ending_at = models.DateTimeField(
        help_text='Expected end datetime',
        null=True)
    ended_at = models.DateTimeField(
        help_text='Effective end datetime',
        null=True,
        blank= True)
    paid = models.DecimalField(
        help_text='Amount paid',
        max_digits=10,
        decimal_places=4,
        null=True,
        blank=True
        )
    feedback = models.CharField(
        max_length=1024,
        help_text='Feedback given by giver',
        null= True,
        blank=True
        )
    created_at = models.DateTimeField(
        help_text='Effective end datetime',
        auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ['id', 'starting_at']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Appointment"""
        return reverse('appointment', args=[str(self.id)])

    def __str__(self):
        """String for representing the Appointment object"""
        return str(self.id)
