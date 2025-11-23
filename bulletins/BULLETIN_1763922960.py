# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PZZ450')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PZZ450")
areaList = wxdata.getBulletinInterestList('PZZ450')
group = """"""
txt = """* WHAT...Seas 7 to 10 feet.  * WHERE...Pt St George to Cape Mendocino out 10 nm.  * WHEN...Until 3 AM PST Monday.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763922960
  b.dispExpiration = 1763952300
  b.group = group
  b.text = txt
  exp = 1763952300
  wxdata.setBulletin(area, b, exp)
