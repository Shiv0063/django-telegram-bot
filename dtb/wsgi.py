import os

from django.core.wsgi import get_wsgi_application

from run_polling import run_polling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtb.settings')

application = get_wsgi_application()


if __name__ == "__main__":
    run_polling()
