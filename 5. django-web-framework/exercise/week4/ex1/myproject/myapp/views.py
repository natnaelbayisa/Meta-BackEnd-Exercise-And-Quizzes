from django.shortcuts import render

# Create your views here.

def about(request): 
    about_content = {'about': "History of Lorem Ipsum originates with Cicero in the 1st Century BC and his text De Finibus bonorum et malorum. This philosophical work, also known as On the Ends of Good and Evil, was split into five books."}
    return render(request, "about.html", about_content) 

def about_us(request):
    about_content = {'about_us': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about_us.html", {'content': about_content})

def menu(request):
    new_menu = {'mains': [
        {
            'name': 'pizza', 'price': '100'
        },
        {
            'name': 'shiro', 'price': '200'
        },
        {
            'name': 'burger', 'price': '300'
        },
    ]}
    about_content = {'about_menu': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    # return render(request, "menu.html", {'content': about_content})
    return render(request, "menu.html", new_menu)

# pl refers to programming language
def pl(request): 
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust'] 
    return render(request, 'pl.html', {'langs':langs}) 


def user_status(request): 
    context={'user':'admin'} 
    return render(request, 'user_status.html', context)

# dct refers to dictionary context
def dictionary(request):
    dct = {'digits': ['One', 'Two', 'Three'],'tens': ['Ten', 'Twenty', 'Thirty']}  
    return render(request, "dct.html", dct)