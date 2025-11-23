# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('HIZ001')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR HIZ001")
areaList = wxdata.getBulletinInterestList('HIZ001')
group = """"""
txt = """...HIGH SURF ADVISORY REMAINS IN EFFECT UNTIL 6 PM HST THIS EVENING FOR NORTH AND WEST FACING SHORES OF NIIHAU KAUAI OAHU MOLOKAI AND NORTH FACING SHORES OF MAUI...  .A moderate, long-period, northwest (310 to 320 degrees) swell will bring high surf today, gradually declining as the day progresses.  * WHAT...Along north facing shores, surf of 12 to 16 feet this morning, lowering to 10 to 15 feet by this afternoon. Along west facing shores, surf of 9 to 13 feet this morning, lowering to 8 to 12 feet by this afternoon.  * WHERE...North and west facing shores of Niihau, Kauai, Oahu, Molokai, and north facing shores of Maui.  * WHEN...Until 6 PM HST this evening.  * IMPACTS...Moderate. Strong breaking waves and strong currents will make swimming dangerous."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SUY'
  b.pilExt = '001'
  b.issueTime = 1763905080
  b.dispExpiration = 1763952300
  b.group = group
  b.text = txt
  exp = 1763952300
  wxdata.setBulletin(area, b, exp)
