import uuid
from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
from django.contrib.auth.models import User


class Appointment(models.Model):
    """This is an appointments between one takeruser and one giveruser"""

    STATUS = (
        ('C', 'Created'),
        ('a', 'Accepted'),
        ('p', 'Paid'),
        ('t', 'Taken'),
        ('x', 'Cancelled'),
        ('r', 'Reprogrammed'),
    )

    # Fields
    id = models.UUIDField(
        max_length=32,
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

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
        null=True,
        help_text='Taker user')
    giver_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_giver_user',
        null=True,
        help_text='Giver user')
    starting_at = models.DateTimeField(help_text='Start datetime')
    ending_at = models.DateTimeField(
        help_text='Expected end datetime',
        null=True)
    ended_at = models.DateTimeField(
        help_text='Effective end datetime',
        null=True)
    paid = models.DecimalField(
        help_text='Amount paid',
        max_digits=10,
        decimal_places=4)
    feedback = models.CharField(
        max_length=1,
        help_text='Feedback given by giver')
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
        return self.id
