# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('WVZ523')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR WVZ523")
areaList = wxdata.getBulletinInterestList('WVZ523')
group = """"""
txt = """Wind gusts of 35 to 45 mph are possible this afternoon along the mountain ridges and eastern slopes. Gusts of this magnitude are capable of blowing around lightweight objects, causing localized minor tree damage and power outages, and creating difficult driving conditions for high profile vehicles."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SPS'
  b.pilExt = '001'
  b.issueTime = 1763920800
  b.dispExpiration = 1763935200
  b.group = group
  b.text = txt
  exp = 1763935200
  wxdata.setBulletin(area, b, exp)
