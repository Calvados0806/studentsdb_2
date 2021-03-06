# -*- coding: utf-8 -*-

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studentsdb.settings import ADMIN_EMAIL

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input( Submit('send_button', u'Надіслати') )

    from_email = forms.EmailField(
        label=u"Ваша Емейл Адреса"
    )
    subject = forms.CharField(
        label=u"Заголовок Листа",
        max_length=128
    )
    message = forms.CharField(
        label=u"Текст повідомлення",
        max_length=2048,
        widget=forms.Textarea
    )

def contact_admin(request):
    # check if forn was posted
    if request.method == 'POST':
        # create form instance
        form = ContactForm(request.POST)
        #check whether user data is valid
        if form.is_valid():
            # send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = u"Під час відправки форми виникла непередбачувана помилка.\
                Спробуйте скористатися даною формою пізніше"
            else:
                message = u"Повідомлення відправлено успішно"

            # redirect to the same page with status message
            return HttpResponseRedirect(u"%s?status_message=%s" %(reverse('contact_admin'), message))
    # if there was not POST render blank form
    else:
        form = ContactForm()
    return render(request, 'contact_admin/contact_admin.html', {'form': form})
