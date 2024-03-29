from django.urls import path
from .views import home_page, shop_page, shop_detail_page, cart_page, chackout_page, testimonial_page, not_found_page, contact_page


urlpatterns = [
    path("", home_page, name='home'),
    path("shop/", shop_page, name="shop"),
    path("shop_detail/", shop_detail_page, name="shop_detail"),
    path("cart_page/", cart_page, name="cart"),
    path("chackout_page/", chackout_page, name="chackout"),
    path("testimonial_page/", testimonial_page, name="testimonial"),
    path("not_found_page/", not_found_page, name="not_found"),
    path("contact_page/", contact_page, name="contact"),
]