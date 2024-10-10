from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('categories',views.categories),
    path('products',views.products, name='products'),
    path('product<int:id>',views.prods,name="prod_cat"),
    path('productdetails<int:id>',views.productdetails,name="product_details"),
    path('addcart<int:id>',views.addtocart,name='addcarts'),
    path('signup',views.signup),
    path('login',views.loginpage,name='login'),
    path('carts',views.cartpage, name='carts'),
    path('remove<int:id>',views.remove,name='remove'),
    path('placeorder',views.placeorder, name='placeorder'),
    path('orderconfirmation',views.orderconfirmation, name='orderconfirm'),
    path('createproduct',views.create_product, name= 'createproduct'),
    path('createcategory',views.create_category, name= 'createcategory'),
    path('adminview',views.adminview, name='adminview'),
    path('edit<int:getid>',views.editbyuser, name='edit'),
    path('delete<int:getid>', views.deletebyuser, name='delete'),
          
]