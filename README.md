# API_in_Django
This project is a sample Django REST API implementation for managing items

*Description

The project utilizes Django and Django REST Framework to create an API for handling items. It includes functionality for retrieving item data and adding new items.

*Installation

1. Clone the repository to your local machine
2. Install the required dependencies by running 'pip install 'r requirements.txt'
3. Configure the database settings in settings.py
4. Apply database migrations using the command 'python manage.py migrate'
5. Start development server with 'python manage.py runserver'

*Usage

Getting Data
To retrieve the existing item data, you can send a GET request to the /api/get-data/ endpoint. The response will contain a JSON object with the item information.

Adding an Item
To add a new item, send a POST request to the /api/add-item/ endpoint. Include the necessary data in the request body, following the JSON format expected by the API. The new item will be saved in the database.

#Contributing
Since it is a sample, so not open for Contribution
#Contact
For any queries and feedback, please contact[codexistslonglastingnotfog@gmail.com]



