import pytest # type: ignore
import uuid
from datetime import datetime, timedelta
from .links_repository import LinksRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    link_infos = {
        "id":link_id,
        "trip_id":trip_id,
        "link": "https://www.example.com",
        "title": "Hotel"
    }
    
    links_repository.registry_links(link_infos)
    
@pytest.mark.skip(reason="interacao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    response = links_repository.find_links_from_trip(trip_id)
    assert isinstance(response,list)
    assert isinstance(response[0], tuple)


