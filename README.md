# Movie downloader

## Features
- Extracted information each movie from [golchindls](https://golchindls.ir/) website.
- Storage data and information for each movie in the database(in sqlite for test but mysql in final product).

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

## TODO
- [ ] add watch and watchn't movies in database for analisis movies data for recommender to user.
- [X] add limit for imdb rate in extracted.
- [ ] add logger
 - [X] add logger in main file
 - [ ] add logger in db
 - [ ] add logger in extraction data
- [ ] add scheduler for app
