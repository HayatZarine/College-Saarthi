class Config:
    SECRET_KEY = 'your_secret_key'  # Change this to a secure key
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/book_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
