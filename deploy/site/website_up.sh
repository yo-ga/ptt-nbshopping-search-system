sleep 15
echo "START"
python -c "from utils.import_data import import_json_to_solr; import_json_to_solr('/data/solr/output_json.json')"
python -c "from utils.import_data import import_json_to_solr; import_json_to_solr('/data/solr/output_selection.json')"
python3 ./main.py
