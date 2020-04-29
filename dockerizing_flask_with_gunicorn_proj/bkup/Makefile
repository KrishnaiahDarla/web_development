default: build

build:
	docker build --no-cache -t activity-service:latest .
  
run:
	docker run -d --name activity-service -p 1014:80 $(SD_DOCKER_OPTS) -v /usr1/volumes/data/logs:/logs -v /usr1/volumes/envs/activity-service-aws-credentials:/root/.aws/credentials -v /usr1/volumes/activity-service/data/tmp:/data/tmp -v /usr1/volumes/envs/activity-service.env:/app/.env --env-file /usr1/volumes/envs/activity-service.env activity-service:latest

term:
	docker run -it --rm -p 1014:80 $(SD_DOCKER_OPTS) -v /usr1/volumes/data/logs:/logs -v /usr1/volumes/envs/activity-service-aws-credentials:/root/.aws/credentials -v /usr1/volumes/activity-service/data/tmp:/data/tmp -v /usr1/volumes/envs/activity-service.env:/app/.env --env-file /usr1/volumes/envs/activity-service.env activity-service:latest bash
