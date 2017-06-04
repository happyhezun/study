flask 实现Restful api

获取所有的tasks
curl -i http://localhost:5000/todo/api/v1.0/tasks

获取某个task：
curl -i http://localhost:5000/todo/api/v1.0/tasks/2

新增一个task:
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks

修改某个task:
curl -i -H "Content-Type: application/json"  -d '{"description":"Buy a Car"}' http://localhost:5000/todo/api/v1.0/tasks/2

删除某个task:
curl -i -X DELETE  http://localhost:5000/todo/api/v1.0/tasks/2