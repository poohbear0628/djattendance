from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import Group, User
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django_select2.forms import ModelSelect2MultipleWidget
from django.shortcuts import get_object_or_404

from .models import UserMeta, User, Trainee, TrainingAssistant, Locality
from .forms import APUserCreationForm, APUserChangeForm
from aputils.admin import VehicleInline, EmergencyInfoInline
from aputils.widgets import PlusSelect2MultipleWidget
from django_extensions.admin import ForeignKeyAutocompleteAdmin

from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

from aputils.admin_utils import FilteredSelectMixin, DeleteNotAllowedModelAdmin, AddNotAllowedModelAdmin
from aputils.utils import sorted_user_list_str


"""" ACCOUNTS admin.py """


class APUserAdmin(UserAdmin):
  # Set the add/modify forms
  add_form = APUserCreationForm
  form = APUserChangeForm

  def type(obj):
    return obj.get_type_display()

  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserAdmin that reference
  # specific fields on auth.User
  list_display = ("firstname", "lastname", "gender", "email", "is_active", type,)
  list_filter = ("is_staff", "type", "is_active", "groups")
  search_fields = ("email", "firstname", "lastname")
  ordering = ("firstname", "lastname",)
  filter_horizontal = ("groups", "user_permissions")
  fieldsets = (
    ("Personal info", {"fields":
     ("email", "firstname", "lastname", "gender", "rfid_tag",)}),
    ("Permissions", {"fields":
     ("is_active",
       "is_staff",
       "is_superuser",
       "groups",)}),
    ("Important dates", {"fields": ("last_login",)}),
    )

  add_fieldsets = (
    (None, {
      "classes": ("wide",),
      "fields": ("email", "firstname", "lastname", "gender", "type", "password",
       "password_repeat")}
      ),
    )


class CurrentTermListFilter(SimpleListFilter):
  # Lists the trainees by term
  title = _('current term')

  parameter_name = 'current term'

  def lookups(self, request, model_admin):
    """
    Returns a list of tuples. The first element in each tuple is the coded value
    for the option that will appear in the URL query. The second element is the human-
    readable name for the option that will appear in the right sidebar.
    """
    return (
      ('1term', _('1st term')),
      ('2term', _('2nd term')),
      ('3term', _('3rd term')),
      ('4term', _('4th term')),
    )

  def queryset(self, request, queryset):
    """
    """
    q_db = {
      '1term': 1,
      '2term': 2,
      '3term': 3,
      '4term': 4,
    }

    if self.value() in q_db:
      return queryset.filter(current_term=q_db[self.value()])


class FirstTermMentorListFilter(SimpleListFilter):
  # Make list of 1st term mentors for email notifications
  title = _('mentors')

  parameter_name = 'mentor'

  def lookups(self, request, model_admin):
    """
    Returns a list of tuples. The first element in each tuple is the coded value
    for the option that will appear in the URL query. The second element is the human-
    readable name for the option that will appear in the right sidebar.
    """
    return (
      ('1termmentor', _('1st term mentors')),
      ('2termmentor', _('2nd term mentors')),
      ('3termmentor', _('3rd term mentors')),
      ('4termmentor', _('4th term mentors')),
    )

  def queryset(self, request, queryset):
    """
    """
    if self.value() == '1termmentor':
      """queryset of 1st term mentors """
      q = queryset.filter(mentor__isnull=False)
      q_ids = [person.mentor.id for person in q if person.current_term == 1]
      q = q.filter(id__in=q_ids)
      return q

    if self.value() == '2termmentor':
      """queryset of 2nd term mentors """
      q = queryset.filter(mentor__isnull=False)
      q_ids = [person.mentor.id for person in q if person.current_term == 2]
      q = q.filter(id__in=q_ids)
      return q

    if self.value() == '3termmentor':
      """queryset of 3rd term mentors """
      q = queryset.filter(mentor__isnull=False)
      q_ids = [person.mentor.id for person in q if person.current_term == 3]
      q = q.filter(id__in=q_ids)
      return q

    if self.value() == '4termmentor':
      """queryset of 4th term mentors """
      q = queryset.filter(mentor__isnull=False)
      q_ids = [person.mentor.id for person in q if person.current_term == 4]
      q = q.filter(id__in=q_ids)
      return q


# Adding a custom TraineeAdminForm to use prefetch_related all the locality many-to-many relationship
# to pre-cache the relationships and squash all the n+1 sql calls.
class TraineeAdminForm(forms.ModelForm):
  TRAINEE_TYPES = (
      ('R', 'Regular (full-time)'),  # a regular full-time trainee
      ('S', 'Short-term (long-term)'),  # a 'short-term' long-term trainee
      ('C', 'Commuter')
  )

  type = forms.ChoiceField(choices=TRAINEE_TYPES)

  class Meta:
    model = Trainee
    exclude = ['password']
    widgets = {
      'locality': ModelSelect2MultipleWidget(
        queryset=Locality.objects.all(),
        required=False,
        search_fields=['city__icontains', 'state__icontains']
      ) # could add state and country
    }


