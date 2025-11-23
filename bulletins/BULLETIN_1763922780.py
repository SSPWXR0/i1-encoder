# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('TXZ091')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR TXZ091")
areaList = wxdata.getBulletinInterestList('TXZ091')
group = """"""
txt = """* WHAT...Flooding caused by excessive rainfall continues to be possible.  * WHERE...Portions of north central and northeast Texas, including the following counties, in north central Texas, Collin, Cooke, Dallas, Denton, Eastland, Fannin, Grayson, Hunt, Jack, Montague, Palo Pinto, Parker, Rockwall, Stephens, Tarrant, Wise and Young. In northeast Texas, Delta, Hopkins, Lamar and Rains.  * WHEN...From 6 PM CST this evening through Monday afternoon.  * IMPACTS...Excessive runoff may result in flooding of rivers, creeks, streams, and other low-lying and flood-prone locations. Flooding may occur in poor-drainage and urban areas.  * ADDITIONAL DETAILS... - Rainfall totals of 1 to 3 inches, with isolated higher amounts up to 4 inches."""

for area in areaList:
  b = twc.Data()
  b.pil = 'FAA'
  b.pilExt = '001'
  b.issueTime = 1763922780
  b.dispExpiration = 1763967600
  b.group = group
  b.text = txt
  exp = 1763967600
  wxdata.setBulletin(area, b, exp)
