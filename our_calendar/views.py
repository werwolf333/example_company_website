from django.shortcuts import render
from django.views.generic import View
from our_calendar.models import OurCalendar
from django.contrib import auth


class Index(View):

    def get(self, request):
        args = {}
        args['dates'] = OurCalendar.objects.all()
        args['username'] = auth.get_user(request).username
        return render(request, "our_calendar/our_calendar_list.html", args)


class HolidayAdd(View):
    pass


class HolidayEdit(View):
    pass


class HolidayDelete(View):
    pass
