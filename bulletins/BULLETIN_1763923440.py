# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('TXC007')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR TXC007")
areaList = wxdata.getBulletinInterestList('TXC007')
group = """"""
txt = """FFWCRP  The National Weather Service in Corpus Christi has issued a  * Flash Flood Warning for... Southwestern Aransas County in south central Texas... East Central San Patricio County in south central Texas...  * Until 345 PM CST.  * At 1244 PM CST, Doppler radar indicated thunderstorms producing heavy rain across the warned area. Between 2.5 and 3.5 inches of rain have fallen. Additional rainfall amounts of 1 to 2 inches are possible in the warned area. Flash flooding is ongoing or expected to begin shortly.  HAZARD...Flash flooding caused by thunderstorms.  SOURCE...Radar.  IMPACT...Flash flooding of small creeks and streams, urban areas, highways, streets and underpasses as well as other poor drainage and low-lying areas.  * Some locations that will experience flash flooding include... Rockport, Aransas Pass and Fulton."""

for area in areaList:
  b = twc.Data()
  b.pil = 'FFW'
  b.pilExt = '001'
  b.issueTime = 1763923440
  b.dispExpiration = 1763934300
  b.group = group
  b.text = txt
  exp = 1763934300
  wxdata.setBulletin(area, b, exp)
