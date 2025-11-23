# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PZZ350')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PZZ350")
areaList = wxdata.getBulletinInterestList('PZZ350')
group = """"""
txt = """* WHAT...Steep seas 10 to 15 ft at 15 to 17 seconds expected.  * WHERE...All areas.  * WHEN...Until 10 AM PST Monday.  * IMPACTS...Steep seas could capsize or damage smaller vessels.  * View the hazard area in detail at https://go.usa.gov/x6hks"""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763892780
  b.dispExpiration = 1763939700
  b.group = group
  b.text = txt
  exp = 1763939700
  wxdata.setBulletin(area, b, exp)
