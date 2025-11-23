# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('WVZ514')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR WVZ514")
areaList = wxdata.getBulletinInterestList('WVZ514')
group = """"""
txt = """* WHAT...West winds 15 to 25 mph with gusts up to 50 mph.  * WHERE...Eastern Tucker County.  * WHEN...Until 5 PM EST this afternoon.  * IMPACTS...Gusty winds will blow around unsecured objects. Tree limbs could be blown down and a few power outages may result."""

for area in areaList:
  b = twc.Data()
  b.pil = 'WIY'
  b.pilExt = '001'
  b.issueTime = 1763909040
  b.dispExpiration = 1763935200
  b.group = group
  b.text = txt
  exp = 1763935200
  wxdata.setBulletin(area, b, exp)
