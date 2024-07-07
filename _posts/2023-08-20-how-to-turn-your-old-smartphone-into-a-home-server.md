---
date: 2023-08-20T01:04:38.000Z
layout: post
title: "How to turn your old smartphone into a home server"
subtitle: Have an extra phone lying around? Use it as a remote server. SSH into it, access its terminal. Transfer files using scp. And much more...
description: Have an extra phone lying around? Use it as a remote server. SSH into it, access its terminal. Transfer files using scp. And much more...
image: https://upload.wikimedia.org/wikipedia/commons/6/69/Wikimedia_Foundation_Servers-8055_35.jpg

# image should be 760, 399 and optimised should be 380, 200
# ![placeholder](http://link//to//image "description text")
optimized_image: https://res.cloudinary.com/dz48emek2/image/upload/v1689964438/samples/food/spices.jpg
category: dev
tags:
  - ssh
  - server
author: abdulrahim
---

## Introduction

So, I had a phone lying around for quite, and I was thinking how could I make use of it. It was a Oneplus 5 pro, and what fascinates me is that it has Qualcomm® Snapdragon™ 855, with 12 GB RAM and 256 GB storage. Then i began to think, given that phones nowadays are doing so well in all areas like gaming, why cant we use phones as servers, which led me into a refreshing journey of phones. Phones have ARM based processors and they use Android, which is based of linux kernel. ARM processors are known for their efficiency and recently they have made their way into server space. Apple is also pushing for ARM based computers with its m1 chip. As a person who enjoyes exploiting devices to their full potential, I began to explore ways in which I could use the phone for programming and development purposes.

## Approach

You would need a terminal to control a machine remotely, there are not alot of choices available in phone space when it comes to terminal emulators. Termux is one of the few available options, which is good. After you manage to open a terminal remotely, then from there its pretty frictionless.

## Termux

Termux is an open source terminal emulator for android. It is an app that does'nt interfere with your system so you can run your android as normal, moreover it runs without root privilages. It comes with a large repository of software found at [packages.termux.dev](https://packages.termux.dev/).

## Below are the steps to setup ssh in termux

### Step 1:

Download texmux on [_playstore_](https://play.google.com/store/apps/details?id=com.termux&hl=en_US&gl=US&pli=1), [_f-droid_](https://f-droid.org/en/packages/com.termux/) or from [_github releases_](https://github.com/termux/termux-app#github)

### Step 2:

Update using pkg:

```bash
pkg update  # update the repositories
pkg upgrade # upgrade all to latest versions
```

### Step 3: Install ssh

```bash
pkg install ssh
```

### Step 4: Set a password

Setup a password that you will use to login

```bash
passwd
```

### Step 5: Note your username

You will require username and ip address when logging in using ssh, hence note them. Run the command `whoami` the know your username. This will generally start with "a0_"

```bash
whoami
```
### Step 6: Note your IP address

You can check your IP address in `settings > Wi-Fi > click on the (i) button, on the wifi you are connected to. Look for IPv4 address 


### Step 7: Run ssh doemon in termux

On your phone, run the ssh daemon using

```bash
sshd
```

### Step 8: Login form your computer

On your computer, use the following command to login into your phone and access its terminal

```bash
ssh <user_name>@<IP_address> -p 8022
```

The username and IP address we already determined in step 5 and 6 resp. Note that it will promt you for password

## Conclusion

So, now you have successfully installed ssh in your android phone. You might find it useful to install vim, git, gccetc. There is a large [repository](https://termux.holehan.org/) of packages in termux, which covers pretty much everything your would need. You might also find it helpful to root your phone for root privilages, which will help you run all commands. But please beware that rooting can null your warrenty, check with local expert. If termux does'nt work for you then there are also other options like [kali net hunder](https://www.mobile-hacker.com/2023/07/18/how-to-install-kali-nethunter-on-rooted-oneplus-7-pro/)

You can use [scp](https://linux.die.net/man/1/scp) command to transfer files between your computer and phone. 

## Setting up a web server

