from django.db import models

class Resume(models.Model):
    # Personal Information
    name = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    age = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    
    # Skills
    skill1 = models.CharField(max_length=50, blank=True)
    skill2 = models.CharField(max_length=50, blank=True)
    skill3 = models.CharField(max_length=50, blank=True)
    skill4 = models.CharField(max_length=50, blank=True)
    skill5 = models.CharField(max_length=50, blank=True)
    
    # Education
    degree1 = models.CharField(max_length=100, blank=True)
    college1 = models.CharField(max_length=200, blank=True)
    year1 = models.CharField(max_length=10, blank=True)
    degree2 = models.CharField(max_length=100, blank=True)
    college2 = models.CharField(max_length=200, blank=True)
    year2 = models.CharField(max_length=10, blank=True)
    degree3 = models.CharField(max_length=100, blank=True)
    college3 = models.CharField(max_length=200, blank=True)
    year3 = models.CharField(max_length=10, blank=True)
    
    # Languages
    lang1 = models.CharField(max_length=50, blank=True)
    lang2 = models.CharField(max_length=50, blank=True)
    lang3 = models.CharField(max_length=50, blank=True)
    
    # Projects
    project1 = models.CharField(max_length=150, blank=True)
    durat1 = models.CharField(max_length=50, blank=True)
    desc1 = models.TextField(blank=True)
    project2 = models.CharField(max_length=150, blank=True)
    durat2 = models.CharField(max_length=50, blank=True)
    desc2 = models.TextField(blank=True)
    
    # Experience
    company1 = models.CharField(max_length=150, blank=True)
    post1 = models.CharField(max_length=100, blank=True)
    duration1 = models.CharField(max_length=50, blank=True)
    lin11 = models.TextField(blank=True)
    company2 = models.CharField(max_length=150, blank=True)
    post2 = models.CharField(max_length=100, blank=True)
    duration2 = models.CharField(max_length=50, blank=True)
    lin21 = models.TextField(blank=True)
    
    # Achievements
    ach1 = models.CharField(max_length=200, blank=True)
    ach2 = models.CharField(max_length=200, blank=True)
    ach3 = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Resume - {self.name or 'Unnamed'}"