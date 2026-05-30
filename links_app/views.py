from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LinksForm
from .models import Links , Category

@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinksForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user # підставив user
            link.save()
            return redirect('my_links')
    else:
        form = LinksForm()
    return render(request, 'links/create_link.html', {'form': form})

@login_required
def my_links(request):
    links = Links.objects.filter(user=request.user).select_related('category', 'user')
    return render(request, 'links/my_links.html', {'links': links})


class LinksListView(ListView):
    model = Links
    template_name = 'links/links_view.html'
    context_object_name = 'links'
    paginate_by = 5

    def get_queryset(self):
        queryset = Links.objects.filter(privacy = False).select_related('category', 'user').order_by('-created_at')

        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id = category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')

        return context

class LinkDetailView(LoginRequiredMixin,DetailView):
    model = Links
    template_name = 'links/link_detail.html'
    context_object_name = 'link'

    def get_queryset(self):
        return Links.objects.filter(user=self.request.user)


class LinkUpdateView(LoginRequiredMixin,UpdateView):
    model = Links
    template_name = 'links/link_update.html'

    form_class= LinksForm

    success_url = '/links/my_links/'

    def get_queryset(self):
        return Links.objects.filter(user=self.request.user)

class LinkDeleteView(LoginRequiredMixin,DeleteView):
    model = Links
    template_name = 'links/link_delete.html'
    success_url = '/links/my_links/'