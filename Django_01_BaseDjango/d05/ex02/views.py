import logging

from django.shortcuts import render
from django.conf import settings
from .forms import InputHistoryForm

# Create your views here.
def index(request):
	logger = logging.getLogger('historyLogger')
	if request.method == 'POST':
		form = InputHistoryForm(request.POST)
		if form.is_valid():
			new_line = form.cleaned_data['line']
			logger.info(new_line)
			with open(settings.EX02_LOG_FILE, 'r') as f:
				history = f.readlines()
			return render(request, 'ex02/index.html', {
				'form': InputHistoryForm(),
				'history': history
			})
		else:
			return render(request, 'ex02/index.html', {
				'form': form
			})
		# 	with open('history.txt', 'a') as f:
		# 		f.write(form.cleaned_data['content'] + '\
	with open(settings.EX02_LOG_FILE, 'r') as f:
		history = f.readlines()
	return render(request, 'ex02/index.html', {
		'form': InputHistoryForm(),
		'history': history
	})