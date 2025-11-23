# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PZZ670')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PZZ670")
areaList = wxdata.getBulletinInterestList('PZZ670')
group = """"""
txt = """* WHAT...Hazardous sea conditions.  * WHERE...Point Piedras Blancas to Point Sal from 10 to 60 NM.  * WHEN...Until 3 PM PST Monday.  * IMPACTS...Conditions will be hazardous to small craft.  * ADDITIONAL DETAILS...See the Coastal Waters Forecast (CWFLOX) for more."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763886780
  b.dispExpiration = 1763935200
  b.group = group
  b.text = txt
  exp = 1763935200
  wxdata.setBulletin(area, b, exp)
