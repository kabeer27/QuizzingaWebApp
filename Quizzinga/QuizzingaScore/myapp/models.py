from django.db import models
class Quiz(models.Model):
	quiz_name = models.CharField(max_length = 200)

class Question(models.Model):
	question_text = models.CharField(max_length = 300)

	def __str__(self):
		return self.question_text


class Team(models.Model):
	team_name = models.CharField(max_length = 200)
	team_score = models.IntegerField(default = 0)
	quiz_id = models.ForeignKey(Quiz, on_delete = models.CASCADE)
	def __str__(self):
		return (self.team_name + "\n" + str(self.team_score))

	def set_score(self, points):
		self.team_score += points

	def get_score(self):
		return self.team_score 

class Member(models.Model):
	member_name = models.CharField(max_length = 200)
	team = models.ForeignKey(Team, on_delete = models.CASCADE)

class Score(models.Model):
	quiz_id = models.ForeignKey(Quiz, on_delete = models.CASCADE)
	bounce_points = models.IntegerField(default = 10)
	bounce_points_negative = models.IntegerField(default = 0)
	pounce_points = models.IntegerField(default = 10)
	pounce_points_negative = models.IntegerField(default = -10)



# Create your models here.
