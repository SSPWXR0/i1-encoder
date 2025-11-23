# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('COZ018')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR COZ018")
areaList = wxdata.getBulletinInterestList('COZ018')
group = """"""
txt = """* WHAT...Snow above 9000 feet. Additional snow accumulations up to 3-6 inches.  * WHERE...Northwest San Juan Mountains and Southwest San Juan Mountains.  * WHEN...Until midnight MST tonight.  * IMPACTS...Roads, especially mountain passes, will likely be slick and hazardous."""

for area in areaList:
  b = twc.Data()
  b.pil = 'WWY'
  b.pilExt = '001'
  b.issueTime = 1763922240
  b.dispExpiration = 1763967600
  b.group = group
  b.text = txt
  exp = 1763967600
  wxdata.setBulletin(area, b, exp)
