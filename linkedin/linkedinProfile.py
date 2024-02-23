from linkedin_api import Linkedin
from datetime import datetime

class linkedinProfile():
	def getProfile(username, currentOrg, email, password):
            currentOrgRegex = currentOrg.lower()
            obj = {}
            try:
                api = Linkedin(email, password)
                response = api.get_profile(username)
                #print(response)
                obj['username'] = username
                obj['headline'] = response['headline']
                obj['displayPictureUrl'] = ''
                try:
                    obj['displayPictureUrl'] = response['displayPictureUrl']
                except:
                    pass
                experiences = response['experience']
                obj['currentOrg'] = experiences[0]['companyName']
                obj['currentDesignation'] = experiences[0]['title']
                obj['previousOrg'] = ""
                end_date = datetime(year=2024, month=2, day=16)

                startYear = experiences[0]['timePeriod']['startDate']['year']
                startMonth = experiences[0]['timePeriod']['startDate'].get('month')
                if startMonth is None:
                    startMonth = 1
                start_date = datetime(year=startYear, 
                                month= startMonth, 
                                day=1)
                for experience in experiences[1:]:
                    if 'companyName' not in experience:
                        continue
                    if currentOrgRegex in experience['companyName'].lower():
                        startYear = experience['timePeriod']['startDate']['year']
                        startMonth = experience['timePeriod']['startDate'].get('month')
                        if startMonth is None:
                            startMonth = 1
                        start_date = datetime(year=startYear, 
                                month= startMonth, 
                                day=1)
                    else:
                        obj['previousOrg'] = experience['companyName']
                        break
                totalExperienceInMonths = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                obj['totalExperienceInCurrentOrgInYrs'] = str(totalExperienceInMonths//12) +' years & '+str(totalExperienceInMonths%12)+' months'
                for experience in experiences[1:]:
                    try:
                        #print(experience['timePeriod']['endDate']['year'])
                        start_date = datetime(year=experience['timePeriod']['startDate']['year'],month=experience['timePeriod']['startDate']['month'],day=1)
                        end_date = datetime(year=experience['timePeriod']['endDate']['year'],month=experience['timePeriod']['endDate']['month'],day=1)
                        total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                        totalExperienceInMonths += total_months
                    except:
                        pass
                obj['totalExperienceInYrs'] = str(totalExperienceInMonths//12) +' years & '+str(totalExperienceInMonths%12)+' months'
                educations = response['education']
                obj['college'] = ''
                for education in educations:
                    obj['college'] += education['schoolName'] + ", "
                #print(obj)
            except:
                pass
            return obj