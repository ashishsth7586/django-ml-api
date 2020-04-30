from django import forms

class ApprovalForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    MARRIED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    GRADUATED_CHOICES = [
        ('Graduate', 'Graduated'),
        ('Not_Graduate', 'Not_Graduate')
    ]

    SELFEMPLOYED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    PROPERTY_CHOICES = [
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    ]
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    Dependents = forms.IntegerField()
    ApplicantIncome = forms.IntegerField()
    CoapplicantIncome = forms.IntegerField()
    LoanAmount = forms.IntegerField()
    Loan_Amount_Term = forms.IntegerField()
    Credit_History = forms.IntegerField()
    Gender = forms.ChoiceField(choices=GENDER_CHOICES)
    Married = forms.ChoiceField(choices=MARRIED_CHOICES)
    Education = forms.ChoiceField( choices=GRADUATED_CHOICES)
    Self_Employed = forms.ChoiceField(choices=SELFEMPLOYED_CHOICES)
    Property_Area = forms.ChoiceField(choices=PROPERTY_CHOICES)
