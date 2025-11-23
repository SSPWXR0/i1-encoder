# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('ANZ650')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR ANZ650")
areaList = wxdata.getBulletinInterestList('ANZ650')
group = """"""
txt = """* WHAT...North to northwest winds 20 to 25 kt with gusts up to 30 kt and seas 3 to 5 ft expected.  * WHERE...Coastal waters from Fenwick Island DE to Chincoteague VA out 20 nm and Coastal waters from Chincoteague to Parramore Island VA out 20 nm.  * WHEN...From 7 PM this evening to 10 AM EST Monday.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763909760
  b.dispExpiration = 1763938800
  b.group = group
  b.text = txt
  exp = 1763938800
  wxdata.setBulletin(area, b, exp)
