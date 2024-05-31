# README

## Apply the API key

[NESC (nier.go.kr)](https://nesc.nier.go.kr/en/html/svc/openapi/insert.do)

Sign in the website before to get an open-API key. You will need to wait about two days to get it in your email.



## Run the script

Change the `APIKEY` parameter to the key you get from above. And the time period is defined by the `begin` and `end` parameters.

Then just run the script.



## Notice

The bash scripts that the NIER website gives can't do the right job. The url that we get need to use `https` instead of `http`, and it should add the port number. 

I discover this on the website: [createURL](https://nesc.nier.go.kr/en/html/svc/openapi/createURL.do) 

You can refer to this to write other scripts.