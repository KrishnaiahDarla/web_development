default: build

build:
	docker build --no-cache -t flask_web_app:latest .
  
run:
	docker run -d --name flask_web_app -p 1014:80 $(SD_DOCKER_OPTS) -v /usr1/volumes/data/logs:/logs -v /usr1/volumes/flask_web_app/data/tmp:/data/tmp -v /usr1/volumes/envs/flask_web_app.env:/app/.env --env-file /usr1/volumes/envs/flask_web_app.env flask_web_app:latest

term:
	docker run -it --rm -p 1014:80 $(SD_DOCKER_OPTS) -v /usr1/volumes/data/logs:/logs -v /usr1/volumes/flask_web_app/data/tmp:/data/tmp -v /usr1/volumes/envs/flask_web-app.env:/app/.env --env-file /usr1/volumes/envs/flask_web_app.env flask_web_app:latest bash
