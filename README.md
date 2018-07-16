# PTT NB Shopping Search Engine

## RUN
### Use docker
1. First, you need `docker` & `docker-compose`
2. `docker-compose build`
3. `docker-compose up -d`
4. Check [http://localhost:5000/](http://localhost:5000/)
5. If yout want to enter Solr Admin, check [http://localhost:8983/solr/](http://localhost:8983/solr/)

### Dev
1. Set up your Solr and copy deploy/solr/ptt/ to Solr core directory.
2. cd src
3. pip install -r reqirements.txt
4. python ./main.py
