# Benzinpreis
Fetch Data from TCS.ch Benzin


To get the Id's form a Station

Open https://benzin.tcs.ch/de/map/SP95
F12 → Network → Fetch/XHR
Type "Dornach" in the search field
Look for the XHR request that returns station data
Right-click it → Copy as cURL

as an example:


curl 'https://europe-west6-tcs-digitalbackend.cloudfunctions.net/benzinGetStationById' \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:159.0) Gecko/20100101 Firefox/159.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Content-Type: application/json' \
  -H 'Referer: https://benzin.tcs.ch/' \
  -H 'Origin: https://benzin.tcs.ch' \
  -H 'Sec-GPC: 1' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Connection: keep-alive' \
  -H 'Priority: u=0' \
  -H 'TE: trailers' \
  --data-raw '{"id":"HFCfbbLXs2LFa9TPTJlT"}'


  
Currently there are 4 stations incoporated
