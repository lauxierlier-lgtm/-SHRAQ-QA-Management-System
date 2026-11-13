from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project, Bug, TestCase
from .forms import ProjectForm, BugForm, TestCaseForm


# ==============================
# PROJECT MANAGEMENT
# ==============================

@login_required
def projects_view(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()

            return redirect('projects')

    else:
        form = ProjectForm()

    projects = Project.objects.filter(
        created_by=request.user
    ).order_by('-created_at')

    return render(request, 'core/projects.html', {
        'form': form,
        'projects': projects
    })


# ==============================
# BUG TRACKING
# ==============================

@login_required
def bugs_view(request):

    if request.method == 'POST':
        form = BugForm(request.POST)

        form.fields['project'].queryset = Project.objects.filter(
            created_by=request.user
        )

        if form.is_valid():
            bug = form.save(commit=False)
            bug.reported_by = request.user
            bug.save()

            return redirect('bugs')

    else:
        form = BugForm()

        form.fields['project'].queryset = Project.objects.filter(
            created_by=request.user
        )

    bugs = Bug.objects.filter(
        reported_by=request.user
    ).select_related('project').order_by('-created_at')

    return render(request, 'core/bugs.html', {
        'form': form,
        'bugs': bugs
    })


# ==============================
# TEST CASE MANAGEMENT
# ==============================

@login_required
def testcases_view(request):

    if request.method == 'POST':
        form = TestCaseForm(request.POST)

        form.fields['project'].queryset = Project.objects.filter(
            created_by=request.user
        )

        if form.is_valid():
            testcase = form.save(commit=False)
            testcase.created_by = request.user
            testcase.save()

            return redirect('testcases')

    else:
        form = TestCaseForm()

        form.fields['project'].queryset = Project.objects.filter(
            created_by=request.user
        )

    testcases = TestCase.objects.filter(
        created_by=request.user
    ).select_related('project').order_by('-created_at')

    return render(request, 'core/testcases.html', {
        'form': form,
        'testcases': testcases
    })