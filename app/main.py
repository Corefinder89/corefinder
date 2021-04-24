from datetime import datetime


def main():
    career_start_date = datetime.strptime("2014-12-11", "%Y-%m-%d")
    career_continue_date = datetime.now().strftime("%Y-%m-%d")
    career_continue_date = datetime.strptime(career_continue_date, "%Y-%m-%d")
    tot_days = abs(career_continue_date - career_start_date).days
    num_years = int(tot_days / 365)
    num_weeks = int((tot_days % 365) / 7)
    num_months = int(num_weeks / 4)
    work_exp = f"{num_years} years and {num_months} months"


if __name__ == '__main__':
    main()
