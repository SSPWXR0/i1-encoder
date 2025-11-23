# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('NMZ210')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR NMZ210")
areaList = wxdata.getBulletinInterestList('NMZ210')
group = """"""
txt = """* WHAT...Snow. Additional snow accumulations up to two inches.  * WHERE...Northern and Southern Sangre de Cristo Mountains, Tusas Mountains Including Chama, and Jemez Mountains.  * WHEN...Until midnight MST tonight.  * IMPACTS...Plan on snow packed or icy road conditions."""

for area in areaList:
  b = twc.Data()
  b.pil = 'WWY'
  b.pilExt = '001'
  b.issueTime = 1763925120
  b.dispExpiration = 1763967600
  b.group = group
  b.text = txt
  exp = 1763967600
  wxdata.setBulletin(area, b, exp)
