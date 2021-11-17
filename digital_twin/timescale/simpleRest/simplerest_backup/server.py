from flask import render_template
import connexion
import  config
# Create the application instance
app = config.connex_app

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yaml')

# Create a URL route in our application for "/"


oidc = config.oidc


@app.route('/')
@oidc.require_login
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
