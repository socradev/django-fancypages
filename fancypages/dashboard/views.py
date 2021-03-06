from django.views import generic
from django.db.models import get_model
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from . import forms
from ..utils import get_page_model, get_node_model


# PageNode = get_node_model()
# FancyPage = get_page_model()

# ContentBlock = get_model('fancypages', 'ContentBlock')
# Category = get_model('catalogue', 'Category')
# Container = get_model('fancypages', 'Container')
# TabBlock = get_model('fancypages', 'TabBlock')
# OrderedContainer = get_model('fancypages', 'OrderedContainer')


class PageListView(generic.ListView):
    # model = FancyPage
    context_object_name = 'fancypage_list'
    template_name = "fancypages/dashboard/page_list.html"

    def __new__(cls, *args, **kwargs):
        cls.model = get_page_model()

    def get_queryset(self, queryset=None):
        return self.model.objects.top_level()


class PageCreateView(generic.CreateView):
    # model = FancyPage
    form_class = forms.PageNodeForm
    template_name = "fancypages/dashboard/page_update.html"

    def __new__(cls, *args, **kwargs):
        cls.model = get_page_model()

    def get_form_kwargs(self):
        kwargs = super(PageCreateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(PageCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Create new page")
        return ctx

    def get_success_url(self):
        return reverse('fp-dashboard:page-list')


class PageUpdateView(generic.UpdateView):
    # model = FancyPage
    form_class = forms.PageNodeForm
    context_object_name = 'fancypage'
    template_name = "fancypages/dashboard/page_update.html"

    def __new__(cls, *args, **kwargs):
        cls.model = get_page_model()

    def get_context_data(self, **kwargs):
        ctx = super(PageUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Update page")
        return ctx

    def get_success_url(self):
        return reverse('fp-dashboard:page-list')


class PageDeleteView(generic.DeleteView):
    # model = FancyPage
    context_object_name = 'fancypage'
    template_name = "fancypages/dashboard/page_delete.html"

    def get_success_url(self):
        return reverse('fp-dashboard:page-list')

    def __new__(cls, *args, **kwargs):
        cls.model = get_page_model()
