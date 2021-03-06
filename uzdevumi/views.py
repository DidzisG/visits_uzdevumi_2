from django.shortcuts import render
from django.http import HttpResponse

from .forms import VisitForm, VisitorNameForm
from .models import Visit


def filter_visits_by_visitor(request):

    form = VisitorNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visitor_name = form.cleaned_data['visitor_name']
            visits = Visit.objects.filter(visitor=visitor_name)

            context = {
                'visits': visits,
            }

            return render(
                request,
                template_name='visits.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='visit_form.html',
        context=context,
    )



def get_all_visits(request):

    visits = Visit.objects.all()

    context = {
        'visits': visits,
    }

    return render(
        request,
        template_name='visits.html',
        context=context,
    )


def get_visit(request, visit_id):

    visit = Visit.objects.get(id=visit_id)

    context = {
        'visit': visit,
    }

    return render(
        request,
        template_name='visit.html',
        context=context,
    )


def add_visit(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visit = Visit(
                visitor=form.cleaned_data['visitor'],
                reason=form.cleaned_data['reason'],
                date_time=form.cleaned_data['date_time'],
            )

            visit.save()

            context = {
                'visit': visit,
            }

            return render(
                request,
                template_name='visit.html',
                context=context,
            )

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
    )
