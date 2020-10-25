import requests

# USER
def GetUserDataFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/GetUser?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetUser: {}".format(SVID))
    else:
        return  result

def GetUsernameFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/GetUsername?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetUsername: {}".format(SVID))
    else:
        return  result

def GetSVIDFromUsername(username):
    result = requests.get("https://api.spookvooper.com/User/GetSVIDFromUsername?username={}".format(username)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromUsername: {}".format(username))
    else:
        return  result

def GetUsernameFromDiscord(discordid):
    result = requests.get("https://api.spookvooper.com/User/GetUsernameFromDiscord?username={}".format(discordid)).text
    if "Could not find" in result:
        raise Exception("GetUsernameFromDiscord: {}".format(discordid))
    else:
        return  result

def GetSVIDFromDiscord(discordid):
    result = requests.get("https://api.spookvooper.com/User/GetSVIDFromDiscord?discordid={}".format(discordid)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromDiscord: {}".format(discordid))
    else:
        return  result

def GetUsernameFromMinecraft(minecraftid):
    result = requests.get("https://api.spookvooper.com/User/GetUsernameFromMinecraft?minecraftid={}".format(minecraftid)).text
    if "Could not find" in result:
        raise Exception("GetUsernameFromMinecraft: {}".format(minecraftid))
    else:
        return  result

def GetSVIDFromMinecraft(minecraftid):
    result = requests.get("https://api.spookvooper.com/User/GetSVIDFromMinecraft?minecraftid={}".format(minecraftid)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromMinecraft: {}".format(minecraftid))
    else:
        return  result

def HasDiscordRoleFromSVIDandRole(SVID, role):
    result = requests.get("https://api.spookvooper.com/User/HasDiscordRole?userid={}&role={}".format(SVID, role)).text
    if "Could not find" in result:
        raise Exception("HasDiscordRoleFromSVID: {}, {}".format(SVID, role))
    else:
        # result is a bool
        return bool(result)

def GetDiscordRolesFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/HasDiscordRole?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetDiscordRolesFromSVID: {}".format(SVID))
    else:
        # result is a list
        return result

def GetDaysSinceLastMoveFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/GetDaysSinceLastMove?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetDaysSinceLastMoveFromSVID: {}".format(SVID))
    else:
        # result is an integer
        return result

# GROUP
def DoesGroupExistFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Group/DoesGroupExist?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("DoesGroupExistFromSVID: {}".format(SVID))
    else:
        # result is a bool
        return bool(result)

def GetGroupMembersFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Group/GetGroupMembers?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetGroupMembersFromSVID: {}".format(SVID))
    else:
        # result is a list
        return result

def HasGroupPermissionFromSVIDandUserSVIDandPermission(SVID, userSVID, permission):
    result = requests.get("https://api.spookvooper.com/Group/HasGroupPermission?svid={}&userSVID={}&permission={}".format(SVID, userSVID, permission)).text
    if "Could not find" in result:
        raise Exception("HasGroupPermissionFromSVIDandUserSVIDandPermission: {}".format(SVID))
    else:
        # result is a bool
        return bool(result)

def GetSVIDFromGroupname(groupname):
    result = requests.get("https://api.spookvooper.com/Group/GetSVIDFromName?name={}".format(groupname)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromGroupname: {}".format(groupname))
    else:
        return result

def GetGroupnameFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Group/GetName?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetName: {}".format(SVID))
    else:
        return result

# ECO
def GetBalanceFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Eco/Getbalance?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetBalanceFromSVID: {}".format(SVID))
    else:
        return result
