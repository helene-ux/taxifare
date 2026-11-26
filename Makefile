run-api:
	uv run uvicorn api.fast:app --reload
docker_build_local:
	docker build -t api .
docker_run:
	docker run -p 8111:8080 api
