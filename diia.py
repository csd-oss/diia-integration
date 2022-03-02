# -*- coding: utf-8 -*-

from config import DIIA_BASE_URL, DIIA_ACQUIRER_TOKEN
from main import Diia_Connector
import uuid

diia = Diia_Connector(
    acquirer_token = DIIA_ACQUIRER_TOKEN,
    endpoint = DIIA_BASE_URL
)

# all_branches = diia.get_branches_list()
# print(all_branches['total'])
# if all_branches['total'] > 1:
#     for barnch in all_branches['branches']:
#         diia.delete_branch(barnch['_id'])
#         print(f"Deleted branch {barnch['_id']} ")

#     branch_id = diia.create_branch(
#         custom_full_name = "Міністерство оборони України",
#         custom_full_address = "м. Київ, Повітрофлотський проспект, 6",
#         name = "Міністерство оборони України",
#         street = "Повітрофлотський проспект",
#         house = "6" )
#     diia.branch_id = branch_id
# else: 
#     diia.branch_id = all_branches['branches'][0]['_id']


# deeplink = diia.create_deeplink(
#     branch_id=diia.branch_id,
#     return_deeplink="google.com",
#     user_id=str(uuid.uuid4()))

# print(deeplink)