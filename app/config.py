class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-11&sortBy=publishedAt&apiKey=f686a2bec46142f588d667a0c2cd0f19'
    pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
