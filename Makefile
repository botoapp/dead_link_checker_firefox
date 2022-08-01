CONTAINER_NAME=`basename "${PWD}"`

build:
	docker build --platform linux/amd64 -t ${CONTAINER_NAME}:latest . 

shell:
	docker run --platform linux/amd64 -ti --rm \
	--entrypoint="" \
	-v `pwd`:/var/task ${CONTAINER_NAME} bash

py:
	docker run --platform linux/amd64 -ti --rm \
	--entrypoint="" \
	-v `pwd`:/var/task ${CONTAINER_NAME} python

run:
	docker run --platform linux/amd64 -ti --rm \
	-p 9000:8080 \
	-v `pwd`:/var/task \
	${CONTAINER_NAME}

exec:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
