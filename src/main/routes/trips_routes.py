from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint("trips_routes", __name__)

#Importação de Controllers
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_finder import LinkFinder
from src.controllers.link_creator import LinkCreator

from src.controllers.activity_creator import ActivityCreator
from src.controllers.participant_creator import ParticipantCreator

#Importação de Repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

#importando os gerentes de conexões
from src.models.settings.db_connection_handler import db_connection_handler

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trips():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    email_repository = EmailsToInviteRepository(conn)
    
    controller = TripCreator(trips_repository, email_repository)
    response = controller.create(request.json)
    
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    controller = TripFinder(trips_repository)
    response = controller.find_trip_details(tripId)
    
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    controller = TripConfirmer(trips_repository)
    response = controller.confirm(tripId)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)
    
    response = controller.create(request.json,tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)
    
    response = controller.find(tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantCreator(participants_repository,email_repository)
    
    response = controller.create(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_Repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activities_Repository)
    
    response = controller.create(request.json,tripId)
    return jsonify(response["body"]), response["status_code"]
    