from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Answer, Participant, Message
from .forms import Create_question, Create_answer
from django.contrib.auth import login, authenticate, logout


def index(request):
    template_index = loader.get_template('polls/index.html')
    return HttpResponse(template_index.render(None, request))


def article(request, number):
    template_new = loader.get_template('polls/temple.html')
    f1 = f2 = 1
    link = []
    for i in range(number):
        f1, f2 = f2, f1 + f2
        link.append(f1)
    context = {'fib': link}
    return HttpResponse(template_new.render(context, request))


def fib(request):
    template_new = loader.get_template('polls/temple.html')
    context = {'fib': list(range(11))}
    return HttpResponse(template_new.render(context, request))


def greet(request):
    template_name = loader.get_template('polls/greeter.html')
    context = None
    return HttpResponse(template_name.render(context, request))


def greeting(request, username, lastname):
    template_name = loader.get_template('polls/greeter.html')
    context = {'username': username, 'lastname': lastname}
    return HttpResponse(template_name.render(context, request))


def test(request):
    template_test = loader.get_template('polls/new_file.html')
    return HttpResponse(template_test.render(None, request))


def header(request):
    template_blog = loader.get_template('polls/header.html')
    context = {'user': request.user}
    return HttpResponse(template_blog.render(context, request))


def questions(request):
    template_page = loader.get_template('polls/questions.html')
    quest = Question.objects.all()[::-1]
    context = {
        'questions': quest,
        'user': request.user
    }
    return HttpResponse(template_page.render(context, request))


def answers(request):
    template_page = loader.get_template('polls/answers.html')
    answ = Answer.objects.all()
    quest = Question.objects.all()
    context = {
        'answers': answ,
        'questions': quest,
    }
    return HttpResponse(template_page.render(context, request))


def create_question(request):
    template_creating = loader.get_template('polls/new_question.html')
    # Проверка, какой запрос
    if request.method == 'POST':  # Это не только проверка: POST или не POST, а еще и проверка заполнености формы
        '''Прежде всего импортируем класс из forms.py || потом создаем экземпляр(в данном случае: question_form)'''
        '''Вывод в полях формы выводится (или остается) текст, там введенный'''
        form = Create_question(data=request.POST)
        if form.is_valid():  # Если всё корректно, выводим в терминал всё что нужно
            user = Participant.objects.get(id=request.user.id)
            question_data = Question(question_text=form.data['question_text'], user_id=user)
            question_data.save()
            form = Create_question()
        # Занесение записей в БД
        '''question = Question(question_text=request.POST['question_text'])
        question.save()'''
    else:  # Если форма пустая то отображается пустая форма
        form = Create_question()
    context = {
        'form': form
    }
    return HttpResponse(template_creating.render(context, request))


def create_answer(request, question_id):
    temple_answer_creating = loader.get_template('polls/new_answer.html')
    questions = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = Create_answer(data=request.POST)
        if form.is_valid():
            user = Participant.objects.get(id=request.user.id)
            form = form.save(commit=False)
            form.user = user
            form.save()
    form = Create_answer()
    context = {
        'quest': questions,
        'form': form,
        'user': request.user.id
    }
    return HttpResponse(temple_answer_creating.render(context, request))


