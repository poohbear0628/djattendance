from django.forms import Form, FileField

class CsvFileForm(Form):
    csvFile = FileField(label='Select a file')
