import requests
import json

headers = {'Content-Type': 'application/json;charset=utf-8'}
payload = {'deploy_version': "2018-06-21-12DB",
           'app_name': "ZIP-BACKEND-JAVA",
           'ip_address': "1.1.1.1",
           'env_name': "UAT",
           'user_name': "sky",
           'operation_type': "deploy",
           'operation_no': 8,
           'log_content': "...2018-07-23 08:43:38 deploypkg \
           cnsz141851-10.25.164.110, deploy progress 80%"}
try:
    result = requests.post("http://127.0.0.1:8888/wslog/log_add/", headers=headers, data=json.dumps(payload))
    print(result.status_code)
except Exception as e:
    print(e)
print('ok')
