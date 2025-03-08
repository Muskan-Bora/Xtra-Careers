from django import forms
from .models import Payment
from .models import candidate_cv

class PaymentForm(forms.ModelForm):
    EXPERIENCE_CHOICES = Payment.EXPERIENECE_CHOICES
    SERVICES_CHOICES = Payment.SERVICES_CHOICES
    
    name = forms.CharField(
        max_length = 500,
        widget = forms.TextInput(attrs={
            'placeholder' : 'Enter Your Full Name',
            'class' : 'form-control',
        }),
        label = "Full Name"
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control',
        }),
        label="Email Address"
    )
    
    contact = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your contact number',
            'class': 'form-control',
        }),
        label="Contact Number"
    )
    
    experience_level = forms.ChoiceField(
        choices = EXPERIENCE_CHOICES,
        widget = forms.RadioSelect(attrs={'class': 'experience-choice'}),
        label = "Experience Level"
    )
    
    selected_services = forms.MultipleChoiceField(
        choices = SERVICES_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={'class': 'services-choice'}),
        label = "Select Services"
    )
    
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=1.00,  # Minimum amount of ₹1
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter the amount to pay (₹1 or more)',
            'class': 'form-control',
        }),
        label="Amount",
        initial=1.00,  # Default to ₹1
    )
    
    class Meta: 
        model = Payment
        fields = ['name', 'email', 'contact', 'experience_level', 'selected_services', 'amount']
        
def clean_amount(self):
        amount_in_inr = self.cleaned_data.get('amount')
        if amount_in_inr:
            # Convert amount to paise (₹1 = 100 paise)
            return int(amount_in_inr * 100)
        return amount_in_inr
    
VETERAN_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

class candidatecvform(forms.Form):
    cv_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Full Name'}),
        max_length=500,
        required=True
    )
    
    cv_contact = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': '1234567890'}),
        required=True
    )
    
    cv_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'email@gmail.com'}),
        required=True
    )
    
    key_skills = forms.CharField(
        widget=forms.Textarea(attrs={'cols':20, 'rows':1, 'style': 'resize:vertical;horizontal', 'placeholder': 'List your Key Skills...',}),
        required=False,
    )
    
    cv_total_experience = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Years of Experience'}),
        required=False,
    )
    
    cv_undergraduate = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Undergraduate Degree'}),
        required=False,
    )

    cv_postgraduate = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Postgraduate Degree'}),
        required=False,
    )
    
    cv_certifications = forms.CharField(
        widget=forms.Textarea(attrs={'cols':20, 'rows':2, 'style': 'resize:vertical;horizontal', 'placeholder': 'Enter your Achievements...',}),
        required=False,
    )
    
    veteran_status = forms.ChoiceField(
        choices=VETERAN_CHOICES, 
        required=True, 
        label="Are you a veteran?",
        widget=forms.Select(attrs={'placeholder': 'Are you a veteran?'})
    )
    
    resumes = forms.FileField(required=True)

    def clean_resumes(self):
        resumes = self.cleaned_data.get('resumes')
        if resumes:
            # Check file size (max 1MB)
            if resumes.size > 2 * 1024 * 1024:
                raise forms.ValidationError("File size must be under 5MB.")
            # Check file extension (only .pdf allowed)
            if not resumes.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
        return resumes
    
    class Meta:
        model = candidate_cv
        fields = ['cv_name', 'cv_contact', 'cv_email', 'key_skills', 'cv_total_experience', 'cv_undergraduate', 'cv_postgraduate',  'cv_certifications', 'veteran_status', 'resumes']