# -*- coding: utf-8 -*-

from config import DIIA_BASE_URL, DIIA_ACQUIRER_TOKEN
from main import Diia_Connector

diia = Diia_Connector(
    acquirer_token = DIIA_ACQUIRER_TOKEN,
    endpoint = DIIA_BASE_URL
)

diia.create_branch(
    custom_full_name = "Міністерство оборони України",
    custom_full_address = "03168, м. Київ-168, Повітрофлотський проспект, 6",
    name = "Міністерство оборони України",
    street = "Повітрофлотський проспект",
    house = "6" )

diia.create_verification_offer(
    offering_name="Верифікація для чат боту",
    scopes={ "identification":[]}, 
    branch_id=diia.last_created_branch_id,)

deeplink = diia.create_deeplink(
    branch_id=diia.last_created_branch_id,
    offer_id=diia.last_created_offer_id,
    user_id="1234567899")

print(deeplink)