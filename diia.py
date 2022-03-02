# -*- coding: utf-8 -*-

from config import DIIA_BASE_URL, DIIA_ACQUIRER_TOKEN
from main import Diia_Connector
import uuid

diia = Diia_Connector(
    acquirer_token = DIIA_ACQUIRER_TOKEN,
    endpoint = DIIA_BASE_URL
)

diia.create_branch(
    custom_full_name = "Міністерство оборони України",
    custom_full_address = "м. Київ, Повітрофлотський проспект, 6",
    name = "Міністерство оборони України",
    street = "Повітрофлотський проспект",
    house = "6" )

diia.create_verification_offer(
    offering_name="Верифікація для чат боту",
    scopes={
		 "identification": ["anonymous","faced"]
	 }, 
    branch_id=diia.last_created_branch_id,)

deeplink = diia.create_deeplink(
    branch_id=diia.last_created_branch_id,
    return_deeplink="google.com",
    user_id=str(uuid.uuid4()))

print(deeplink)