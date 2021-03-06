from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Name_of_quiz, Name_of_Question, Answer, Who_Answer

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Name_of_quiz.objects.order_by('-Date_of_public')[:5]


class DetailView(generic.DetailView):
    model = Name_of_Question
    template_name = 'polls/detail.html'
    context_object_name = "question"





class ResultsView(generic.DetailView):
    #model = Question
    model = Name_of_quiz
    template_name = 'polls/results.html'


def vote(request, pytanie_id):
    #question = get_object_or_404(Question, pk=question_id)
    pytanie = get_object_or_404(Pytanie,pk=pytanie_id)

    try:
        selected_choice = pytanie.choice_set.get(pk=request.POST['choice'])
        #selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'pytanie': pytanie,
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:

        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        smieszki = pytanie_id+1
        return HttpResponseRedirect(reverse('polls:detail', args=(smieszki)))
        #return HttpResponseRedirect(reverse('polls:results', args=(pytanie.id+1,)))