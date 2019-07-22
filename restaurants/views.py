from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        'my_list':[
            {"restaurant_name":"CHLOE HAY","food_type" :"Asian" },
            {"restaurant_name":"Al Khayam","food_type" :"Middle Eastern" },     
             {"restaurant_name":"Piatto","food_type" :"Italian" },   
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object': {"restaurant_name":"Piatto","food_type" :"Italian" },   
    }
    return render(request, 'detail.html', context)
