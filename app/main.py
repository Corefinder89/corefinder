import sys
from datetime import datetime

from app.card import card


def main():
    __version__ = "1.1.7"
    career_start_date = datetime.strptime("2014-12-11", "%Y-%m-%d")
    career_continue_date = datetime.now().strftime("%Y-%m-%d")
    career_continue_date = datetime.strptime(career_continue_date, "%Y-%m-%d")

    # Get the total number of days of my experience
    tot_days = abs(career_continue_date - career_start_date).days
    num_years = int(tot_days / 365)
    num_weeks = int((tot_days % 365) / 7)
    num_months = int(num_weeks / 4)

    # Get the total work experience
    work_exp = f"{num_years} years and {num_months} months"

    my_data = {
        "attributes": {
            "profile": {
                "current_designation": "Senior software qa engineer (automation)",
                "organization": "Encora Inc.",
                "working_from": "November, 2020 - till date",
                "ex_organization": "Synup | Equifax | Automatad | Srijan",
                "linkedin_profile": "https://www.linkedin.com/in/soumyajit-basu-5a783886/",
                "github_profile": "https://github.com/Corefinder89",
                "bitbucket_profile": "https://bitbucket.org/CodersDen/"
            },
            "education": {
                "highest_degree": "Post graduation (MSc. computer applications)",
                "university": "Symbiosis International University (Deemed)"
            },
            "certifications": {
                "certification-1": {
                    "certification_name": "QA Infra workshop",
                    "issued_by": "The Test Tribe",
                    "issued_date": "November, 2024",
                    "credentials": "none",
                    "link": "none"
                },
                "certification-2": {
                    "certification_name": "Post Graduate Program in DevOps",
                    "issued_by": "Simplilearn",
                    "issued_date": "January, 2022",
                    "credentials": 45341790,
                    "link": "https://success.simplilearn.com/3bfa2dd8-1710-42d3-90bc-1ca3c1a3458e#acc.vMisnA7j",
                },
                "certification-3": {
                    "certification_name": "Backend API testing using python",
                    "issued_by": "Udemy",
                    "issued_date": "April, 2018",
                    "credentials": "UC-N7XQAPSW",
                    "link": "https://www.udemy.com/certificate/UC-N7XQAPSW/"
                },
                "certification-4": {
                    "certification_name": "Selenium WebDriver with Python 3.x from novice to ninja",
                    "issued_by": "Udemy",
                    "issued_date": "July, 2017",
                    "credentials": "UC-VB821J3L",
                    "link": "https://www.udemy.com/certificate/UC-VB821J3L/"
                }
            },
            "personal_details": {
                "name": "Soumyajit Basu",
                "also_known_as": "corefinder",
                "email": "soumyajit.basu62@gmail.com",
                "current_location": "Bengaluru, Karnataka",
                "zip_code_current": 560078,
                "permanent_location": "Kolkata, West Bengal",
                "zip_code_permanent": 700048,
                "blood_group": "B-"
            }
        }
    }

    if "--version" in sys.argv[1:]:
        print(__version__)
        exit(0)

    if "--help" in sys.argv[1:]:
        print("To install the module run pip install --user corefinder")
        print("To execute the package run corefinder")
        print("To check for the version number please run corefinder --version")
        exit(0)

    print(card(my_data, work_exp))


if __name__ == '__main__':
    main()
