from django.shortcuts import render,redirect
from django.http import Http404
from .models import QueDoneByUser, QuestionList
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Below are Register, login and logout views

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('questions')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            new_user = form.save()
            QueDoneByUser.objects.create(owner=new_user)
            
            messages.success(request, 'Account was creatd for ' + user)
            return redirect('login')
        else:
            messages.warning(request, 'Failed to Register the user')

    context = {
        'form': form
    }
    return render(request, 'questionlist/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('questions')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('questions')
        else:
            messages.warning(request, 'Username or password is Incorrect') 

    context = {}
    return render(request, 'questionlist/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')



def returnQuestionTypes():
    question_type = {
        'Arrays' : 'array',
        'Dynamic Programing': 'dp',
        'Strings': 'string',
        'Maths': 'maths',
        'Greedy' : 'greedy',
        'DFS' : 'dfs',
        'Tree' : 'tree', 
        'Hash Table': 'hash table',
        'Binary Search': 'binary search',
        'BFS': 'bfs',
        'Two Pointer': 'two pointer',
        'BackTracking' : 'backtracking',
        'Stack' : 'stack',
        'Design' : 'design',
        'Graph' : 'graph', 
        'Bit Manipulation' : 'bit',
        'Linked List' : 'linked list',
        'HEAP' : 'heap',
        'Sliding Window' : 'sliding window',
        'trie' : 'trie',
        'Segment Tree': 'segment tree'
    }
    return question_type

@login_required(login_url='login')
def questions_list(request):
    """
        render a page with catagorization of all questions
    """
    question_type = returnQuestionTypes()

    questions = QuestionList.objects.all() 
    completed = QuestionList.objects.filter(quedonebyuser__owner = request.user.id)
    total_question = len(questions)
    complete_count = len(completed)
    incomplete_count = total_question - complete_count

    label = []
    data = []

    for key, val in question_type.items():
        label.append(key)
        data.append(len(QuestionList.objects.filter(topic=val)))
    
    questionData = {
        'label' : label,
        'data' : data
    }


    chartData = {
        "label" : ['completed counts', 'incompleted counts'],
        "data" : [complete_count, incomplete_count]
    }

    context = {
        'questions_type': question_type,
        'total_question': total_question,
        'complete_count': complete_count,
        'incomplete_count': incomplete_count,
        'chartData' : chartData,
        'questionData': questionData,
        'template' : 'base',
        'que_type' : None,
    }
        
    return render(request, 'questionlist/base.html', context =context)


@login_required(login_url='login')
def render_questions_of_a_type(request, que_type):
    """
    it list all the question for a particular type 
    Exampel:  questions of array only
    """
    question_type = returnQuestionTypes()
    questions = QuestionList.objects.filter(topic=que_type) # gets all question of a particular type
    questions_completed = QuestionList.objects.filter(quedonebyuser__owner = request.user.id).filter(topic=que_type)
    total_question = len(questions)
    complete_count = len(questions_completed)
    incomplete_count = total_question - complete_count


    extradata = {}                                          # dictationary for extra data
    for question in questions:                              # adding data into extra_data
        question_name = question.question.split('/')[-2]
        status = ""
        if question in questions_completed:
            status = "completed"
        else: 
            status = "incomplete"
        extradata[question.id] = (question_name, status)

    addOrRemove = {
        'add' : 'add',
        'remove' : 'remove',
    }

    questionData = {
        'label': ['complete_count', 'incomplete_count'],
        'data' : [complete_count, incomplete_count]
    }

    context = {
        'questions_type': question_type,
        'questions' : questions, 
        'extradata': extradata,
        'total_question': total_question,
        'complete_count': complete_count,
        'incomplete_count': incomplete_count,
        'que_type' : que_type,
        'return_id' : 'render',
        'questionData': questionData,
        'addOrRemove': addOrRemove,
        'template' : 'index',
    }


    return render(request, 'questionlist/index.html', context = context)


@login_required(login_url='login')
def completed_question(request, que_type, que_status):
    question_type = returnQuestionTypes()

    questions = QuestionList.objects.filter(topic=que_type) # gets all question of a particular type
    questions_completed = QuestionList.objects.filter(quedonebyuser__owner = request.user.id).filter(topic=que_type)
    
    required_questions = []

    if que_status == 'completed':
        required_questions = questions_completed
    else:
        for que in questions:
            if que not in questions_completed:
                required_questions.append(que)

    easy_count = medium_count = hard_count = 0
    extradata = {}                                          # dictationary for extra data
    for question in required_questions:                              # adding data into extra_data
        question_name = question.question.split('/')[-2]
        status = ""
        if question in questions_completed:
            status = "completed"
        else: 
            status = "incomplete"
        extradata[question.id] = (question_name, status)    # dictationary will be used to add extra data used in template
                                                            # which doesn't store in database
        if question.level == 'E':
            easy_count += 1
        elif question.level == 'M':
            medium_count += 1
        elif question.level == 'H':
            hard_count += 1

    levelData = {
        'label' : ['Easy', 'Medium', 'Hard'],
        'data' : [easy_count, medium_count, hard_count]
    }
    addOrRemove = {
        'add' : 'add',
        'remove' : 'remove',
    }

    context = {
        'questions_type': question_type,
        'questions' : required_questions, 
        'extradata': extradata,
        'levelData' : levelData,
        'easy_count' : easy_count,
        'medium_count' : medium_count,
        'hard_count' : hard_count,
        'que_type' : que_type,
        'que_status' : que_status,
        'return_id' : 'completed',
        'addOrRemove': addOrRemove,
        'template' : 'completed',
    }

    return render(request, 'questionlist/completed.html', context = context)

@login_required(login_url='login')
def changeQuestionStatus(request, que_id, que_type, que_status, return_id, addOrRemove):
    que_user = QueDoneByUser.objects.get(owner=request.user)            # getting the current user
    question = QuestionList.objects.get(id=int(que_id))                 # getting current question object from database using que_id
    if addOrRemove == 'add':
        que_user.questionlist.add(question)                             # adding the current question to user completed-qeustion list
    else:
        que_user.questionlist.remove(question)

    if return_id == 'render':
        return redirect('renderquestions', que_type=que_type)
    else: 
        return redirect('completed', que_type=que_type, que_status=que_status)
    








