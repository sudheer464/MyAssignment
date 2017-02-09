#!/bin/bash

endpoints --prefix=mycontroller --host=localhost:8000 &

# print all the posts
curl http://localhost:8000/posts

#publish a post

# curl http://localhost:8000/post  -d "title='fred'" -d "body='this stuff'"
# json data
curl -H "Content-Type: application/json" \
 -X POST -d '{"title":"xyz","body":"my blog post"}' http://localhost:8000/post  

curl -H "Content-Type: application/json" \
 -X POST -d '{"title":"one more time","body":"my blog post with content"}' http://localhost:8000/post  

# see if we added 

curl http://localhost:8000/posts

kill %1
