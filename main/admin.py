from django.contrib import admin
from .models import*
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
 
class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','category','brand','status','is_featured')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable=('status','is_featured')

# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','product','price','color','size')
    
# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')    

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','total')


class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
 
class UserAddressBookAdmin(admin.ModelAdmin):
	list_display=('user','address','status')
 
  

admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(UserAddressBook,UserAddressBookAdmin)
admin.site.register(Wishlist)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(ProductAttribute,ProductAttributeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Banner,BannerAdmin)