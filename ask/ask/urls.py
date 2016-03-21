from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from qa.views import main_list, test, question_details, popular_list, \
ask_form, post_answer, signup_form, login_form

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),i
    url(r'^$', main_list, name='home'),
    url(r'^login/', login_form),
    url(r'^signup/', signup_form),
    url(r'^question/(\d+)/', question_details, name='question-details'),
    url(r'^ask/', ask_form),
    url(r'^popular/', popular_list),
    url(r'^new/', test),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^answer/', post_answer),
)
