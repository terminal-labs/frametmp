import os
import os.path

_egg = ".egg-link"
_paylaod = "/payload"
_conf = "/conf.cfg"

SITEPACKAGESPATH = __file__

def resolve_payload_path(EGG_NAME, PROJECT_NAME):
    return os.path.dirname(__file__)
    possible_path = SITEPACKAGESPATH + "/" + EGG_NAME + _egg
    if os.path.exists(possible_path):
        egglink_file = open(possible_path, "r")
        link_path = egglink_file.read().split("\n")[0]
        possible_payload_path = link_path + "/" + PROJECT_NAME + _paylaod
    else:
        possible_path = SITEPACKAGESPATH + "/" + PROJECT_NAME
        possible_payload_path = possible_path + _paylaod
    return possible_payload_path

def payload_get_location():
    return resolve_payload_path(_egg, "spinglass")
