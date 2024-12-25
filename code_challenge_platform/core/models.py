# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    skills = models.TextField(null=True, blank=True)  # Can store as a comma-separated list of skills
    points = models.IntegerField(default=0)  # Tracks total points

    def add_points(self, points):
        """Adds points to the user."""
        self.points += points
        self.save()

    def __str__(self):
        return self.username
        

# models.py
from django.db import models

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    input_format = models.TextField()
    output_format = models.TextField()
    examples = models.TextField()
    template_code = models.TextField(default="") 

    def __str__(self):
        return self.title

class TestCase(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='test_cases', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()


class UserChallenge(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="completed_challenges")
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name="completed_by_users")
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"
    

class Contest(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_contests")
    name = models.CharField(max_length=255)
    entry_code = models.CharField(max_length=10, unique=True)  # Random code for joining
    challenges = models.ManyToManyField(Challenge, related_name="contests")
    start_time = models.DateTimeField()
    duration = models.DurationField()  # Length of the contest
    is_active = models.BooleanField(default=True)  # To deactivate completed contests

    def end_time(self):
        """Calculate the contest end time."""
        return self.start_time + self.duration

    def __str__(self):
        return self.name


class ContestParticipant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="contest_participations")
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name="participants")
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.contest.name}"


class ContestSubmission(models.Model):
    participant = models.ForeignKey(ContestParticipant, on_delete=models.CASCADE, related_name="submissions")
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.participant.user.username} - {self.challenge.title} - {self.score} points"
