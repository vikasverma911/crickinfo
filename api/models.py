from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class TeamMember(models.Model):
    team_name = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
