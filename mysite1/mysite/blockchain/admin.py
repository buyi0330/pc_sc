from django.contrib import admin

# Register your models here.
from .models import PublicChainBlock,SideChainBlock,SideChain

admin.site.register(PublicChainBlock)
admin.site.register(SideChainBlock)
admin.site.register(SideChain)