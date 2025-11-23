# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('AKZ319')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR AKZ319")
areaList = wxdata.getBulletinInterestList('AKZ319')
group = """"""
txt = """...ACCUMULATING SNOW FOR HAINES MONDAY...  .A weak, decaying low pressure will bring moisture up from the south, generating snow showers for Haines, Lutak, and Mud Bay beginning early Monday morning. Highest uncertainty regarding this system is the depth of the moisture profile, which will dictate heavier rates. Current guidance indicate about a 50% chance to exceed 0.5 inch rates and could be as high as one inch per hour. Current advisory represents most likely snow amounts during this period, but updates may be necessary as the event draws near.  * WHAT...Snow expected. Total snow accumulations of 4 to 6 inches.  * WHERE...Haines, Lutak, and Mud Bay.  * WHEN...From 3 AM to 6 PM AKST Monday.  * IMPACTS...Travel could be difficult.  * ADDITIONAL DETAILS...Heaviest snow rates are expected Monday morning, with rates possibly exceeding 0.5 inches per hour."""

for area in areaList:
  b = twc.Data()
  b.pil = 'WWY'
  b.pilExt = '001'
  b.issueTime = 1763921400
  b.dispExpiration = 1763950500
  b.group = group
  b.text = txt
  exp = 1763950500
  wxdata.setBulletin(area, b, exp)
