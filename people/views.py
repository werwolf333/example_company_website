from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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



@method_decorator(csrf_exempt, name='dispatch')
class PeopleAdd(View):
    def get(self, request):
        args = {}
        args['mans'] = People.objects.all()
        args['username'] = auth.get_user(request).username
        return render(request, "people/people_add.html", args)

    def post(self, request):
        args = {}
        man = People(
            name=request.POST['name'],
            surname=request.POST['surname'],
            patronymic=request.POST['patronymic'],
            position=request.POST['position'],
            boss_id=request.POST['boss'],
            image=request.FILES.get('image', None)
        )

        man.save()
        args['man'] = man
        return redirect("/company/")


class PeopleEdit(View):
    pass
