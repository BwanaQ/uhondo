from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__, instance_relative_config=True)

# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# initialize Flask Extension
bootstrap = Bootstrap(app)

@app.template_filter()
def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel.dates.format_datetime(value, format)
    
from app import views
