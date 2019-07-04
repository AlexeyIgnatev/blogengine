from django.db.models import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect, reverse


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        creator = False
        try:
            if obj.creator.all().get(user=request.user):
                creator = True
        except ObjectDoesNotExist:
            pass

        return render(request, self.template,
                      context={self.model.__name__.lower(): obj, 'admin_object': obj, 'detail': True,
                               'creator': creator})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        form = self.form_model(request.POST)
        if form.is_valid():
            new_obj = form.save()
            new_obj.creator.set([request.user.profile])
            new_obj.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': form})


class ObjectUpdateMixin:
    form_model = None
    template = None
    model = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(instance=obj)
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(request.POST, instance=obj)
        if form.is_valid():
            new_obj = form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
