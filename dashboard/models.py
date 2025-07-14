from django.db import models

class Dashboard(models.Model):
    profile = models.OneToOneField('accounts.Profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.profile.user.username}'s Dashboard"
