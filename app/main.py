import sys
from datetime import datetime

from app.card import card


def main():
    __version__ = "1.1.5"
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
            "personal_details": {
                "name": "Soumyajit Basu",
                "also_known_as": "corefinder",
                "email": "soumyajit.basu62@gmail.com",
                "current_location": "Bengaluru, karnataka",
                "zip_code": 560078
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
