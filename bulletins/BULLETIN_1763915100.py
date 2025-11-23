# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('GUZ001')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR GUZ001")
areaList = wxdata.getBulletinInterestList('GUZ001')
group = """"""
txt = """* WHAT...Dangerous rip currents.  * WHERE...East facing reefs of the Marianas.  * WHEN...Through late Wednesday night.  * IMPACTS...Rip currents can sweep even the best swimmers away from shore into deeper water.  * ADDITIONAL DETAILS...Elevated easterly trade swell is expected to persist through midweek, maintaining a high risk of rip currents along east facing reefs of the Marianas through Wednesday night. Swell and associated surf is expected to diminish through the second half of the week, which may allow the high rip current risk to fall to moderate as early as Thursday."""

for area in areaList:
  b = twc.Data()
  b.pil = 'RPS'
  b.pilExt = '001'
  b.issueTime = 1763915100
  b.dispExpiration = 1763971200
  b.group = group
  b.text = txt
  exp = 1763971200
  wxdata.setBulletin(area, b, exp)
