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
**Database**
- [X] Impliment Singleton Desain Pattern
**Logger**
- [ ] Impliment Singleton Desain pattern
- [ ] Debug logger in production mode
**App**
- [ ] Debug run sceduler in production app
**Release**
- [ ] Create CI/CD on master branch for best practice release
