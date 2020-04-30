from django.shortcuts import render, redirect
from django.views.generic import View
from our_calendar.models import OurCalendar
from django.contrib import auth
from people.models import People


class Index(View):

    def get(self, request):
        args = {}
        args['dates'] = OurCalendar.objects.all()
        args['username'] = auth.get_user(request).username
        return render(request, "our_calendar/our_calendar_list.html", args)


class HolidayAdd(View):

    def get(self, request):
        args = {}
        args['dates'] = OurCalendar.objects.all()
        args['mans'] = People.objects.all()
        args['this_man'] = ""
        args['username'] = auth.get_user(request).username
        return render(request, "our_calendar/our_calendar_form.html", args)

    def post(self, request):
        holiday = OurCalendar(
            man_id = request.POST['worker'],
            data_start = request.POST['data_start'],
            data_finish = request.POST['data_finish'],
        )
        holiday.save()
        return redirect("/calendar/")


class HolidayEdit(View):
    pass


class HolidayDelete(View):
    pass
