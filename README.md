# Movie downloader

## Features
- Extracted information each movie from [golchindls](https://golchindls.ir/) website.
- Storage data and information for each movie in the database (in sqlite for test but mysql in final product).


## vertual envaierment
1. **Create a vertual envaierment with `venv`**
```bash
# This .venv name example
python -m venv .venv
```
2. **Activate `.venv`**
```bash
source .venv/bin/activate
```
3. **Install all dependences with requairement file**
```bash
pip install -r requairement.txt
```

## use `.env` 
- rename `.env.sample` file to `.env`:
### Linux
```bash
mv .env.sample .env
```
- enter information in the relevant fields(for example):
```python
DATABASE_ADDRESS = "sqlite:///./db_name.db"
```

## Log Files
- All log file this blowe address storage  
**log files address** : `logger/logs/*`


## TODO
- [ ] add watch and watchn't movies in database for analisis movies data for recommender to user.
- [X] add limit for imdb rate in extracted.
- [X] add logger
  - [X] add logger in main file
  - [X] add logger in db
  - [X] add logger in extraction data
- [X] add scheduler for app
