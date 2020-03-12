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
	
def quiz_display(request):
	quiz_id = int(request.path([-2]))

	quiz = Quiz.objects.get(pk = quiz_id)
	team_list = Team.objects.filter(quiz_id = quiz_id)
	score = score.objects.get(quiz_id = quiz_id)

	context = {
		'quiz': quiz,
		'team_list': team_list,
		'score': score
	}
	return JsonResponse(render_to_response('myapp/quiz_display.html',context))