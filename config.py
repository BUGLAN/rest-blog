class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/restblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_ITEMS = 10
