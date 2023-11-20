import os
import requests

def webhook(request):
    payload = request.get_json()
    if payload["zen"]["type"] == "push":
        repo_url = payload["repository"]["url"]
        os.system("git pull {}".format(repo_url))

        # Reload web app
        web_app_name = "siddmi07.pythonanywhere.com"
        requests.post("https://api.pythonanywhere.com/v2/webapps/{}/reload/".format(web_app_name))

    return "OK"