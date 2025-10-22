# Requirements
* **Docker**   
This is as simple as going to: https://www.docker.com/get-started, downloading it, and running the installer for your system.

# Let's do it!
## Step 1: download & execute
When Docker is running on your system, you only have to execute one more step to start this Quickstart:
```
docker run -d -p 80:80 --rm --name tomp-oi edwinvandenbelt/tomp-oi
```
If you already have a webserver running on your machine, you have to use another port, f.x. 81 or 8080. Replace the first '80' in the line with an available port number, and off you go!  

## Step 2: start exploring
Open your browser at [http://localhost/ui/](http://localhost/ui/) and the Operator Information part of the TOMP-API is running on your machine, with a simple implementation behind it.  

For instance, let's have a look at the generic information of this Transport Operator:  
- open the section 'GET /operator/information'
![GET Operator information](https://raw.githubusercontent.com/TOMP-WG/website/master/wiki/images/qs-oi-1.png)
- click on 'Try it out' (it chances to 'Cancel')
- navigate a bit down to 'Execute', click on it.
![GET Operator information](https://raw.githubusercontent.com/TOMP-WG/website/master/wiki/images/qs-oi-2.png)
- you have executed the first call to the example implementation on your machine! Congrats!
- a bit below the 'Execute' button, you'll find the 'Response body', where the reply can be found of the request for Operator Information.

You can do this for each of the endpoints. The most important endpoint is the operator/meta, where you can amongst others find the implemented endpoints, thereby describing the interface. So if you don't want to implement the operator/stations (because you do have a free-floating solution), remove this endpoint in your implementation or return 'STATUS': "NOT_IMPLEMENTED".

## Step 3: start playing
Ok, now you know how it works. Now the fun part starts! Let's tune the results to your needs!  
- we have to stop the running web server:
```
docker stop tomp-oi
```
- we have to create a folder on your machine with some files, to overwrite the existing output: f.x. c:\temp\tomp-oi\  
- in this folder, we can create a file called alerts.json (the name of the file should match the endpoint part after '/operator/', but replace the dashes with underscores (e.g. available_assets.json).
- open 'alerts.json' and past this into it:
```
[
    {
      "alertId": "791ab120-0297-445d-b391-435bba0f352d",
      "alertType": "OTHER",
      "description": "This is a slightly different alert",
      "lastUpdated": "2021-12-03T04:56:07+00:00",
      "startAndEndTimes": [
        [
          "2021-12-03T04:56:07+00:00",
          "2021-12-03T05:56:07+00:00"
        ]
      ],
      "summary": "quickstart alert",
      "url": "https://www.default-to.com/alerts/791ab120-0297-445d-b391-435bba0f352d"
    }
  ]
```
Don't be afraid to break anything (like creating invalid JSON), the quick start will return directly the content of this file.
- start the quick start again, executing a slightly different command:
```
docker run -d -p 80:80 --rm --name tomp-oi -v c:/temp/tomp-oi:/usr/src/app/external edwinvandenbelt/tomp-oi
``` 
- execute the alert endpoint, and you'll see that the output will be yours! This exercise you can perform with each of the endpoints. 

That's about it!