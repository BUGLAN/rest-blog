from blog import create_app
from config import BaseConfig

if __name__ == '__main__':
    app = create_app(BaseConfig)
    app.run(debug=True)
