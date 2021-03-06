
from django.conf.urls import include, url
from gglobal.crm import views

urlpatterns = [
    url(
        regex=r'^~createclient/$',
        view=views.CreateCRMApeal,
        name='createclient'
        ),
    url(
    	regex=r'^proceed_appeal/(?P<appeal_id>\d+)/(?P<next_state_id>\d+)/$',
    	view=views.proceed_appeal,
    	name='proceed_appeal' ),
    url(
    	regex=r'^proceed_appeal_single/(?P<appeal_id>\d+)/(?P<next_state_id>\d+)/$',
    	view=views.proceed_appeal_single,
    	name='proceed_appeal_single' ),
    url(
    	regex=r'^proceed_assignment/(?P<assignment_id>\d+)/(?P<next_state_id>\d+)/$',
    	view=views.proceed_assignment,
    	name='proceed_assignment' ),
    url(
    	regex=r'^proceed_assignment_single/(?P<assignment_id>\d+)/(?P<next_state_id>\d+)/$',
    	view=views.proceed_assignment_single,
    	name='proceed_assignment_single' ),
    url(
        regex=r'^passing_assign/(?P<assignment_id>\d+)/(?P<user_id>\d+)/$',
        view=views.passing_assign,
        name='passing_assign' ),
    url(
        regex=r'^telegram_auth/(?P<user_id>\d+)/$',
        view=views.telegram_auth,
        name='telegram_auth' ),
    url(
        regex=r'^payment-method-autocomplete/$',
        view=views.PaymentAutocomplete.as_view(),
        name='payment-method-autocomplete',
    ),
]


