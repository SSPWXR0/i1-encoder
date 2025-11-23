# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PZZ130')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PZZ130")
areaList = wxdata.getBulletinInterestList('PZZ130')
group = """"""
txt = """* WHAT...Seas 7 to 10 ft.  * WHERE...West Entrance U. S. Waters Strait Of Juan De Fuca.  * WHEN...Until 10 PM PST this evening.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763914080
  b.dispExpiration = 1763943300
  b.group = group
  b.text = txt
  exp = 1763943300
  wxdata.setBulletin(area, b, exp)
