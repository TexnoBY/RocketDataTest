from django.contrib.auth.models import User
from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100, verbose_name='Position title')
    description = models.TextField(verbose_name='Position description')

    def __str__(self):
        return self.title


class Employer(User):
    full_name = models.CharField(editable=False, default='', max_length=150)
    second_name = models.CharField(default='', max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    level = models.IntegerField(editable=False, default=1)
    boss = models.ForeignKey('self',
                             verbose_name='Leader',
                             blank=True, null=True,
                             on_delete=models.CASCADE)
    total_salary_paid = models.DecimalField(blank=True, max_digits=7, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Employers"

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.second_name + ' ' + self.last_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name



class TeamLeader(Employer):

    def save(self, *args, **kwargs):
        self.level = 2
        super().save(*args, **kwargs)

    class Meta:

        verbose_name_plural = "Team Leaders"


class DepartmentLeader(Employer):

    def save(self, *args, **kwargs):
        self.level = 3
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Department Leaders"


class VicePresident(Employer):

    def save(self, *args, **kwargs):
        self.level = 4
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Vice-Presidents"


class President(Employer):

    def save(self, *args, **kwargs):
        self.level = 5
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Presidents"
