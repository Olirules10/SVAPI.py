import requests
import json

# USER
def GetUserDataFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/GetUser?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetUser: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetUsernameFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/GetUsername?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetUsername: Param(s) are invalid.")
    else:
        return  result

def GetSVIDFromUsername(username):
    result = requests.get("https://api.spookvooper.com/User/GetSVIDFromUsername?username={}".format(username)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromUsername: Param(s) are invalid.")
    else:
        return  result

def GetUsernameFromDiscord(discordid):
    result = requests.get("https://api.spookvooper.com/User/GetUsernameFromDiscord?username={}".format(discordid)).text
    if "Could not find" in result:
        raise Exception("GetUsernameFromDiscord: Param(s) are invalid.")
    else:
        return  result

def GetSVIDFromDiscord(discordid):
    result = requests.get("https://api.spookvooper.com/User/GetSVIDFromDiscord?discordid={}".format(discordid)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromDiscord: Param(s) are invalid.")
    else:
        return  result

def GetUsernameFromMinecraft(minecraftid):
    result = requests.get("https://api.spookvooper.com/User/GetUsernameFromMinecraft?minecraftid={}".format(minecraftid)).text
    if "Could not find" in result:
        raise Exception("GetUsernameFromMinecraft: Param(s) are invalid.")
    else:
        return  result

def GetSVIDFromMinecraft(minecraftid):
    result = requests.get("https://api.spookvooper.com/User/GetSVIDFromMinecraft?minecraftid={}".format(minecraftid)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromMinecraft: Param(s) are invalid.")
    else:
        return  result

def HasDiscordRoleFromSVIDandRole(SVID, role):
    result = requests.get("https://api.spookvooper.com/User/HasDiscordRole?userid={}&role={}".format(SVID, role)).text
    if "Could not find" in result:
        raise Exception("HasDiscordRoleFromSVID: Param(s) are invalid.")
    else:
        return bool(result)

def GetDiscordRolesFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/HasDiscordRole?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetDiscordRolesFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDaysSinceLastMoveFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/User/GetDaysSinceLastMove?SVID={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetDaysSinceLastMoveFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

# GROUP
def DoesGroupExistFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Group/DoesGroupExist?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("DoesGroupExistFromSVID: Param(s) are invalid.")
    else:
        return bool(result)

def GetGroupMembersFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Group/GetGroupMembers?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetGroupMembersFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def HasGroupPermissionFromSVIDandUserSVIDandPermission(SVID, userSVID, permission):
    result = requests.get("https://api.spookvooper.com/Group/HasGroupPermission?svid={}&userSVID={}&permission={}".format(SVID, userSVID, permission)).text
    if "Could not find" in result:
        raise Exception("HasGroupPermissionFromSVIDandUserSVIDandPermission: Param(s) are invalid.")
    else:
        return bool(result)

def GetSVIDFromGroupname(groupname):
    result = requests.get("https://api.spookvooper.com/Group/GetSVIDFromName?name={}".format(groupname)).text
    if "Could not find" in result:
        raise Exception("GetSVIDFromGroupname: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetGroupnameFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Group/GetName?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetName: Param(s) are invalid.")
    else:
        return json.loads(result)

# ECO
def GetBalanceFromSVID(SVID):
    result = requests.get("https://api.spookvooper.com/Eco/Getbalance?svid={}".format(SVID)).text
    if "Could not find" in result:
        raise Exception("GetBalanceFromSVID: Param(s) are invalid.")
    else:
        return float(result)

def SendTransactionByIDs(sender_svid, receiver_svid, amount, auth, detail):
    result = requests.get("https://api.spookvooper.com/Eco/SendTransactionByIDs?from={}&to={}&amount={}&auth={}&detail={}".format(sender_svid, receiver_svid, amount, auth, detail)).text
    if "Could not find" in result:
        raise Exception("SendTransactionByIDs: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetStockValueFromTicker(ticker):
    result = requests.get("https://api.spookvooper.com/Eco/GetStockValueFromTicker?ticker={}".format(ticker)).text
    if "Could not find" in result:
        raise Exception("GetStockValueFromTicker: Param(s) are invalid.")
    else:
        return float(result)

def GetStockHistory(ticker, time_type, count, interval):
    if count > 60:
        raise Exception("GetStockHistory: Count must not be greater than 60.")
    result = requests.get("https://api.spookvooper.com/Eco/GetStockHistory?ticker={}&type={}&count={}&interval={}".format(ticker, time_type, count, interval)).text
    if "Could not find" in result:
        raise Exception("GetStockHistory: Param(s) are invalid.")
    else:
        return json.loads(result)

def SubmitStockBuy(ticker, count, price, accountid, auth):
    result = requests.get("https://api.spookvooper.com/Eco/SubmitStockBuy?ticker={}&count={}&price={}&accountid={}&auth={}".format(ticker, count, price, accountid, auth)).text
    if "Could not find" in result:
        raise Exception("SubmitStockBuy: Param(s) are invalid.")
    else:
        return json.loads(result)

def SubmitStockSell(ticker, count, price, accountid, auth):
    result = requests.get("https://api.spookvooper.com/Eco/SubmitStockSell?ticker={}&count={}&price={}&accountid={}&auth={}".format(ticker, count, price, accountid, auth)).text
    if "Could not find" in result:
        raise Exception("SubmitStockSell: Param(s) are invalid.")
    else:
        return json.loads(result)

def CancelOrder(orderid, accountid, auth):
    result = requests.get("https://api.spookvooper.com/Eco/CancelOrder?orderid={}&accountid={}&auth={}".format(orderid, accountid, auth)).text
    if "Could not find" in result:
        raise Exception("CancelOrder: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetStockBuyPrice(ticker):
    result = requests.get("https://api.spookvooper.com/Eco/GetStockBuyPrice?ticker={}".format(ticker)).text
    if "Could not find" in result:
        raise Exception("GetStockBuyPrice: Param(s) are invalid.")
    else:
        return float(result)

def GetQueueInfo(ticker, action_type):
    result = requests.get("https://api.spookvooper.com/Eco/GetQueueInfo?ticker={}&type={}".format(ticker, action_type)).text
    if "Could not find" in result:
        raise Exception("GetQueueInfo: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetUserStockOffers(ticker, svid):
    result = requests.get("https://api.spookvooper.com/Eco/GetUserStockOffers?ticker={}&svid={}".format(ticker, svid)).text
    if "Could not find" in result:
        raise Exception("GetUserStockOffers: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDistrictWealth(svid):
    result = requests.get("https://api.spookvooper.com/Eco/GetDistrictWealth?id={}".format(svid)).text
    if "Could not find" in result:
        raise Exception("GetDistrictWealth: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDistrictUserWealth(svid):
    result = requests.get("https://api.spookvooper.com/Eco/GetDistrictUserWealth?id={}".format(svid)).text
    if "Could not find" in result:
        raise Exception("GetDistrictUserWealth: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDistrictGroupWealth(svid):
    result = requests.get("https://api.spookvooper.com/Eco/GetDistrictGroupWealth?id={}".format(svid)).text
    if "Could not find" in result:
        raise Exception("GetDistrictGroupWealth: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetOwnerData(ticker):
    result = requests.get("https://api.spookvooper.com/Eco/GetOwnerData?ticker={}".format(ticker)).text
    if "Could not find" in result:
        raise Exception("GetOwnerData: Param(s) are invalid.")
    else:
        return json.loads(result)
