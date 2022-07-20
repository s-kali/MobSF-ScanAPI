# MobSF-ScanAPI

This API will analyze uploaded file with MobSF

### To-Do

- [x] File upload
- [x] Python funcs to communicate with MobSF
  - [x] Malware path and name values as script or function parameters 
- [x] API func to send uploaded file to MobSF && send MobSF Json analys as response
- [ ] Refactor API code
- [ ] Dockerize


```
curl -F 'file=@filepath' http://localhost:5000/file-upload 
```
