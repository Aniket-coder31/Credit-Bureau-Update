# views.py
from django.shortcuts import render, redirect
from .models import Question, UserResponse
from django.contrib.auth.decorators import login_required

def calculate_credit_score(user):
    responses = UserResponse.objects.filter(user=user)
    total_score = sum(response.score for response in responses)
    return total_score

@login_required
def question_view(request):
    questions = Question.objects.all()
    
    if request.method == 'POST':
        answers = request.POST.getlist('answers')
        for i, answer in enumerate(answers):
            question = questions[i]
            score = getattr(question, f'score_{answer.lower()}')
            UserResponse.objects.create(
                user=request.user,
                question=question,
                answer=answer,
                score=score
            )
        return redirect('results')

    return render(request, 'questions.html', {'questions': questions})

@login_required
def results_view(request):
    score = calculate_credit_score(request.user)
    return render(request, 'results.html', {'score': score})

