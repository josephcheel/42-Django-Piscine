from django.shortcuts import render

# Create your views here.
def index(request):

	noir_shades = []	
	for i in range(0, 256, 5):
		noir_shades.append([i, i, i])
	
	rouge_shades = []
	for i in range(0, 256, 5):
		rouge_shades.append([i, 0, 0])
	
	bleu_shades = []
	for i in range(0, 256, 5):
		bleu_shades.append([0, 0, i])

	vert_shades = []
	for i in range(0, 256, 5):
		vert_shades.append([0, i, 0])

	noir_shades.reverse()
	rouge_shades.reverse()
	bleu_shades.reverse()
	vert_shades.reverse()

	noir_shades = noir_shades[:50]
	rouge_shades = rouge_shades[:50]
	bleu_shades = bleu_shades[:50]
	vert_shades = vert_shades[:50]

	nbr_list = []
	for i in range(1, 51):
		nbr_list.append(i)
	all_shades = zip(nbr_list, noir_shades, rouge_shades, bleu_shades, vert_shades)

	return render(request, 'ex03/index.html', {
		'all_shades': all_shades,
	})