from django import forms
from .models import Discipline, Summary
from accounts.models import Trainee, Statistics
from houses.models import House
from books.models import Book



class NewDisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        fields = '__all__'

    def save(self, commit=True):
        discipline = super(NewDisciplineForm, self).save(commit=False)
        if commit:
            discipline.save()
        return discipline


class NewSummaryForm(forms.ModelForm):

    class Meta:
        model = Summary
        exclude = ('approved', 'discipline',)

    def __init__(self, *args, **kwargs):
        t = kwargs.pop('trainee', None)
        # self.request = kwargs.pop('request', None)
        super(NewSummaryForm, self).__init__(*args, **kwargs)

        # Auto-populate from last lifestudy book + chapter
        print 'user', t
        # t = self.user.trainee
        if t and t.statistics:
            (book_id, chpt) = t.statistics.latest_ls_chpt.split(':')
            self.initial['book'] = Book.objects.get(id=book_id)
            self.initial['chapter'] = int(chpt) + 1
            # self.fields['book'] = Book.objects.get(id=book_id)
            # self.fields['chapter'] = int(chpt) + 1

    def save(self, commit=True):
        summary = super(NewSummaryForm, self).save(commit=False)
        if commit:
            #update the last book for discipline for trainee
            t = summary.discipline.trainee
            print 'trainee', t, t.statistics
            stat_str = str(summary.book.id) + ':' + str(summary.chapter)

            Statistics.objects.update_or_create(trainee=t, latest_ls_chpt=stat_str)
            # if t.statistics:
            #     print 'update stats'
            #     # update
            #     t.statistics.update(latest_ls_chpt=stat_str)
            # else:
            #     print 'create'
            #     # create
            #     s = Statistics(latest_ls_chpt=stat_str)
            #     s.save()
            #     t.statistics = s
            #     t.save()
            print summary.book, summary.chapter, t.statistics
            summary.save()
        return summary


class EditSummaryForm(forms.ModelForm):

    class Meta:
        model = Summary
        exclude = ('book', 'chapter', 'discipline', 'approved', )

    def save(self, commit=True):
        summary = super(EditSummaryForm, self).save(commit=False)
        if commit:
            summary.save()
        return summary


class HouseDisciplineForm(forms.ModelForm):

    class Meta:
        model = Discipline
        exclude = ('trainee',)
        
    House = forms.ModelChoiceField(House.objects)
