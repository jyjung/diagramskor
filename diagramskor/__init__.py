import os
from diagrams.custom import Custom

def get_current_path():
    return os.path.dirname(__file__)

service_list = [ 
    ("containerlinker", os.path.join(get_current_path(),"containerlinker.png")),
    ("infolineage", os.path.join(get_current_path(),"infolineage.png")),
    ("security365",os.path.join(get_current_path(),"security365.png")),
    ("shieldgate",os.path.join(get_current_path(),"shieldgate.png")),
    ("shieldinfo", os.path.join(get_current_path(), "shieldinfo.png")),
    ("shieldrive", os.path.join(get_current_path(), "shieldrive.png")),
    ("shieldrm", os.path.join(get_current_path(), "shieldrm.png")),
    ("cypherdocsflow", os.path.join(get_current_path(), "cypherdocsflow.png")),
    ("remotebrowser", os.path.join(get_current_path(), "remotebrowser.png")),
    ("shieldexmail", os.path.join(get_current_path(), "shieldexmail.png")),
    ("shieldid", os.path.join(get_current_path(), "shieldid.png")),
    ("shieldmail", os.path.join(get_current_path(), "shieldmail.png")),
    ("shieldriveworks", os.path.join(get_current_path(), "shieldriveworks.png")),
    ("shieldshare", os.path.join(get_current_path(), "shieldshare.png"))
]

def get_node(nodename: str, name: str):
    for service in service_list:
        if service[0] == nodename:
            return Custom(name, service[1])
    return Custom("Not Found", "notfound.png")
