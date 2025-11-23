# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PZZ571')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PZZ571")
areaList = wxdata.getBulletinInterestList('PZZ571')
group = """"""
txt = """* WHAT...Northwest winds 10 to 20 kt and seas 8 to 11 ft.  * WHERE...Waters from Point Reyes to Pigeon Point 10-60 NM.  * WHEN...Until 9 PM PST this evening.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763915700
  b.dispExpiration = 1763945100
  b.group = group
  b.text = txt
  exp = 1763945100
  wxdata.setBulletin(area, b, exp)
