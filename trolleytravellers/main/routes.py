from flask import Blueprint, request, jsonify
from trolleytravellers.main.utils import is_authenticated_customer, is_authenticated_volunteer
main = Blueprint('main', __name__)

database = r"./trolleytravellers/site.db"

@main.route('/customer_login', methods=['GET', 'POST'])
def customer_login():
    """ Checks the whether a username and password is found in the customer database and returns whether \
    the user is logged in or not.
    """

    json_body = request.get_json()

    customer_username, customer_password = "", ""

    for json_object in json_body:
        customer_username = json_object.get('username')
        customer_password = json_object.get('password')

    database_customer = is_authenticated_customer(customer_username, customer_password)
    failed_login = 'Login details incorrect, or no account found.'
    if database_customer:
        return jsonify({
            'Customer ID' : database_customer.id,
            'Username' : database_customer.username,
            'Email' : database_customer.email,
            'Postcode' : database_customer.postcode,
            'House Number' : database_customer.house_number
            })
    else:
        return jsonify({'Login Failure' : failed_login })


@main.route('/volunteer_login', methods=['GET', 'POST'])
def volunteer_login():
    """ Checks the whether a username and password is found in the volunteer database and returns whether \
    the user is logged in or not.
    """

    json_body = request.get_json()

    volunteer_username, volunteer_password = "", ""

    for json_object in json_body:
        volunteer_username = json_object.get('username')
        volunteer_password = json_object.get('password')
    
    database_volunteer = is_authenticated_volunteer(volunteer_username, volunteer_password)
    failed_login = 'Login details incorrect, or no account found.'
    if database_volunteer:
        return jsonify({
            'Volunteer ID' : database_volunteer.id,
            'Username' : database_volunteer.username,
            'Email' : database_volunteer.email,
            'Postcode' : database_volunteer.postcode,
            'House Number' : database_volunteer.house_number
            })
    else:
        return jsonify({'Login Failure' : failed_login })

