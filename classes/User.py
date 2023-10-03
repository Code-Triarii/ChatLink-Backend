class User:
    '''User class for user object handling.
    
    Constructor
    ----------
    - username (str): username given by the user. By default, anon.

    Attributes
    ----------
    - username (str): username given by the user. By default, anon.
    - pwd (str): password to authenticate the user.
    - room (str): room identifier to set the user's context.

    Methods
    ----------
    - N/A
    '''
    def __init__(self, username: str = 'anon'):
        self.username = str(username)
        self.room = ''
        self.pwd = ''