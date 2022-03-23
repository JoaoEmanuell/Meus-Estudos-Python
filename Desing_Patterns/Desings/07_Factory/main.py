from source import MysqlFactory

usecase = MysqlFactory.create()
response = usecase.do_something()
print(response)