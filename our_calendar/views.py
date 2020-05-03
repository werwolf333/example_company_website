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


class Test(View):
    errorMessages = []

    def validate(self, data_start, data_finish, args, request):
        self.errorMessages = []
        args['error_messages'] = self.errorMessages
        if data_start > data_finish:
            self.errorMessages.append('Дата окончания должна быть позже чем дата начала.')
        if data_start == "":
            self.errorMessages.append('Не указана дата начала')
        if data_finish == "":
            self.errorMessages.append('Не указана дата окончания')


class HolidayAdd(Test):

    def get(self, request):
        args = {}
        args['dates'] = OurCalendar.objects.all()
        args['mans'] = People.objects.all()
        args['this_man'] = ""
        args['username'] = auth.get_user(request).username
        return render(request, "our_calendar/our_calendar_form.html", args)

    def post(self, request):
        args = {}
        args['this_man'] = ""
        args['mans'] = People.objects.all()
        man_id = request.POST['worker']
        data_start = request.POST['data_start']
        data_finish = request.POST['data_finish']

        holiday = OurCalendar(
            man_id = man_id,
            data_start = data_start,
            data_finish = data_finish,
        )
        self.validate(data_start, data_finish, args, request)
        if(len(args['error_messages'])==0):
            holiday.save()
            return redirect("/calendar/")
        else:
            return render(request, "our_calendar/our_calendar_form.html", args)


class HolidayEdit(Test):

    def get(self, request, id):
        args = {}
        args['date'] = OurCalendar.objects.get(id=id)
        man_id = args['date'].man_id
        args['mans'] = People.objects.filter().exclude(id=man_id)
        args['this_man'] = People.objects.get(id=man_id)
        args['username'] = auth.get_user(request).username
        return render(request, "our_calendar/our_calendar_form.html", args)

    def post(self, request, id):
        args = {}
        args['mans'] = People.objects.all()
        args['date'] = OurCalendar.objects.get(id=id)
        man_id = args['date'].man_id
        args['this_man'] = People.objects.get(id=man_id)

        data_start = request.POST['data_start']
        data_finish = request.POST['data_finish']

        holiday = OurCalendar.objects.get(id=id)
        holiday.man_id = request.POST['worker']
        holiday.data_start = data_start
        holiday.data_finish = data_finish

        self.validate(data_start, data_finish, args, request)
        if (len(args['error_messages']) == 0):
            holiday.save()
            return redirect("/calendar/")
        else:
            return render(request, "our_calendar/our_calendar_form.html", args)


class HolidayDelete(View):
    def get(self, request, id):
        OurCalendar.objects.filter(id=id).delete()
        return redirect("/calendar/")
