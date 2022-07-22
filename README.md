# MobSF-ScanAPI

This API will analyze uploaded file with MobSF and return analysis result as JSON

### To-Do

- [x] File upload
- [x] Python funcs to communicate with MobSF
  - [x] Malware path and name values as script or function parameters 
- [x] API func to send uploaded file to MobSF && send MobSF Json analys as response
- [x] Refactor file structure
- [ ] Refactor API code
- [x] Dockerize
  - [ ] ?Define static MobSF API key as secret
  - [x] Build API image
  - [x] ?Build network for multi container structure
  - [x] Build docker-compose and yml file
    - [ ] ?Set MobSF API KEY as secret variable
  - [x] Run & test docker-compose
<sub>
PS: ? - not sure about task
</sub>

## You can send your file request using command below
```
curl -F 'file=@<filepath>' http://172.18.0.2:5000/file-upload 
```
