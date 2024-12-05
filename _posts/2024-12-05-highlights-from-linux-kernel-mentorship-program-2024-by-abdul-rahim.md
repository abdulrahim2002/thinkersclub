---
date: 2024-12-05T18:22:18.000Z
layout: post
title: 'Highlights from Linux Kernel Mentorship Program 2024 by Abdul Rahim'
subtitle: "My journey with Linux Kernel Development"
description: "Linux Kernel Mentorhip Program (LKMP) or Linux Kernel Bug Fix Program provides an opportunity for aspiring kernel developers to get started in kernel development. In this post, I would discuss my experience with it and what I learned in the program"
# image should be 760, 399
# image: https://res.cloudinary.com/dg6zyzzwr/image/upload/v1733412669/out_eappts.svg
image: https://res.cloudinary.com/dg6zyzzwr/image/upload/v1733417580/tux_on_terminal_yqcggj.svg
#image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1733412669/out_eappts.svg
# image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1733411390/lin_v8ghbp.png
# and optimised should be 380, 200
optimized_image: https://res.cloudinary.com/dg6zyzzwr/image/upload/w_380/v1733417580/tux_on_terminal_yqcggj.svg
category: dev
tags:
  - comp science
  - dev
author: abdulrahim
---

## Introduction

Linux is a
[_kernel_](https://en.wikipedia.org/wiki/Kernel_(operating_system))
which is widely used in modern computing. All of the top 500
supercomputers in the world are running Linux[^1]. More than two thirds
of mobile phones in the world are running linux[^2].  More than 95% of
servers in the world use Linux[^3]. I'll stop there, because this blog
is not about Linux. It's about how I started contributing to the Linux
Kernel and how you can to.


## How does Kernel Development Work

Development in the Kernel happens on the Linux Kernel Mailing List
(LKML).  Linux is an open source kernel, and anyone can contribute to
it. You just have to send your patches (which is nothing but `git diff`
rebranded as an email). Then, if your contribution is useful/required,
some experienced developers will ask question on what you are trying to
do and why.  You need to be there explaining what you are doing.  Don't
explain the code, the code explains itself, explain why the change is
needed. People on LKML are really nice, they will guide you on what you
are doing wrong and how your code can be improved.

Prerequisites to the Kernel development like how to generate patches,
how to send them to LKML, how to compile and boot the kernel etc will be
taught through a course called LFD 103. You don't need extensive
experience in kernel development, however I would have some survivorship
bias here.  Kernel development can get as complicated as you want and it
is by no means a walk in the park. I spent a whole month trying to
understanding what people are talking about on LKML, and configuring my
mail client.  Once, you conquer these small impediments, everything else
becomes easy.  You can use [_my
notes_](https://github.com/abdulrahim2002/ldf103_notes) to help yourself
should you need them.

## My background

My friend believed that Linux Kernel developers are the coolest peopel
in the world. I wanted to flaunt to him my skills, so that is how I got
interested in kernel developmeent. Also, in my 2nd semester, I got hold
of a book called "The C programming language". This book made me fell in
love with C programming. The kind of control that C language provides is
really cool. Unfortunately, it is this power that when not used with
great responsibility opens up a lot of bugs.

I am actually not a long time linux user. In fact, I was introduced to
it just this year. The moment I got hold of it, everything just came
together. I previously used Windows, and I was so confounded about so
many things. See, Windows has this habit of hiding away everything from
the user and making features that work, so the user then is left alone
to troubleshoot a system that even microsoft does not understand. So.. I
wasted a lot of time on windows.

While I worked on the Kernel, I read this book called "Linux Device
Drivers". It is written by seasoned kernel developers and it improved my
understanding of the kernel a lot. I would highly recommend it to anyone
who is trying to write drivers or just improve his understanding of the
Kernel.

## What to contribute

The biggest challenge to start contributing to the Linux Kernel is to
come up what subsystem would you be working on. Kernel is huge and you
can work on anything, from cutting edge GPUs to network drivers.

Most of the code in the Kernel resides in drivers. Since, a kernel's
main job is to communicate with the hardware and provide control at
upper levels to OS and the user. Hence, a great deal of development
pertains to driver development. And since, there's so much of new
devices that come out, this are is quite busy.

But for driver development you would need the device/harware. And
knowledge in electronics. I would recommend if you have an electronics
background and a hardware, you write the driver for it.

However, this was not the case with me, so I focused on kselftest and
core subsystems. There is also something called `syzbot` which is a
kernel fuzzer. What that means is that it keeps on putting random data
into the kernel until it thinks it found a bug. You can also look at
syzbot bug reports, they are a great resourse to learn. You would get to
know what are the common mistakes that kernel developers make.

Your next option is that you can upgrade [_depreciated
API's_](https://docs.kernel.org/process/deprecated.html). Some of these
API's is insecure and still being used in a lot of parts of the kernel.
And developers really appreaciate if you upgrade their code. However, it
is many times not as simple as search and replace, you might need to
develop a deeper understanding of that particular code base. But by and
large, I would consider it as a low lying fruit and one that is useful,
more useful than fixing spellings.

Which brings us to our next option, fixing spellings. This is the
easiest type of contribution and I would recommend that you start by
fixing spellings. This is because it gives you a kickstart and is very
simple. The biggest benefit of fixing grammer issues is that it makes
you read the code/documentation. Nontheless, you can even skip that with
a tool called `codespell`. Just run `spellcheck drivers/` and it would
list all of spelling mistakes it found in the drivers directory.

I started with a simple patch, which was about fixing a spelling
mistake. I would highly recommend to start with simple patches first,
since they make you learn how things move in the kernel. In my first
patch for example, I made the mistake of introducting 2 changes while my
changelog described only one. 

There are many ways to contribute to the linux kernel. Infact once you
get started, you will keep seeing issues after issues and it will become
a routine. For a start I would recommend to read the discussions on
LKML. They are very insightfull.

## Conclusion

While kernel development may seem daunting at first, but trust me it's
really not. And what's more, once you start. You become a much better
developer and you will develop a very good indight into working of
computers, Not just kernel but also in the userspace and in general. You
will develop skills in git which is crucial if you want to survive as a
developer. In conclusion, I would totally recommend kernel development.
The kind of learning you will get here, you cannot get anywhere, even in
the best of companies.

Good luck!

## References

[^1]: [top500.org](https://www.stackscale.com/blog/most-powerful-supercomputers-linux/)
[^2]: [statcounter.com](https://gs.statcounter.com/os-market-share/mobile/worldwide)
[^3]: [zdnet.com](https://www.zdnet.com/article/linux-has-over-3-of-the-desktop-market-its-more-complicated-than-that/)
