# MobSF-ScanAPI

This API will analyze uploaded file with MobSF and return analysis result as JSON

### To-Do

- [x] File upload
- [x] Python funcs to communicate with MobSF
  - [x] Malware path and name values as script or function parameters 
- [x] API func to send uploaded file to MobSF && send MobSF Json analys as response
- [x] Refactor file structure
- [ ] Refactor API code
- [ ] Create Upload folder
- [x] Dockerize
  - [x] Define static MobSF API key
  - [x] Build API image
  - [x] ?Build network for multi container structure
  - [ ] Build docker-compose and yml file
    - [ ] Set static MobSF API KEY as secret variable
    - [ ] ?Change static network values in yml file (default values causes duplicate network issue)

<sub>
PS: ? - not sure about task
</sub>

## You can send your file request using command below
```
curl -F 'file=@<filepath>' http://172.18.0.2:5000/file-upload 
```
