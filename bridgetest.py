# testing communications directly to the Bridge over local ports.
# The online documentation for the api is 3+ years out of date.
# The commands listed in the documentation do not match the'possibleRequests' returned from the current version of Bridge (2019)
# python 2.7 based script at this point.  Moving to Python 3 once I have comms working.
#
# Bridge returns JSON.

# sample output of the active commands below:
# {"folder":"Z:\\git\\quixel"}
# {"possibleRequests":["/GetMegascansFolder/","/GetSelectedAssets/","/GetSelectedAsset/","/GetDownloadedAssets/","/GetCustomAssets/","/GetOfflineAssets/","/Reload/","/log/","/error/"],"youSent":"/GetCommands/","status":"Error : Invalid request"}
# DONE LOGGING STR
# Reported Error

import urllib2

# {"possibleRequests":
#   [
#       "/GetMegascansFolder/"
#       "/GetSelectedAssets/"
#       "/GetSelectedAsset/"
#       "/GetDownloadedAssets/"
#       "/GetCustomAssets/"
#       "/GetOfflineAssets/"
#       "/Reload/"
#       "/log/"
#       "/error/"
#   ]

getMsFolders = 'http://localhost:28241/GetMegascansFolder/'
getMsCustomAssets = 'http://localhost:28241/GetCustomAssets/'
getMsSelectedAsset = 'http://localhost:28241/GetSelectedAsset/'
getMsOfflineAssets = 'http://localhost:28241/GetOfflineAssets/'
getMsDownloadedAssets = 'http://localhost:28241/GetDownloadedAssets/'
getMsCommands = 'http://localhost:28241/GetCommands/'
getMsLog = 'http://localhost:28241/log/'
getMsError = 'http://localhost:28241/error/'

# send command to bridge and print response.
# The commend out commands below are ones that do not work currently.
# I have submitted a request for assistance from Quixel.

response = urllib2.urlopen(getMsFolders)
msFolders = response.read()
print(msFolders)
response.close()

response = urllib2.urlopen(getMsCommands)
msCommands = response.read()
print(msCommands)
response.close()

# response = urllib2.urlopen(getMsSelectedAsset)
# msSelectedAsset = response.read()
# print(msSelectedAsset)
# response.close()

response = urllib2.urlopen(getMsLog)
msLog = response.read()
print(msLog)
response.close()

response = urllib2.urlopen(getMsError)
msError = response.read()
print(msError)
response.close()

# response = urllib2.urlopen(getMsCustomAssets)
# msCustomAssets = response.read()
# print(msCustomAssets)
# response.close()
#
# response = urllib2.urlopen(getMsOfflineAssets)
# msOfflineAssets = response.read()
# print(msOfflineAssets)
# response.close()
#
# response = urllib2.urlopen(getMsDownloadedAssets)
# msDownloadedAssets = response.read()
# print(msDownloadedAssets)
# response.close()

