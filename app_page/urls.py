from django.urls import path
from .views import ListCarsView, AddCarsView, UpdateCarsView, DetailCarsView, DeleteCarsView
# from .views import home_page, add_car


urlpatterns = [
    # path("asdf/", home_page, name="home_page"),
    # path("add/car/", add_car, name='add_car'),
    path("", ListCarsView.as_view(), name='home'),
    path("add/", AddCarsView.as_view(), name='add'),
    path('detail/<int:pk>', DetailCarsView.as_view(), name='detail'),
    path("update/<int:pk>", UpdateCarsView.as_view(), name='update'),
    path("delete/<int:pk>", DeleteCarsView.as_view(), name='delete')
]
