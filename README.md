# MobSF-ScanAPI

This API will analyze uploaded file with MobSF and return analysis result as JSON

### To-Do

- [x] File upload to API
  - [x] Extract malware path and name variables from request 
- [x] Functions to send request to MobSF
  - [x] Upload file to MobSF
  - [x] Scan file
  - [x] Return JSON response
- [x] Return JSON response to request
- [x] Define static MobSF API key
- [x] Refactor file structure
- [x] Dockerize
  - [x] Build API image
  - [x] Build docker-compose and yml file
    - [ ] ?Set static MobSF API KEY as secret variable

<sub>
PS: 
? - not sure about task
</sub>

### How to setup

You can start by downloading this repo with git command below
```
git clone https://github.com/s-kali/MobSF-ScanAPI.git
```
Move to project directory
```
cd MobSF-ScanAPI
```
Run docker containers using compose (you can add --build tag)
```
docker-compose -f docker-compose.dev.yml up
```

### You can send your file request using command below
```
curl -F 'file=@<filepath>' http://172.18.0.2:5000/file-upload 
```
