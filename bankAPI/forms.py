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
    CREDIT_HISTORY_CHOICES = [
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3)
    ]
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter last Name'}))
    Dependents = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter No. of dependants'}))
    ApplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter applicants income'}))
    CoapplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter coapplicants income'}))
    LoanAmount = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter loan amount'}))
    Loan_Amount_Term = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter loan amount term'}))
    Credit_History = forms.ChoiceField(choices=CREDIT_HISTORY_CHOICES)
    Gender = forms.ChoiceField(choices=GENDER_CHOICES)
    Married = forms.ChoiceField(choices=MARRIED_CHOICES)
    Education = forms.ChoiceField( choices=GRADUATED_CHOICES)
    Self_Employed = forms.ChoiceField(choices=SELFEMPLOYED_CHOICES)
    Property_Area = forms.ChoiceField(choices=PROPERTY_CHOICES)
