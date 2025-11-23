# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('MDZ501')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR MDZ501")
areaList = wxdata.getBulletinInterestList('MDZ501')
group = """"""
txt = """Wind gusts reaching 40 to 45 mph are possible through this afternoon. The strongest gusts, potentially reaching 50 mph along the ridges, will generally be brief at any given location. Even so, gusts of this magnitude are capable of blowing around lightweight objects, causing localized minor tree damage and power outages, and creating difficult driving conditions for high profile vehicles."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SPS'
  b.pilExt = '001'
  b.issueTime = 1763908920
  b.dispExpiration = 1763931600
  b.group = group
  b.text = txt
  exp = 1763931600
  wxdata.setBulletin(area, b, exp)
