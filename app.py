from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Resume API', description='API for extracting details from multiple resumes')

# Sample data
resumes = {
    1: {
        "contact": {
            "name": "Rosendo Inzunza",
            "phone": "111-000-1111",
            "location": "Brea, CA",
            "email": "test1a@gmail.com"
        },
        "professional_experience": [
            {
                "position": "Site Reliability Engineer",
                "company": "A",
                "location": "Los Angeles, CA",
                "duration": "7/2022 - Present",
                "responsibilities": [
                    "Spearhead the maintenance and continuous upgrading of services hosted on cloud infrastructure within a Linux environment, ensuring optimal performance and reliability for millions of Tiktok users worldwide.",
                    "Successfully orchestrated the setup of a robust backend Flask service and frontend Node service for a new datacenter...",
                ]
                },  
        ], 
        "education": [ {"degree": "Bachelors of Science in Computer Science", "institution": "California State University Fullerton", "location": "Fullerton", "duration": "02/2015 - 08/2019"} ]
    },
    2: {
    "contact": {
        "name": "Ro-in",
        "phone": "111-222-3333",
        "location": "Anaheim, CA",
        "email": "test2@gmail.com"
    },
    "professional_experience": [
        {
            "position": "Engineer",
            "company": "B",
            "location": "San Diego, CA",
            "duration": "10/2021 - 7/2022",
            "responsibilities": [
                "Spearhead the maintenance and continuous upgrading of services hosted on cloud infrastructure within a Linux environment, ensuring optimal performance and reliability for millions of Tiktok users worldwide.",
                "Successfully orchestrated the setup of a robust backend Flask service and frontend Node service for a new datacenter...",
            ]
            },  
    ], 
    "education": [ {"degree": "Bachelors of Science in Science", "institution": "California State University Fullerton", "location": "Fullerton", "duration": "02/2015 - 08/2019"} ]
}
}


""" Endpoint definitions """
@api.route('/get_all_contacts')
class GetAllContacts(Resource):
    def get(self):
        return {contact_id: details["contact"] for contact_id, details in resumes.items()}


@api.route('/get_contact_details/<int:id>')
class GetContactDetails(Resource):
    def get(self, id):
        if id in resumes:
            contact_details = resumes[id]["contact"].copy()
            city, state = contact_details.pop('location').split(', ')
            contact_details['address'] = {
                'city': city.strip(),
                'state': state.strip()
            }
            return contact_details
        return {"message": "Contact not found"}, 404


@api.route('/get_professional_experience/<int:id>')
class GetProfessionalExperience(Resource):
    def get(self, id):
        if id in resumes:
            return resumes[id]["professional_experience"]
        return {"message": "Professional experience not found"}, 404


@api.route('/get_education/<int:id>')
class GetEducation(Resource):
    def get(self, id):
        if id in resumes:
            return resumes[id]["education"]
        return {"message": "Education details not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)


"""
v1
API
- web documentation
- responses need to be consistent
- data read from db needs to be consistent
- create unit tests using the data


create DB scheme
- create db
- read data from db into endpoints

messaging system
- kafka/ rabbitmq

v2
- config center
- frontend to display projects and resume
-- consume resume data from api I made
"""

"""
API data

- GET /all_contacts {1: Rosendo}
- GET /contact details/{1}
- 
"""