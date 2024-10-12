---
date: 2024-02-20T01:04:38.000Z
layout: post
title: "How to turn your old smartphone into a home server"
subtitle: Have an extra phone lying around? Use it as a remote server. SSH into it, access its terminal. Transfer files using scp. And much more...
description: Have an extra phone lying around? Use it as a remote server. SSH into it, access its terminal. Transfer files using scp. And much more...
image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1720556907/termux_bugka5.png

# image should be 760, 399 and optimised should be 380, 200
# ![placeholder](http://link//to//image "description text")
optimized_image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_399/v1720556907/termux_bugka5.png
category: dev
tags:
  - ssh
  - server
author: abdulrahim
---

## Introduction

I had an unused phone lying around for some time, and I began
contemplating how I could repurpose it. This led me to reflect on the
impressive performance of modern smartphones and consider whether they
could be utilized as servers.

Smartphones are equipped with ARM-based processors and run on Android,
which is itself built on the Linux kernel. ARM processors are renowned
for their energy efficiency[^efficiency] and have recently found
applications in the server space[^armserver]. 

As someone who enjoys exploring the full potential of devices, I
embarked on a journey to discover how I could leverage the full
potential of smartphones.

<!--
So, I had a phone lying around for quite a while, and I was thinking how
could I make use of it. It was a Oneplus 5 pro, and what fascinates me
is that it has Qualcomm® Snapdragon™ 855, with 12 GB RAM and 256 GB
storage. Yes, it has more ram than my computer. Then i began to think,
given the performance of phones nowadays, why cant we use phones as
servers, which led me into a refreshing journey of phones. Phones have
ARM based processors and they use Android, which is based on linux
kernel. ARM processors are known for their power efficiency[^efficiency]
and recently they have made their way into server space[^armserver].
Apple is also pushing for ARM based computers with its m1 chip. So,
naturally as a person who enjoyes exploiting devices to their full
potential, I began to explore ways in which I could use the phone for
programming and development purposes.
-->

## Setup

Although, you would like to run your programs on phones, but programming on phones typing on screen is a horrifying idea. Fortunately, you dont have to type on your phone, what you can do is you can access its terminal, using protocols like ssh/telnet etc.

So, firstly you would need a terminal to control a machine remotely. Unfortunately, there are not, alot of choices available in phone space when it comes to terminal emulators. Termux is one of the few available options. 

After you manage to open a terminal remotely, then from there its pretty frictionless. You can install the software of your choice and write, compile and run your programs. You might also find it helpful to root your phone for root privilages, which will help you run all commands. But please beware that rooting can null your warrenty, check with local expert. If termux does'nt work for you then there are also other options like [kali net hunter](https://www.mobile-hacker.com/2023/07/18/how-to-install-kali-nethunter-on-rooted-oneplus-7-pro/).

So, in total, we need to install termux, then we would setup ssh.

## Termux

Termux is an open source terminal emulator for android. In essence, it provides you with a linux environment, within android, The only difference between actual linux environment and termex is that it is not FHS(File System Hierarcy) compliant, i.e. it does not strictly follow linux file system conventions. The consequences of that are that `#! /usr/bin/sh` may not work, so you have to watch out the paths. Other than that, it supports almost all commands on linux. 

Moreover, It is an app that does'nt interfere with your system so you can run your android as normal, moreover it runs without root privilages. It comes with a large repository of software found at [packages.termux.dev](https://packages.termux.dev/).

## Below are the steps to setup ssh in termux

### Step 1:

Download texmux on [_playstore_](https://play.google.com/store/apps/details?id=com.termux&hl=en_US&gl=US&pli=1), [_f-droid_](https://f-droid.org/en/packages/com.termux/) or from [_github releases_](https://github.com/termux/termux-app#github)

### Step 2:

Update using pkg:

```bash
pkg update  # update the repositories
pkg upgrade # upgrade all to latest versions
```

![run these commands on phone](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,h_780/v1720609372/update_upgrade_ncnwx1.jpg)
*Run this commands*

### Step 3: Install ssh

```bash
pkg install ssh
```
![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,h_780/v1720609372/ssh_flhmpc.jpg)
*install ssh*

### Step 4: Set a password

Setup a password that you will use to login

```bash
passwd
```

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_500/v1720610775/Screenshot_from_2024-07-10_16-55-56_wy3veq.png)
*set password and note username*

### Step 5: Note your username

You will require username and ip address when logging in using ssh, hence note them. Run the command `whoami` the know your username. This will generally start with "a0_"

```
whoami
```

### Step 6: Note your IP address

You can check your IP address in:

```
settings > Wi-Fi > click on the (i) button, on the 
                   wifi you are connected to and 
                   Look for IPv4 address 
```

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

## Aftermath

You can use [scp](https://linux.die.net/man/1/scp) command to transfer files between your computer and phone. In case you want to do development, there are a number of [programming packages](https://wiki.termux.com/wiki/Development_Environments) available in termux, you can find rust, nodejs, python, C/C++ and tools for many other programming languages.

## Conclusion

So, now you have successfully installed ssh in your android phone. You might find it useful to install vim, git, gcc etc. There is a large [repository](https://termux.holehan.org/) of packages in termux, which covers pretty much everything your would need.

## Further Reads

[^armserver]: [arm\_server](https://www.stackscale.com/blog/arm-a-revolution-for-dedicated-servers-and-the-cloud/)

[^efficiency]: Simili, Emanuele, et al. "Power Efficiency in HEP (x86 vs. arm)." Power (W) 350.400 (2023): 450
