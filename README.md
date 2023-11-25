# turism-backend-db-api
### Instructions for local run
clone this repository
```
git clone url_repository
```
create containers
```
docker compose -f docker-compose.yaml up
docker restart api
```
without docker, using pipenv
```python
python3 -m pip install pipenv #install pipenv
python3 -m pipenv shell #create virtual enviremont
pip install -r requirements.txt #install requirements
uvicorn src.main:app --reload --port 8000 #run server
```
