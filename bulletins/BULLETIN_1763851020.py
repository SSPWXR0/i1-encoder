# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('AKZ833')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR AKZ833")
areaList = wxdata.getBulletinInterestList('AKZ833')
group = """"""
txt = """* WHAT...Heavy snow. Additional snow accumulations up to 5 inches.  * WHERE...White Mountains and High Terrain South of the Yukon River and Yukon Flats.  * WHEN...Until noon AKST Sunday.  * IMPACTS...Travel could be very difficult.  * ADDITIONAL DETAILS...3 to 5 inches of additional snow are possible throughout the White Mountains Recreation Area with the heaviest amounts north and east of Eagle Summit."""

for area in areaList:
  b = twc.Data()
  b.pil = 'WSW'
  b.pilExt = '001'
  b.issueTime = 1763851020
  b.dispExpiration = 1763931600
  b.group = group
  b.text = txt
  exp = 1763931600
  wxdata.setBulletin(area, b, exp)
