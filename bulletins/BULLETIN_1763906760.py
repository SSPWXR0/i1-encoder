# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('AKZ701')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR AKZ701")
areaList = wxdata.getBulletinInterestList('AKZ701')
group = """"""
txt = """* WHAT...Visibility one quarter mile or less in dense fog.  * WHERE...Anchorage.  * WHEN...Until 1 PM AKST this afternoon.  * IMPACTS...Hazardous driving conditions due to low visibility."""

for area in areaList:
  b = twc.Data()
  b.pil = 'FGY'
  b.pilExt = '001'
  b.issueTime = 1763906760
  b.dispExpiration = 1763935200
  b.group = group
  b.text = txt
  exp = 1763935200
  wxdata.setBulletin(area, b, exp)