def auth(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print('something', name, password)
        user = authenticate(request, username=name, password=password)
        info = (user, password, name)
        for i in info:
            print(i, type(i))
        if user != None:
            print(type(user.id))
            login(request, user)
            context = {'id': user.id}
            return HttpResponseRedirect("user")
        else:
            context = {'id': None}
            return HttpResponseRedirect("/polls/blog/")


def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        user_password = request.POST['password']
        pass_again = request.POST['repeat_password']
        first_name = request.POST['firstname']
        phone_number = request.POST['tel_number']
        last_name = request.POST['lastname']
        # print(request.POST)
        # print(name, first_name, last_name, phone_number)
        if pass_again == user_password:
            print(user_password)
            new_user = Participant.objects.create_user(first_name=first_name, last_name=last_name,
                                                       phone_number=phone_number,
                                                       username=name, password=user_password)
            new_user.save()
            login(request, new_user)
        else:
            print('invalid password, Try again')
    return HttpResponseRedirect('/polls/blog')


def account(request):
    # print(dir(request.user))
    # print(request.user.id)
    # print(type(request.user.id))
    template = loader.get_template('polls/account.html')
    if request.user.is_anonymous:
        alt_template = loader.get_template('polls/alt_profile.html')
        return HttpResponse(alt_template.render(None, request))
    user = Participant.objects.get(id=request.user.id)
    questions = Question.objects.filter(user_id=user)
    answers = Answer.objects.filter(user=user)
    context = {'user': user, 'questions': questions, 'answers': answers}
    return HttpResponse(template.render(context, request))


def change_question(request, id):
    question = Question.objects.get(id=id)
    print('something')
    if request.method == 'POST':
        question.question_text = request.POST['question_text']
        question.save()
    return HttpResponseRedirect("/polls/blog/user")


def change_answer(request, id):
    answer = Answer.objects.get(id=id)
    if request.method == 'POST':
        answer.answer_text = request.POST['answer_text']
        answer.save()
    return HttpResponseRedirect("/polls/blog/user")


def analytics(request):
    template = loader.get_template('polls/analytics.html')
    all_answers = Answer.objects.all()
    all_questions = Question.objects.all()
    question_count = []
    for question in all_questions:
        answer_list = Answer.objects.filter(question=question)
        question_count.append((question, len(answer_list)))
    print(question_count)
    print(request.user)

    def sorting(question):
        return question.question_text

    alternative_questions = list(map(sorting, list(all_questions)))
    print(sorted(alternative_questions))
    context = {
        'questions': all_questions,
        'answers': all_answers,
        'q_count': question_count,
        'all_answer_count': len(all_answers)
    }
    return HttpResponse(template.render(context, request))


def users_analytics(request):
    template = loader.get_template('polls/users_analytics.html')
    all_user = Participant.objects.all()
    data = []
    for user in all_user:
        if user.username != request.user.username:
            data.append([user, user.get_full_name(), Question.objects.filter(user_id=user), Answer.objects.filter(user=user)])
    context = {'users_data': data}
    return HttpResponse(template.render(context, request))


def user_logout(request):
    logout(request)
    for i in Participant.objects.all():
        print(i.is_authenticated)
    return HttpResponseRedirect('/polls/blog')


def change_data(request):
    template = loader.get_template('polls/change_data.html')
    all_questions = Question.objects.filter(user_id=request.user.id)
    all_answers = Answer.objects.filter(user=request.user.id)
    user = Participant.objects.get(id=request.user.id)

    # print(request.FILES['avatar'])
    if request.method == 'POST':
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.self_description = request.POST['self_description']
        user.birthday = request.POST['birthday']
        user.phone_number = request.POST['phone_number']
        user.avatar = request.FILES['avatar']

        user.save()
        return HttpResponseRedirect('/polls/blog/user')

    context = {
        'user': user,
        'questions': all_questions,
        'answers': all_answers
    }
    return HttpResponse(template.render(context, request))


def user_profile(request, user_id):
    template = loader.get_template('polls/profile.html')
    user = Participant.objects.get(id=user_id)
    context = {'user': user}
    return HttpResponse(template.render(context, request))


def message(request):
    template = loader.get_template('polls/messages.html')
    get_messages = Message.objects.filter(host=request.user)
    send_messages = Message.objects.filter(sender=request.user)
    context = {'host': get_messages, 'send': send_messages}
    return HttpResponse(template.render(context, request))


def write_message(request):
    print(request.POST['host'])
    if request.user.is_anonymous:
        return HttpResponseRedirect('polls/alt_profile.html')
    else:
        user = Participant.objects.get(id=request.user.id)
        if request.method == 'POST':
            message_text = request.POST['message']
            host = Participant.objects.get(id=request.POST['host'])
            new_message = Message(sender=user, host=host, message=message_text)
            new_message.save()
        return HttpResponseRedirect('/polls/blog/analytics/users')


def delete_message(request, id):
    message = Message.objects.get(id=int(id))
    message.delete()
    return HttpResponseRedirect('/polls/blog/messages')
