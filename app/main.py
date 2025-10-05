import sys
import time
from datetime import datetime

from app.card import card
from app.url_shortener import URLShortener

def main():
    __version__ = "1.2.7"
    
    # Handle command line arguments first
    if "--version" in sys.argv[1:]:
        print(__version__)
        exit(0)

    if "--help" in sys.argv[1:]:
        print("To install the module run pip install --user corefinder")
        print("To execute the package run corefinder")
        print("To check for the version number please run corefinder --version")
        print("To run with persistent server use corefinder --daemon")
        print("The URL shortener server will run for 5 minutes by default")
        exit(0)
    
    # Initialize URL shortener with error handling
    url_shortener = None
    
    try:
        url_shortener = URLShortener(port=8888, display_host='cf.link')
        time.sleep(2)  # Give server time to start
    except Exception as e:
        # URL shortener failed to initialize - will show regular URLs
        pass
    
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
                "linkedin_profile": url_shortener.create_terminal_link("https://www.linkedin.com/in/soumyajit-basu-5a783886/") if url_shortener else "https://www.linkedin.com/in/soumyajit-basu/",
                "github_profile": url_shortener.create_terminal_link("https://github.com/Corefinder89") if url_shortener else "https://github.com/Corefinder89",
                "bitbucket_profile": url_shortener.create_terminal_link("https://bitbucket.org/CodersDen/") if url_shortener else "https://bitbucket.org/CodersDen/"
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
                    "link": url_shortener.create_terminal_link("https://success.simplilearn.com/45341790") if url_shortener else "https://success.simplilearn.com/45341790",
                },
                "certification-3": {
                    "certification_name": "Backend API testing using python",
                    "issued_by": "Udemy",
                    "issued_date": "April, 2018",
                    "credentials": "UC-N7XQAPSW",
                    "link": url_shortener.create_terminal_link("https://www.udemy.com/certificate/UC-N7XQAPSW/") if url_shortener else "https://www.udemy.com/certificate/UC-N7XQAPSW/"
                },
                "certification-4": {
                    "certification_name": "Selenium WebDriver with Python 3.x from novice to ninja",
                    "issued_by": "Udemy",
                    "issued_date": "July, 2017",
                    "credentials": "UC-VB821J3L",
                    "link": url_shortener.create_terminal_link("https://www.udemy.com/certificate/UC-VB821J3L/") if url_shortener else "https://www.udemy.com/certificate/UC-VB821J3L/"
                },
                "certification-5": {
                    "certification_name": "Forging CI pipelines for selenium with kubernetes and aws",
                    "issued_by": "The Test Tribe",
                    "issued_date": "November, 2024"
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
            },
            "accolades": {
                "accolade-1": {
                    "title": "Dzone core member",
                    "issued_by": "Dzone",
                    "issued_date": "October, 2023",
                    "credentials": 25519461103392,
                    "description": "Awarded for being the most valuable blogger contributing actively to the Dzone community.",
                    "link": url_shortener.create_terminal_link("https://verified.sertifier.com/en/verify/25519461103392/") if url_shortener else "https://verified.sertifier.com/en/verify/25519461103392/"
                },
                "accolade-2": {
                    "title": "Certificate of participation",
                    "issued_by": "Shree Agrasain College",
                    "issued_date": "October, 2025",
                    "description": "Resource person for delivering a seminar to the students of the college"
                },
                "accolade-3": {
                    "title": "Team Excellence",
                    "issued_by": "Encora",
                    "issued_date": "June, 2024, October 2023",
                    "description": "Awarded for being a team player",
                },
                "accolade-4": {
                    "title": "Living our values",
                    "issued_by": "Encora",
                    "issued_date": "July, 2025",
                    "description": "Awarded for outstanding performance for the quarter"
                }
            }
        }
    }

    print(card(my_data, work_exp))
    
    # Keep URL shortener server alive for link redirects
    if url_shortener:
        try:
            if "--daemon" in sys.argv[1:]:
                print("Use Ctrl+C to stop")
                while True:
                    time.sleep(1)
            else:
                print("Server will run for 60 seconds")
                print("Use 'corefinder --daemon' to run indefinitely")
                print("Or press Ctrl+C to stop early")

                # Run for 60 seconds by default
                total_time = 60
                for remaining in range(total_time, 0, -1):
                    # Calculate progress
                    elapsed = total_time - remaining
                    progress = elapsed / total_time
                    bar_length = 40
                    filled_length = int(bar_length * progress)
                    
                    # Create progress bar
                    bar = '█' * filled_length + '░' * (bar_length - filled_length)
                    percentage = int(progress * 100)
                    
                    # Print progress bar with carriage return to overwrite
                    print(f"\rServer: [{bar}] {percentage}% ({remaining}s remaining)", end='', flush=True)
                    time.sleep(1)

                print("\n\n60 seconds elapsed - stopping server")

        except KeyboardInterrupt:
            print("\nShutting down server...")
        finally:
            if url_shortener:
                url_shortener.close()
                print("Server stopped successfully!")


if __name__ == '__main__':
    main()
