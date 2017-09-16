from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.BadgeListView.as_view(), name='badges_list'),
  url(r'^print/$', views.badgeprintout, name='badges_print'),
  url(r'^print/term/front/$', views.BadgePrintFrontView.as_view(), name='badges_print_term_front'),
  url(r'^print/term/massfront/$', views.BadgePrintMassFrontView.as_view(), name='badges_print_term_massfront'),
  url(r'^print/term/bostonfront/$', views.BadgePrintBostonFrontView.as_view(), name='badges_print_term_bostonfront'),
  url(r'^print/term/massbostonfront/$', views.BadgePrintMassBostonFrontView.as_view(), name='badges_print_term_massbostonfront'),
  url(r'^print/term/allinclusivefront/$', views.BadgePrintAllInclusiveFrontView.as_view(), name='badges_print_all_inclusive_front'),
  url(r'^print/back/$', views.BadgePrintGeneralBackView.as_view(), name='badges_print_general_back'),
  url(r'^print/term/bostonback/$', views.BadgePrintBostonBackView.as_view(), name='badges_print_boston_back'),
  url(r'^print/term/facebook/$', views.BadgePrintFacebookView.as_view(), name='badges_print_term_facebook'),
  url(r'^print/staff/$', views.BadgePrintStaffView.as_view(), name='badges_print_staff'),
  url(r'^print/shortterm/$', views.BadgePrintShorttermView.as_view(), name='badges_print_shortterm'),
  url(r'^print/usher/$', views.BadgePrintUsherView.as_view(), name='badges_print_usher'),
  url(r'^print/temp/$', views.BadgePrintTempView.as_view(), name='badges_print_temp'),
  url(r'^print/visitor/$', views.BadgePrintVisitorView.as_view(), name='badges_print_visitor'),
  url(r'^print/visitorxb/$', views.BadgePrintVisitorXBView.as_view(), name='badges_print_visitor_xb'),
  url(r'^print/office/$', views.BadgePrintOfficeView.as_view(), name='badges_print_office'),
  url(r'^create/$', views.BadgeCreateView.as_view(), name='badge_create'),
  url(r'^edit/(?P<pk>\d+)/$', views.BadgeUpdateView.as_view(), name='badge_detail'),
  url(r'^delete/(?P<pk>\d+)/$', views.BadgeDeleteView.as_view(), name='badge_delete'),
  url(r'^create/batch/$', views.batch, name='badges_batch'),
  url(r'^remake/avatar/$', views.remakeMassAvatar, name='badges_remake_avatar'),
  url(r'^view/$', views.BadgeTermView.as_view(), name='badges_term'),
  url(r'^view/current$', views.BadgeTermView.as_view(), name='current_badges_term'),
  url(r'^view/xb/$', views.BadgeXBTermView.as_view(), name='badges_term_xb'),
  url(r'^view/staff/$', views.BadgeStaffView.as_view(), name='badges_staff'),
  url(r'^print/term/facebook/generate/$', views.BadgePrintFrontView.as_view(), name='badges_print_term_genpdf'),
  # Dynamic CSS
  url(r'^print/badgeSettings.css$', views.badgeSettingsCSS, name='badge_settings_CSS'),
  url(r'^print/settings/$', views.BadgePrintSettingsUpdateView.as_view(), name='badge_print_settings_update'),
]
