from django.shortcuts import render
from django.http import HttpResponse

projectsList =  [
    {"id": '1', "title": "The Shawshank Redemption", "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
    {"id": '2', "title": "The Godfather", "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."},
    {"id": '3', "title": "The Dark Knight", "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."},
    {"id": '4', "title": "Pulp Fiction", "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."},
    {"id": '5', "title": "Schindler's List", "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis."},
    {"id": '6', "title": "The Lord of the Rings: The Return of the King", "description": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring."},
    {"id": '7', "title": "Fight Club", "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more."},
    {"id": '8', "title": "Forrest Gump", "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart."},
    {"id": '9', "title": "Inception", "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."},
    {"id": '10', "title": "The Matrix", "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."}
]


# Create your views here.
def projects(request):
    # page = 'projects'
    number = 9
    context =  {'projects':projectsList}
    return render(request,'projects/projects.html',context)
def project(request,pk):
    projectObj = None
    for i in projectsList:
        print(i['id'],  pk)
        if i['id']==pk:
            projectObj = i
            print(i)
        else:
            print('Zero')
    return render(request,'projects/single-projects.html',{'project':projectObj})

