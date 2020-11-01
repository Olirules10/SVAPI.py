import requests
import json

session = requests.Session()
session.trust_env = False

# USER
def GetUserDataFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/User/GetUser?SVID={SVID}").text
    if "Could not find" in result:
        raise Exception("GetUser: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetUsernameFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/User/GetUsername?SVID={SVID}").text
    if "Could not find" in result:
        raise Exception("GetUsername: Param(s) are invalid.")
    else:
        return  result

def GetSVIDFromUsername(username):
    result = requests.get(f"https://api.spookvooper.com/User/GetSVIDFromUsername?username={username}").text
    if "Could not find" in result:
        raise Exception("GetSVIDFromUsername: Param(s) are invalid.")
    else:
        return  result

def GetUsernameFromDiscord(discordid):
    result = requests.get(f"https://api.spookvooper.com/User/GetUsernameFromDiscord?discordid={discordid}").text
    if "Could not find" in result:
        raise Exception("GetUsernameFromDiscord: Param(s) are invalid.")
    else:
        return  result

def GetSVIDFromDiscord(discordid):
    result = requests.get(f"https://api.spookvooper.com/User/GetSVIDFromDiscord?discordid={discordid}").text
    if "Could not find" in result:
        raise Exception("GetSVIDFromDiscord: Param(s) are invalid.")
    else:
        return  result

def GetUsernameFromMinecraft(minecraftid):
    result = requests.get(f"https://api.spookvooper.com/User/GetUsernameFromMinecraft?minecraftid={minecraftid}").text
    if "Could not find" in result:
        raise Exception("GetUsernameFromMinecraft: Param(s) are invalid.")
    else:
        return  result

def GetSVIDFromMinecraft(minecraftid):
    result = requests.get(f"https://api.spookvooper.com/User/GetSVIDFromMinecraft?minecraftid={minecraftid}").text
    if "Could not find" in result:
        raise Exception("GetSVIDFromMinecraft: Param(s) are invalid.")
    else:
        return  result

def HasDiscordRoleFromSVIDandRole(SVID, role):
    result = requests.get(f"https://api.spookvooper.com/User/HasDiscordRole?userid={SVID}&role={role}").text
    if "Could not find" in result:
        raise Exception("HasDiscordRoleFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDiscordRolesFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/User/HasDiscordRole?SVID={SVID}").text
    if "Could not find" in result:
        raise Exception("GetDiscordRolesFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDiscordIdFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/User/GetUser?SVID={SVID}").text
    if "Could not find" in result:
        raise Exception("GetDiscordRolesFromSVID: Param(s) are invalid.")
    else:
        data = json.loads(result)
        discordid = data["discord_id"]
        return discordid

def GetDaysSinceLastMoveFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/User/GetDaysSinceLastMove?SVID={SVID}").text
    if "Could not find" in result:
        raise Exception("GetDaysSinceLastMoveFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetSenators():
    result = requests.get("https://api.spookvooper.com/User/GetSenators").text
    return result

# GROUP
def DoesGroupExistFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/Group/DoesGroupExist?svid={SVID}").text
    if "Could not find" in result:
        raise Exception("DoesGroupExistFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetGroupMembersFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/Group/GetGroupMembers?svid={SVID}").text
    if "Could not find" in result:
        raise Exception("GetGroupMembersFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def HasGroupPermissionFromSVIDandUserSVIDandPermission(SVID, userSVID, permission):
    result = requests.get(f"https://api.spookvooper.com/Group/HasGroupPermission?svid={SVID}&userSVID={userSVID}&permission={permission}").text
    if "Could not find" in result:
        raise Exception("HasGroupPermissionFromSVIDandUserSVIDandPermission: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetSVIDFromGroupname(groupname):
    result = requests.get(f"https://api.spookvooper.com/Group/GetSVIDFromName?name={groupname}").text
    if "Could not find" in result:
        raise Exception("GetSVIDFromGroupname: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetGroupnameFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/Group/GetName?svid={SVID}").text
    if "Could not find" in result:
        raise Exception("GetName: Param(s) are invalid.")
    else:
        return json.loads(result)

# ECO
def GetBalanceFromSVID(SVID):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetBalance?svid={SVID}").text
    if "Could not find" in result:
        raise Exception("GetBalanceFromSVID: Param(s) are invalid.")
    else:
        return json.loads(result)

def SendTransactionByIDs(sender_svid, receiver_svid, amount, auth, detail):
    result = requests.get(f"https://api.spookvooper.com/Eco/SendTransactionByIDs?from={sender_svid}&to={receiver_svid}&amount={amount}&auth={auth}&detail={detail}").text
    if "Could not find" in result:
        raise Exception("SendTransactionByIDs: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetStockValueFromTicker(ticker):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetStockValueFromTicker?ticker={ticker}").text
    if "Could not find" in result:
        raise Exception("GetStockValueFromTicker: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetStockHistory(ticker, time_type, count, interval):
    if count > 60:
        raise Exception("GetStockHistory: Count must not be greater than 60.")
    result = requests.get(f"https://api.spookvooper.com/Eco/GetStockHistory?ticker={ticker}&type={time_type}&count={count}&interval={interval}").text
    if "Could not find" in result:
        raise Exception("GetStockHistory: Param(s) are invalid.")
    else:
        return json.loads(result)

def SubmitStockBuy(ticker, count, price, accountid, auth):
    result = requests.get(f"https://api.spookvooper.com/Eco/SubmitStockBuy?ticker={ticker}&count={count}&price={price}&accountid={accountid}&auth={auth}").text
    if "Could not find" in result:
        raise Exception("SubmitStockBuy: Param(s) are invalid.")
    else:
        return json.loads(result)

def SubmitStockSell(ticker, count, price, accountid, auth):
    result = requests.get(f"https://api.spookvooper.com/Eco/SubmitStockSell?ticker={ticker}&count={count}&price={price}&accountid={accountid}&auth={auth}").text
    if "Could not find" in result:
        raise Exception("SubmitStockSell: Param(s) are invalid.")
    else:
        return json.loads(result)

def CancelOrder(orderid, accountid, auth):
    result = requests.get(f"https://api.spookvooper.com/Eco/CancelOrder?orderid={orderid}&accountid={accountid}&auth={auth}").text
    if "Could not find" in result:
        raise Exception("CancelOrder: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetStockBuyPrice(ticker):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetStockBuyPrice?ticker={ticker}").text
    if "Could not find" in result:
        raise Exception("GetStockBuyPrice: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetQueueInfo(ticker, action_type):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetQueueInfo?ticker={ticker}&type={action_type}").text
    if "Could not find" in result:
        raise Exception("GetQueueInfo: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetUserStockOffers(ticker, SVID):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetUserStockOffers?ticker={ticker}&svid={SVID}").text
    if "Could not find" in result:
        raise Exception("GetUserStockOffers: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDistrictWealth(district_name):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetDistrictWealth?id={district_name}").text
    if "Could not find" in result:
        raise Exception("GetDistrictWealth: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDistrictUserWealth(district_name):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetDistrictUserWealth?id={district_name}").text
    if "Could not find" in result:
        raise Exception("GetDistrictUserWealth: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetDistrictGroupWealth(district_name):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetDistrictGroupWealth?id={district_name}").text
    if "Could not find" in result:
        raise Exception("GetDistrictGroupWealth: Param(s) are invalid.")
    else:
        return json.loads(result)

def GetOwnerData(ticker):
    result = requests.get(f"https://api.spookvooper.com/Eco/GetOwnerData?ticker={ticker}").text
    if "Could not find" in result:
        raise Exception("GetOwnerData: Param(s) are invalid.")
    else:
        return json.loads(result)
