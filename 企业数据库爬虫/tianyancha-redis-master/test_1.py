from RedisQueue import RedisQueue
q=RedisQueue('test')
q.put("你好")
print(q.get().decode('utf-8'))


