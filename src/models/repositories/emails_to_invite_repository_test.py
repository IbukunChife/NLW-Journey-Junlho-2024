import pytest # type: ignore
import uuid
from datetime import datetime, timedelta
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    email_trips_infos = {
        "id":str(uuid.uuid4()),
        "trip_id":trip_id,
        "email": "olaMundo@example.com"
    }
    
    emails_to_invite_repository.registry_email(email_trips_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print(emails)
    
