from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    # You can add more fields like project URL, date, and so on as needed.

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Use null=True and blank=True to allow for ongoing experiences.

    def __str__(self):
        return self.title

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    # You can use a function to automatically generate the image URL from the link, or manually add it if needed.
    image = models.URLField(blank=True, null=True, help_text="Leave blank to generate automatically")

    def __str__(self):
        return self.name
    
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    document = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.institution}"

class Achievement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    achievement_date = models.DateField()

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    document = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

