from flask import Flask, render_template
import os
import adal

app = Flask(__name__)

tenant = os.environ['AZURE_TENANT']
app_id = os.environ['AZURE_APP_ID']
app_password = os.environ['AZURE_APP_PASSWORD']

resource_URL ='https://graph.microsoft.com'
authority_url = 'https://login.microsoftonline.com/%s'%(tenant)

context = adal.AuthenticationContext(authority_url)

@app.route("/")
def index():    
    token = context.acquire_token_with_client_credentials(
        resource_URL,
        app_id,
        app_password)
    
    return render_template('login.html', access_token=token['accessToken'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)