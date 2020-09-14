class News :
    '''
    news class to define news objects
    '''

    def __init__(self,id,name,author,title,description,poster,content):
        self.id = id
        self.name = name
        self.author= author
        self.title= title
        self.description= description
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.content =  content