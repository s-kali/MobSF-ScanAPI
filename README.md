# MobSF-ScanAPI

This API will analyze uploaded file with MobSF and return analysis result as JSON

### To-Do

- [x] File upload
- [x] Python funcs to communicate with MobSF
  - [x] Malware path and name values as script or function parameters 
- [x] API func to send uploaded file to MobSF && send MobSF Json analys as response
- [ ] Refactor API code
- [ ] Dockerize
  - [ ] ?Define static MobSF API key as secret
  - [ ] Build API image
  - [ ] ?Build network for multi container structure
  - [ ] Build docker-compose and yml file

<sub>
PS: ? - not sure about task
</sub>
## You can send your file request using command below
```
curl -F 'file=@<filepath>' http://localhost:5000/file-upload 
```
