from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

app = Flask(__name__)

with open('almacen.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)

SWAGGER_URL = '/api/docs' 
API_URL = 'localhost:5000' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,
    config={  
        'app_name': "Swagger API Python",
        'body': yaml.dump_all(prime_service['basedatos'], explicit_start=True)
    },
     oauth_config={

     }
)

app.register_blueprint(swaggerui_blueprint)

app.run()

