import sys
import re
import requests
import json
from datetime import datetime

def matching_dates_per_parter(dates, workind_dates):
    # meant to find a single partner's working dates (can attend at least 2 days in a row). Return list of dates
    potential_dates = []
    for idx, _date in enumerate(dates[:-1]):
        if(datetime.strptime(dates[idx], '%Y-%m-%d') - datetime.strptime(dates[idx+1], '%Y-%m-%d')).days == -1:
            potential_dates.append(dates[idx])
            workind_dates.add(dates[idx])
    return potential_dates


def get_availableDates(country_partners):
    # Returns list of attendees and optimal date to host
    # Initalize chosen date as none and declare variables
    chosen_date = None
    attending_partners = []
    workind_dates = set()
    potential_dates={}

    # create a list of all possible dates that the country could poitentially host an even and have at least 1 attendee
    for partner, dates in country_partners.items():
        potential_dates[partner] = matching_dates_per_parter(dates, workind_dates)

    # sort dates chronologically
    workind_dates = sorted(workind_dates, key=lambda x: datetime.strptime(x, '%Y-%m-%d'), reverse=True)[::-1]
    most_attending = 0
    attending_by_date_dict = {}

    # go through chronoligical workind dates and check which attendees can make each date, keeping track of highest attendece
    for date in workind_dates:
        attending_by_date_dict[date] = [] 
        attending = 0
        for partner, partner_dates in potential_dates.items():
            if partner_dates:
                for partner_date in partner_dates:
                    if partner_date == date:
                        attending_by_date_dict[date].append(partner) 
                        attending += 1   
        # only change highest attending if greater than not equal (prioritize earliest)
        if(attending > most_attending):
            most_attending = attending
            chosen_date = date
            attending_partners = attending_by_date_dict[date]    

    return attending_partners, chosen_date


def main():
    # Get the json formatted response from hubspot
    response = requests.get("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=12726f0dbcdab529193f10e791dd")
    
    # Convert response to a dict
    partners_dict = response.json()
    

    countries_dict = {}
    for partner in partners_dict['partners']:
        countries_dict[str(partner['country'])] = {}
        
    for partner in partners_dict['partners']:
        countries_dict[str(partner['country'])].update({partner['email']:partner['availableDates']})

    # Declare returning API response in desired format
    invitation_response = {}
    invitation_response['countries'] = []

    # Iterate by country find possible start dates and attendees in each country
    for country in countries_dict:
        country_invite={}

        # get country's attendee list and start date
        attendees, startDate = get_availableDates(countries_dict[country])

        country_invite['startDate'] = startDate
        country_invite['attendees'] = attendees
        country_invite['name'] = country
        country_invite['attendeeCount'] = len(attendees)

        # append country's complete invite list api post msg
        invitation_response['countries'].append(country_invite)
    
    # Post response
    r = requests.post('https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=12726f0dbcdab529193f10e791dd', data=json.dumps(invitation_response))
    print(r)
    return

if __name__ == "__main__":
    main()