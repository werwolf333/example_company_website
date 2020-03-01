from django.contrib import auth
from django.shortcuts import render
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
    pass


class PeopleDelete(View):
    pass


class PeopleAdd(View):
    pass


class PeopleEdit(View):
    pass
