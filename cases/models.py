from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
#---------------------------------------------------------------------

class Client(Person):
    # Add client specific fields here (e.g., company name, address)
    def __str__(self) -> str:
        return super().__str__()
    
class Lawyer(Person):
    # Add lawyer specific fields here (e.g., bar number, specialization)
    def __str__(self) -> str:
        return super().__str__()

class Case(models.Model):
    STATUS_CHOICES = (
        ('OPEN','Open'),
        ('CLOSED','closed'),
        ('PENDING','Pending'),
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='OPEN')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title