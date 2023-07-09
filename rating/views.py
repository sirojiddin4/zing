# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Lesson, Credit, Student
from django.db.models import Count

def home(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
  
    return render(request,'zing/base.html',{})

def search_group(request):
    if request.method == 'POST':
        group_id = request.POST.get('group')
        if group_id:
            return redirect('credit_table', group_id=group_id)
    
    groups = Group.objects.all()
    return render(request, 'zing/search_group.html', {'groups': groups})

def credit_table(request, group_id):
    selected_group = get_object_or_404(Group, id=group_id)
    lessons = Lesson.objects.filter(course=selected_group.course)
    students = selected_group.student_set.all()
    
    num_lessons = lessons.count()
    max_credits = num_lessons * 4
    
    table_data = []
    for student in students:
        row_data = {'student': student, 'credits': []}
        total_credits = 0
        num_classes_with_credits = Credit.objects.filter(student=student, lesson__in=lessons, amount__gt=0).values('lesson').distinct().count()
        for lesson in lessons:
            credit = Credit.objects.filter(student=student, lesson=lesson).first()
            if credit:
                credit_value = credit.amount
                total_credits += credit_value
                row_data['credits'].append(credit_value)
        percentage = (num_classes_with_credits / num_lessons) * 100 if num_lessons > 0 else 0
        row_data['percentage'] = round(percentage, 2)
        row_data['average_credit'] = round(total_credits / num_classes_with_credits, 2) if num_classes_with_credits > 0 else 0
        table_data.append(row_data)
    
    table_data.sort(key=lambda row: (row['percentage'], row['average_credit']), reverse=True)
    
    return render(request, 'zing/credits.html', {'selected_group': selected_group, 'table_data': table_data})

def edit_credit(request, student_id, group_id):
    student = get_object_or_404(Student, id=student_id)
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        # Process the form data and save the credit record
        lesson_ids = request.POST.getlist('lesson')
        amounts = request.POST.getlist('amount')

        for lesson_id, amount in zip(lesson_ids, amounts):
            lesson = get_object_or_404(Lesson, id=lesson_id)
            credit, created = Credit.objects.get_or_create(student=student, lesson=lesson)
            if amount == "":
                amount = 0
            credit.amount = amount
            credit.save()

        return redirect('credit_table', group_id=group_id)

    lessons = group.course.lesson_set.all()
    credits = Credit.objects.filter(student=student, lesson__in=lessons)

    return render(request, 'zing/edit_credit.html', {'student': student, 'group': group, 'lessons': lessons, 'credits': credits})
