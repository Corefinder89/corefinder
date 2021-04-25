import json
from datetime import datetime

from card import card


def main():
    __version__ = "1.0.0"
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

    # Get all details from json
    with open("app/details.json") as jsonobj:
        json_data = json.load(jsonobj)

    print(card(json_data, work_exp))


if __name__ == '__main__':
    main()
