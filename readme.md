# Background
Hi
I received a text message from +61 406 456 469 which surprisingly had no typos (not that I'm much of a judge), telling me that $750 had been moved rejected and to log in and change my password or whatever.

![Original Text](Assets/IMG_2639(Small).jpeg)

Going to the website, they clearly wanted to make people believe that they were on the ANZ website
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

Looking at my ANZ CRN it's a 9 digit number, so using random to generate a number between 100000000 - 999999999.

## run spam.py
See the spam.py file.

My plan is to spam them every 4 seconds, I thought I would just let it run through the passwords for a few days and hopefully they don't do any kind of detailed analysis on the timing to figure out which posts are mine, and which posts are from their real victims.

I should mention that I start a new requests session & grab a cookie every time I go to their home page, I just thought I would make it slightly harder on them by using new cookies for every request, so hopefully it's just a bit harder to decipher which requests are mine and which are real. I fully recognise that they might just be able to do something with my IP address, but I wasn't willing to put in the time to figure that out.

I've seen lots of people on YouTube just spam them with thousands of requests in parallel, which might also be ok, but they might just ignore the results over the hour that until I ran out of passwords, and go back to it. I thought maybe by spamming in smaller chunks I might mess them up for longer?

I don't know, happy to have feedback from someone who knows what they're actually doing :)

# Results

It feel a bit unbelievable, but after a couple of hours of spamming them with fake data I started getting 404 errors

![My errors](Assets/ClosedDown(Small).png)

My gut feel was that they probably just blocked my IP address, but [isup.me](http://isup.me) also showed that they were down.

![it's gone](Assets/isup.me(Small).png)

So I guess that's a win?

# Lessons Learnt
After this has all finished I've had a bit of a look at rotating proxies in python 3, [Scrapehero](https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/) has a tutorial about how to do it, and [Proxy Requests](https://github.com/rootVIII/proxy_requests) looks easy enough.  

Otherwise it was a relatively small project which I didn't want to sink too much time in to, I'm happy that I (maybe?) made a difference, and it wasn't that complex to do.
