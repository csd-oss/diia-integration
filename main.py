import requests
import time
from typing import Optional

class Diia_Connector():
    def generate_token(self):
        """
        Token Generation And Update Method -> void
        
        Side effects:
        - updating self.token with active token
        - updating self.lastRefresh with current unixtime
        """
        url = f"{self.endpoint}api/v1/auth/acquirer/{self.acquirer_token}"
        response = requests.get(url)
        self.token = response.json()['token']
        self.lastRefresh = int(time.time())
    
    def __init__(self, acquirer_token, endpoint, refresh_rate=7000):
        """
        Class for interaction with Diia 
        """
        self.endpoint = endpoint
        self.acquirer_token = acquirer_token
        self.refresh_rate = refresh_rate

        self.generate_token()

    def create_branch(self, custom_full_name, custom_full_address, name, street, house): 
        """
        Class for creation of branch 

        custom_full_name name of organisation making request
        custom_full_address address of organisation making request

        Side effects:
        - updating self.last_created_branch_id with last created branch
        """
        payload = {
            "customFullName":custom_full_name,
            "customFullAddress":custom_full_address,
            "name":name,
            "street":street,
            "house": house,
            "deliveryTypes": ["api"],
            "offerRequestType": "dynamic",
            "scopes": {
		        "identification": ["anonymous","faced"]
	        }
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.request("POST", f"{self.endpoint}api/v2/acquirers/branch", json=payload, headers=headers)
        print(response.text)
        self.last_created_branch_id = response.json()['_id']
        self.branch_id = response.json()['_id']
        return response.json()['_id']
    
    def get_branches_list(self):

        querystring = {"skip":"0","limit":"10"}

        headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.token}"
                }

        response = requests.request("GET", f"{self.endpoint}api/v1/acquirers/branches", headers=headers, params=querystring)
        
        return response.json()

    def delete_branch(self, branch_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.request("DELETE", f"{self.endpoint}api/v2/acquirers/branch/{branch_id}", headers=headers)

        if response.status_code == 204:
            return True
        else:
            return False


    def create_verification_offer(self, offering_name, scopes, branch_id, return_link = None,):
        """
        Class for creation of sharing offer for specific branch 

        offering_name name service recived by individual for wich identification is needed
        return_link(optional) link to wich user will be redirected after sucsesfull verification
        scopes wich data needs to be acquired, can't be more than branch permissions

        Side effects:
        - updating self.last_created_offer_id with last created branch
        """
        if return_link == None or return_link == "":
            payload = {
                "name": offering_name,
                "scopes": scopes
            }
        else:
            payload = {
                "name": offering_name,
                "returnLink": return_link,
                "scopes": scopes
            }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.request("POST", f"{self.endpoint}api/v1/acquirers/branch/{branch_id}/offer", json=payload, headers=headers)
        
        self.last_created_offer_id = response.json()['_id']

        return response.json()['_id']

    def create_deeplink(self, branch_id, return_deeplink, user_id):
        payload = {
            "branchId":branch_id ,
            "returnDeeplink": return_deeplink,
            "id": user_id
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.request("POST", f"{self.endpoint}api/v1/acquirers/identification" , json=payload, headers=headers)
        print(response.text)
        return response.json()['deeplink']