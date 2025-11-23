# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('LMZ541')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR LMZ541")
areaList = wxdata.getBulletinInterestList('LMZ541')
group = """"""
txt = """* WHAT...Southwest winds 10 to 20 kt with gusts up to 25 kt. Waves 2 to 4 ft expected with locally higher waves up to 5 ft near Deaths Door.  * WHERE...Lake Michigan nearshore waters from Washington Island to Sheboygan.  * WHEN...From 6 AM to 10 PM CST Monday.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763917680
  b.dispExpiration = 1763946900
  b.group = group
  b.text = txt
  exp = 1763946900
  wxdata.setBulletin(area, b, exp)
