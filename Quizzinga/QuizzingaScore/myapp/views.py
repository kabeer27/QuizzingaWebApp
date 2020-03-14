from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Question, Team, Member, Quiz, Score
# Create your views here.

def index(request):
	quiz_list = Quiz.objects.all()
	context = {
		'quiz_list': quiz_list
	}
	return render(request, 'myapp/index.html', context)

def detail(request, quiz_id):
	try:
		quiz = Quiz.objects.get(pk = quiz_id)
	except quiz.DoesNotExist:
		raise Http404("Quiz does not exist")
	#teams = Team.objects.filter()
	team_list = Team.objects.filter(quiz_id = quiz)
	score = Score.objects.get(quiz_id = quiz)
	context = {
		'quiz': quiz,
		'team_list': team_list,
		'score': score
	}
	return render(request, 'myapp/quiz_display.html', context)

def results(request, quiz_id, team_id ):
	try:
		quiz = Quiz.objects.get(pk = quiz_id)
	except quiz.DoesNotExist:
		raise Http404("Quiz does not exist")

	try:
		team = Team.objects.get(pk = team_id)
	except team.DoesNotExist:
		raise Http404("Team does not exist")

	member_list = Member.objects.filter(team_id = team)

	context = {
		'team' : team,
		'member_list': member_list
	}
	return render(request, 'myapp/team_display.html', context)

def ajax_change_score(request):
	team_id = request.POST.get('team_id', 0)
	points = request.POST.get('points', 0)
	
	try:
		team = Team.objects.get(pk = team_id)
		team.team_score += int(points)
		team.save()
		return JsonResponse({"success": True})
	except Exception as e:
		return JsonResponse({"success": False})

def leaderboard(request, quiz_id):
	try:
		quiz = Quiz.objects.get(pk = quiz_id)
	except quiz.DoesNotExist:
		raise Http404("Quiz does not exist")

	unordered_team_list = Team.objects.filter(quiz_id = quiz_id)
	temp_list = []
	for team in unordered_team_list:
		temp_list.append((-team.team_score,team.id))
	temp_list.sort()
	ordered_team_list = []
	for team in temp_list:
		ordered_team_list.append(Team.objects.get(pk = team[1]))

	context = {
		'team_list': ordered_team_list,
		'quiz': quiz
	}
	return render(request, 'myapp/leaderboard.html', context)

	
