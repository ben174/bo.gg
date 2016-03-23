from django.db import models

from bogg.users.models import User


class CalorieLog(models.Model):
    user = models.ForeignKey(User)
    CALORIE_LOG_TYPE_CHOICES = (
        ('E', 'Eaten'),
        ('X', 'Exercise'),
    )
    calories = models.IntegerField(
        verbose_name='Calories consumed or explled during this activity.',
        name='Calories Consumed',
    )
    created = models.DateTimeField(auto_now_add=True)
    log_date = models.DateTimeField(auto_now=True)
    log_type = models.CharField(max_length=1, choices=CALORIE_LOG_TYPE_CHOICES, default='E')
    note = models.CharField(max_length=1000, null=True, blank=True)


class WeightLog(models.Model):
    user = models.ForeignKey(User)
    weight = models.DecimalField(
        verbose_name='Weight at the time the entry was created.',
        name='Logged Weight',
        decimal_places=2,
        max_digits=6,
    )
    created = models.DateTimeField(auto_now_add=True)
    log_date = models.DateField(auto_now=True)
    note = models.CharField(max_length=1000, null=True, blank=True)

    def save(self):
        self.user.weight = WeightLog.objects.latest('log_date').weight
        self.user.save()
        self.save()
