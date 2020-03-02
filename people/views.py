from django.contrib import auth
from django.shortcuts import render, redirect
from django.views import View
from people.models import People


class PeopleList(View):
    template_name = 'people/people_list.html'

    def get(self, request):
        args = {}
        args['mans'] = People.objects.all()
        args['username'] = auth.get_user(request).username
        return render(request, 'people/people_list.html', args)


class PeopleLink(View):
    def get(self, request, id):
        args = {}
        args['man'] = People.objects.get(id=id)
        args['username'] = auth.get_user(request).username
        return render(request, "people/people_link.html", args)


class PeopleDelete(View):
    def get(self, request, id):
        People.objects.filter(id=id).delete()
        return redirect("/company/")


class PeopleAdd(View):
    pass


class PeopleEdit(View):
    pass