class UserMetaInline(admin.StackedInline):
  model = UserMeta
  suit_classes = 'suit-tab suit-tab-meta'
  exclude = ('services', 'houses')


class TraineeAdmin(ForeignKeyAutocompleteAdmin, UserAdmin):
  add_form = APUserCreationForm
  form = TraineeAdminForm

  # Automatically type class event objects saved.
  def save_model(self, request, obj, form, change):
    print 'saving trainee', obj, obj.type
    if not obj.type or obj.type == '':
      obj.type = 'R'
    super(TraineeAdmin, self).save_model(request, obj, form, change)

  # User is your FK attribute in your model
  # first_name and email are attributes to search for in the FK model
  related_search_fields = {
    'TA': ('firstname', 'lastname', 'email'),
    'mentor': ('firstname', 'lastname', 'email'),
  }

  # TODO(useropt): removed spouse from search fields
  search_fields = ['email', 'firstname', 'lastname']

  # TODO(useropt): removed bunk, married, and spouse
  list_display = ('full_name', 'current_term', 'email', 'team', 'house',)
  list_filter = (CurrentTermListFilter, FirstTermMentorListFilter,)

  ordering = ('firstname', 'lastname',)
  filter_horizontal = ("groups", "user_permissions")

  def user_change_password(self, request, id, form_url=''):
    if not self.has_change_permission(request):
      raise PermissionDenied
    user = get_object_or_404(User, pk=id)
    new_password = user.date_of_birth.strftime("%m%d%y")
    user.set_password(new_password)
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  fieldsets = (
    (None, {
      'classes': ('suit-tab', 'suit-tab-personal',),
      'fields': ('email', 'firstname', 'middlename', 'lastname', 'gender',
                 'date_of_birth', 'type', 'locality', 'terms_attended', 'current_term',
                 ('date_begin', 'date_end',),
                 'TA', 'mentor', 'team', ('house',),
                 'self_attendance')
      }
    ),
    ('Permissions', {
      'classes': ('suit-tab', 'suit-tab-permissions',),
      'fields': ('is_active',
                 'is_staff',
                 'is_superuser',
                 'groups',)
      }
    ),
  )

  suit_form_tabs = (('personal', 'General'),
                    ('meta', 'Personal info'),
                    ('permissions', 'Permissions'),
                    ('vehicle', 'Vehicle'),
                    ('emergency', 'Emergency Info'))

  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'firstname', 'lastname', 'gender', 'password',
       'password_repeat')}
    ),
  )

  inlines = (UserMetaInline, VehicleInline, EmergencyInfoInline, )


# Adding a custom TrainingAssistantAdminForm to for change user form
class TrainingAssistantAdminForm(forms.ModelForm):
  class Meta:
    model = TrainingAssistant
    exclude = ['password', ]


class TrainingAssistantAdmin(UserAdmin):
  add_form = APUserCreationForm
  form = TrainingAssistantAdminForm

  # Automatically type class event objects saved.
  def save_model(self, request, obj, form, change):
    obj.type = 'T'
    print 'saving TA', obj, obj.type
    super(TrainingAssistantAdmin, self).save_model(request, obj, form, change)

  search_fields = ['email', 'firstname', 'lastname']
  list_display = ('firstname', 'lastname', 'email')
  list_filter = ('is_active',)
  ordering = ('firstname', 'lastname', 'email',)
  filter_horizontal = ('groups', 'user_permissions')

  fieldsets = (
      ('Personal info', {'fields':
       ('email',
        'firstname',
        'middlename',
        'lastname',
        'gender',
        'type',
        'TA')}),

      ('Permissions', {'fields':
       ('is_active',
        'is_staff',
        'is_superuser',
        )}),
  )

  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'firstname', 'lastname', 'gender', 'password',
       'password_repeat')}
      ),
    )

  inlines = (
    UserMetaInline,
  )


class GroupForm(forms.ModelForm):
  user_set = forms.ModelMultipleChoiceField(
    label='Trainees',
    queryset=User.objects.prefetch_related('groups'),
    required=False,
    widget=admin.widgets.FilteredSelectMultiple('user_set', is_stacked=False))

  class Meta:
    model = Group
    fields = ('name', )
    widgets = {
      'user_set': admin.widgets.FilteredSelectMultiple('user_set', is_stacked=False),
    }


class MyGroupAdmin(FilteredSelectMixin, GroupAdmin, DeleteNotAllowedModelAdmin, AddNotAllowedModelAdmin):
  form = GroupForm
  registered_filtered_select = [('user_set', User), ]
  list_display = ('name', 'members', )
  ordering = ('name', )

  def members(self, obj):
    return sorted_user_list_str(obj.user_set.all().only('firstname', 'lastname', 'email'))

  def member_count(self, obj):
    return obj.user_set.count()


# Register the new Admin
admin.site.register(User, APUserAdmin)
admin.site.register(Trainee, TraineeAdmin)
admin.site.register(TrainingAssistant, TrainingAssistantAdmin)

# unregister and register again
admin.site.unregister(Group)
admin.site.register(Group, MyGroupAdmin)
