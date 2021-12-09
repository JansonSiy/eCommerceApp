"""projectFolder_eCommerceApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# STEP 5 - REFERENCE URL
# The next step is to point the root URLconf at the store.urls module.
# In projectFolder_eCommerceApp/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list.
# The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
# The idea behi nd include() is to make it easy to plug-and-play URLs. Since store are in their own URLconf (store/urls.py), they can be placed under “/store/”, or under “/fun_store/”, or under “/content/store/”, or any other path root, and the app will still work.

# removed, I don't know what this is for, but it's causing an error
# from _typeshed import SupportsLessThan
from django.contrib import admin
from django.urls import include, path
from store import url as store_url
# from store app, import url.py then rename to store_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(store_url))
]