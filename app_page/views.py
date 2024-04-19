from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Cars
from .forms import CarsModel
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView
                                  )

# def home_page(request):
#     cars = Cars.objects.all()
#     context = {
#         "cars": cars
#     }
#     return render(request, 'home_page.html', context)


# def add_car(request):
#     if request.method == "POST":
#         form = CarsModel(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#         else:
#             return render(request, 'CRUD/add_car.html', {"form":form})
#     else:
#         form = CarsModel()
#         context = {
#             "form": form
#         }
#         return render(request, 'CRUD/add_car.html', context)


class AddCarsView(LoginRequiredMixin, CreateView):
    template_name = 'cars/add_car.html'
    model = Cars
    fields = ["car_name", 'car_make', 'car_image', 'car_price', "car_year", 'car_category']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.car_added_by = self.request.user
        return super().form_valid(form)


class ListCarsView(ListView):
    template_name = 'home_page.html'
    model = Cars
    paginate_by = 3


class DetailCarsView(DetailView):
    model = Cars
    template_name = 'cars/detail.html'


class UpdateCarsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'cars/update.html'
    model = Cars
    fields = ['car_name', 'car_make', 'car_image', 'car_price', 'car_year', 'car_added_by', 'car_category']
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user == self.get_object().car_added_by


class DeleteCarsView(LoginRequiredMixin, DeleteView):
    model = Cars
    template_name = 'cars/delete.html'
    success_url = reverse_lazy('home')
