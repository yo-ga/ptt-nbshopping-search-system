FROM solr

COPY ./ptt /opt/solr/server/solr/configsets/ppt
USER root
RUN chown -R solr:solr /opt/solr/server/solr/configsets/ppt
USER solr
CMD ["/opt/solr/bin/solr", "-f"]
