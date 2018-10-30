import requests
import json

headers = {'Content-Type': 'application/json;charset=utf-8'}
payload = {'deploy_version': "2018-06-21-12DB",
           'app_name': "ZIP-BACKEND-JAVA",
           'ip_address': "1.1.1.1",
           'env_name': "UAT",
           'user_name': "chengang",
           'operation_type': "deploy",
           'operation_no': 8,
           'log_content': "...2018-07-23 08:43:38deploypkg \
           cnsz141851-10.25.164.109, deploy progress 60%"}

requests.post("http://localhost:8888/wslog/log_add/", headers=headers, data=json.dumps(payload))
print('ok')
