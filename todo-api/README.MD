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

提交git遇到问题：
error: The requested URL returned error: 403 Forbidden while accessing

解决方法：
[remote "origin"]
    url = https://wangz@github.com/wangz/example.git

电影下载地址：
http://www.bttt99.com/v/27773/#download
