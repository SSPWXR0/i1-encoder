# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('LEZ040')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR LEZ040")
areaList = wxdata.getBulletinInterestList('LEZ040')
group = """"""
txt = """* WHAT...West winds 15 to 25 knots and waves 4 to 7 feet.  * WHERE...The nearshore waters of Lake Erie from Ripley to Buffalo.  * WHEN...Until midnight EST tonight.  * IMPACTS...Winds and/or waves will cause hazardous conditions that could capsize or damage small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763915820
  b.dispExpiration = 1763953200
  b.group = group
  b.text = txt
  exp = 1763953200
  wxdata.setBulletin(area, b, exp)
