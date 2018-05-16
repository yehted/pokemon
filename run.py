import logging
from pokemon import create_app

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s- %(levelname)s: %(message)s')
app = create_app()

if __name__ == '__main__':
    app.run()
