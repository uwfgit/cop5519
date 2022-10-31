import json


class MysqlDatabase:
    def __init__(self):
        self.users = json.loads(open('./assets/users.json', mode='r', encoding='utf-8').read())
        self.consumers = json.loads(open('./assets/consumers.json', mode='r', encoding='utf-8').read())
        self.new_users = []

    def check_login(self, username, password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, 'Login Successfully '
                else:
                    return False, 'Login Failed, incorrect passwords'
        return False, 'Login Failed, incorrect username'

    def insert_records(self, consumer):
        self.new_users.append(consumer)

    def all_records(self):
        return self.consumers

    def write_into(self):
        temp = self.all_records()
        temp = ','.join(str(i) for i in self.new_users)
        json_str = json.dumps(self.new_users, indent=4)
        with open('./assets/consumers.json', 'w') as json_file:
            json_file.write(json_str)


# TODO: 装饰器
def check_login_to(func):
    def wrapper():
        pass

    return wrapper


db = MysqlDatabase()
