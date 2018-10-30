import json
from channels.generic.websocket import WebsocketConsumer

from .models import LogsDB


class MabLogConsumer(WebsocketConsumer):
    org_string = ""

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None):
        cur_string = ""
        log_set = None
        text_data_json = json.loads(text_data)
        app_name = text_data_json["app_name"]
        operation_no = text_data_json["operation_no"]
        # 用于从日志数据库里找到发布单的发布日志
        if text_data_json["env_name"] == "Demo":
            deploy_version = text_data_json["deploy_version"]
            log_set = LogsDB.objects.filter(app_name=app_name,
                                            deploy_version=deploy_version,
                                            operation_no=operation_no,
                                            operation_type="deploy")\
                .order_by('id')
        # 用于从日志数据库里找到服务器启停的发布日志
        if text_data_json["deploy_version"] == "Demo":
            deploy_version = "Demo",
            env_name = text_data_json["env_name"]
            log_set = LogsDB.objects.filter(app_name,
                                            deploy_version=deploy_version,
                                            env_name=env_name,
                                            operation_no=operation_no,
                                            operation_type="operation")\
                .order_by('id')
        if log_set is not None:
            for log_item in log_set:
                cur_string += log_item.log_content + "\n"
        if cur_string == self.org_string:
            pass
        else:
            if len(cur_string) > len(self.org_string):
                send_string = cur_string.replace(self.org_string, "")
                self.org_string = cur_string
                '''
                self.send(text_data=json.dumps({
                    "message": log_set[0].log_content
                }))
                '''
                self.send(text_data=send_string)
            else:
                pass


