# Background
Hi
I received a text message from +61 406 456 469 which suprisingly had no typos (not that I'm much of a judge), telling me that $750 had been moved rejected and to log in and change my password or whatever.

![Original Text](Assets/IMG_2639(Small).jpeg)

Going to the website, they clearly wanted to make people believe that they were on teh ANZ website
> https://review-pending-transaction.com/login.php

![Their Website](Assets/TheirWebsite(Small).png)

# The plan
Just spam them with fake data.

## Step 1. Getting the post page
For some reason the website didn't work on my desktop, I had to change it to use 400 x 1003 resolution (mobile view) before it would let me access it.

Using the network monitor in my web browser going to their home page sends this:

```
URL: https://review-pending-transaction.com/login.php
```

```
Request Headers:
:authority: review-pending-transaction.com
:method: GET
:path: /login.php
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
dnt: 1
referer: https://keep.google.com/
sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: cross-site
sec-fetch-user: ?1
sec-gpc: 1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
```

## Step 2. Post fake details, get the header / data format.
By clicking through and sending some fake data, it looks like the actual post command goes here:
```
https://review-pending-transaction.com/core/actions.php?action=send_data
```
These are my headers
```
:authority: review-pending-transaction.com
:method: POST
:path: /core/actions.php?action=send_data
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
content-length: 56
content-type: application/x-www-form-urlencoded; charset=UTF-8
cookie: PHPSESSID=kp7fh8ga3t94pe16nacb8e74id
dnt: 1
origin: https://review-pending-transaction.com
referer: https://review-pending-transaction.com/login.php
sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?1
sec-ch-ua-platform: "Android"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
sec-gpc: 1
user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
x-requested-with: XMLHttpRequest
```

And this is my initial fake data:
```
currentpage: 	login
username: 		45678924
password: 		ajdkfhurtlm
```

## Getting believable junk details
Using the top passwords from here:
> https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt

Looking at my anz CRN it's a 9 digit number, so using random to generate a number between 100000000 - 999999999.

## run spam.py
See the spam.py file.

My plan is to spam them every 4 seconds, just so it's somewhat believable ?

I've seen lots of people just spam them with thousands of requests in parallel, which might also be ok, but they might just delete a small batch of data over the time period.

# Results

It feel a bit unbelievable, but after a couple of hours of spamming them with fake data I started getting 404 errors

![My errors](Assets/ClosedDown(Small).png)

My gut feel was that they probably just blocked my IP address, but [isup.me](http://isup.me) also showed that they were down.

![it's gone](Assets/isup.me(Small).png)

So I guess that's a win?
