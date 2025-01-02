import requests
from requests.auth import HTTPBasicAuth
import env


def public_authenticate() -> str:
    auth_url = 'https://api.trackmania.com/api/access_token'
    body = f"grant_type=client_credentials&client_id={env.TRACKMANIA_CLIENT_ID}&client_secret={env.TRACKMANIA_CLIENT_SECRET}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp = requests.post(auth_url, data=body, headers=headers)
    resp.raise_for_status()
    j = resp.json()
    TOKEN = j['access_token']
    TOKEN_TYPE = j['token_type']
    return f"{TOKEN_TYPE} {TOKEN}"


def live_authenticate() -> None:
    auth_url = 'https://prod.trackmania.core.nadeo.online/v2/authentication/token/basic'
    headers = {}
    data = {'audience': 'NadeoLiveServices'}
    auth = HTTPBasicAuth(env.TRACKMANIA_LOGIN, env.TRACKMANIA_PASSWORD)
    resp = requests.post(url=auth_url, data=data, headers=headers, auth=auth)
    resp.raise_for_status()
    j = resp.json()
    return f"nadeo_v1 t={j['accessToken']}"
