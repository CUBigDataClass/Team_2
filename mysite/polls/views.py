from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic


from .models import Question, Choice

class IndexView(generic.ListView):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_text for q in latest_question_list])
	#template = loader.get_template('polls/index.html')
	#context = {
	#	'latest_question_list':latest_question_list,
	#}
	#return HttpResponse(template.render(context, request))
	#return render(request, 'polls/index.html', context)
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	# try:
	# 	question = Question.objects.get(pk = question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	#question = get_object_or_404(Question, pk = question_id)
	#return render(request, 'polls/detail.html', {'question': question})
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(DetailView):
	#question = get_object_or_404(Question, pk = question_id)
	#return render(request, 'polls/results.html', {'question': question})
	# response = "You're looking at the results of question %s."
	# return HttpResponse(response % question_id)
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))