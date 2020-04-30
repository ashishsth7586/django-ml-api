from django.db import models


class Approval(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    GRADUATED_CHOICES = (
        ('Graduate', 'Graduated'),
        ('Not_Graduate', 'Not_Graduate')
    )

    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dependant = models.IntegerField(default=0)
    applicant_income = models.IntegerField(default=0)
    coapplicant_income = models.IntegerField(default=0)
    loan_amount = models.IntegerField(default=0)
    loan_term = models.IntegerField(default=0)
    credit_history = models.IntegerField(default=0)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    graduate_education = models.CharField(max_length=25, choices=GRADUATED_CHOICES)
    self_employed = models.CharField(max_length=25, choices=SELFEMPLOYED_CHOICES)
    area = models.CharField(max_length=25, choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.first_name + '' + self.last_name
