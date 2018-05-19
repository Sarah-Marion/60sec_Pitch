import json, urllib.request
from flask import url_for, redirect, request, current_app as app
from rauth import OAuth2service

class GoogleSignIn(OAuthSignIn):
    def __init__(self):

        super(GoogleSignIn, self).__init__('google')
        googleinfo = urllib.request.urlopen('https://accounts.google.com/.well-known/openid-configuration')
        google_params = json.load(googleinfo)

        self.service = OAuth2Service(
                name='google',
                client_id=self.consumer_id,
                client_secret=self.consumer_secret,
                authorize_url=google_params.get('authorization_endpoint'),
                base_url=google_params.get('userinfo_endpoint'),
                access_token_url=google_params.get('token_endpoint')
        )


    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email',
            response_type='code',
            redirect_uri=self.get_callback_url())
            )


    def callback(self):
        try:
            if 'code' not in request.args:
                return None, None, None
            oauth_session = self.service.get_auth_session(
                    data={'code': request.args['code'],
                          'grant_type': 'authorization_code',
                          'redirect_uri': self.get_callback_url()
                         },
                    decoder = json.loads
            )
            user = oauth_session.get('').json()
        except:
            flash("An error occurred,please try again")
            redirect(url_for('main.login'))
        else:
            return (user['name'],
                    user['email'])