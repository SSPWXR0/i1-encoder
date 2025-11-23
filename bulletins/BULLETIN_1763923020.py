# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('CAZ101')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR CAZ101")
areaList = wxdata.getBulletinInterestList('CAZ101')
group = """"""
txt = """* WHAT...Increased threat of sneaker waves expected.  * WHERE...Coastal Del Norte, Northern Humboldt Coast, Southwestern Humboldt and Mendocino Coast Counties.  * WHEN...Until 10 PM PST this evening. .  * IMPACTS...Large, unexpected waves can sweep across the beach without warning, sweeping people into the sea from rocks, jetties, and beaches. These sneaker waves can also move large objects such as logs, crushing anyone caught underneath."""

for area in areaList:
  b = twc.Data()
  b.pil = 'BHS'
  b.pilExt = '001'
  b.issueTime = 1763923020
  b.dispExpiration = 1763956800
  b.group = group
  b.text = txt
  exp = 1763956800
  wxdata.setBulletin(area, b, exp)
