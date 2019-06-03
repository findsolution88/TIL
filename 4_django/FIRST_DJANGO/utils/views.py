from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'utils/index.html')

def art_text(request, keyword):
    import art
    result = art.text2art(keyword, 'alpha')
    context = {
        'result': result,
        'keyword': keyword,
    }
    return render(request, 'utils/art_text.html', context)

def stock(request):
    pass # todo: 완성하기