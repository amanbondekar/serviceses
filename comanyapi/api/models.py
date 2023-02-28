from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator,ValidationError
# Create your models here.
#creating comany model
class Company(models.Model):

    company_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z ]+$', 'Name can only contain letters and spaces.')])
    location=models.CharField(max_length=50)
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                          ('non IT','non IT'),
                          ('mobile phones','mobile phones')
                          ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name  +'--'+ self.location
def validate_image_size(value):
    file_size = value.size
    if file_size > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")


class Image(models.Model):
    image = models.ImageField(upload_to='employee_images')

    ##Employee Model
class Employee(models.Model):
    
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2), RegexValidator(r'^[a-zA-Z ]+$', 'Name can only contain letters and spaces.')])
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    about=models.TextField()
    images = models.ManyToManyField('Image')



    position=models.CharField(max_length=50,choices=(
       ('manager','manager'),
        ('softwere Developer','sd'),
        ('Project Leader','pl')
    ))

   
    company = models.ForeignKey(Company, on_delete=models.CASCADE)