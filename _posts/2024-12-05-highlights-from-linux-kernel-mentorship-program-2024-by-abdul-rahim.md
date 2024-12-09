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
that is widely used in modern computing. All of the
top 500 supercomputers in the world are running Linux[^1]. More than
two-thirds of mobile phones in the world are running Linux[^2]. More than
95% of servers in the world use Linux[^3]. I’ll stop there, because this
blog is not about Linux. It’s about how I started contributing to the
Linux Kernel and how you can too.

## How Kernel Development Works

Development in the Kernel happens on the Linux Kernel Mailing List
(LKML). Linux is an open-source kernel, and anyone can contribute to it.
You just have to send your patches (which are nothing but `git diff`
rebranded as an email). Then, if your contribution is useful/required,
some experienced developers will ask questions about what you are trying
to do and why. You need to be there explaining what you are doing. Don’t
explain the code; the code explains itself. Explain why the change is
needed. People on LKML are really nice; they will guide you on what you
are doing wrong and how your code can be improved.

Prerequisites for kernel development, such as how to generate patches,
how to send them to LKML, how to compile and boot the kernel, etc., will
be taught through a course called LFD 103. You don’t need extensive
experience in kernel development; however, I would have some
survivorship bias here. Kernel development can get as complicated as you
want, and it is by no means a walk in the park. I spent a whole month
trying to understand what people were talking about on LKML and
configuring my mail client. Once you conquer these small impediments,
everything else becomes easy. You can use [_my
notes_](https://github.com/abdulrahim2002/ldf103_notes)  to help
yourself should you need them.

## My Background

Kernel developers have always been like an _enigma_ for me, they always
seemed to be doing something really cool and they seemed so smart. I
once watched [_this video_](https://www.youtube.com/watch?v=KSs0v2Fmnhc)
of a guy doing kernel and it got me interested in the kernel. Also, in
my second semester, I got hold of a book called The C Programming
Language.  This book made me fall in love with C programming. The kind
of control that C provides is really cool. Unfortunately, it is this
power that, when not used with great responsibility, opens up a lot of
bugs.

I am actually not a long-time Linux user. In fact, I was introduced to
it just this year. The moment I got hold of it, everything just came
together. I previously used Windows, and I was so confounded about so
many things. See, Windows has this habit of hiding away everything from
the user and making features that work, so the user is left alone to
troubleshoot a system that even Microsoft does not understand. So, I
wasted a lot of time on Windows.

While I worked on the Kernel, I read a book called Linux Device Drivers.
It is written by seasoned kernel developers, and it improved my
understanding of the kernel a lot. I would highly recommend it to anyone
who is trying to write drivers or just improve their understanding of
the kernel.

What to Contribute The biggest challenge to starting to contribute to
the Linux Kernel is deciding which subsystem you would be working on.
The kernel is huge, and you can work on anything, from cutting-edge GPUs
to network drivers.

Most of the code in the Kernel resides in drivers. Since a kernel’s main
job is to communicate with the hardware and provide control at upper
levels to the OS and the user, a great deal of development pertains to
driver development. And since there are so many new devices that come
out, this area is quite busy.

But for driver development, you would need the device/hardware and
knowledge in electronics. I would recommend that if you have an
electronics background and hardware, you write the driver for it.

However, this was not the case with me, so I focused on kselftest and
core subsystems. There is also something called syzbot, which is a
kernel fuzzer. What that means is that it keeps putting random data into
the kernel until it thinks it found a bug. You can also look at syzbot
bug reports; they are a great resource to learn. You would get to know
what the common mistakes that kernel developers make are.

Your next option is to upgrade [_deprecated
APIs_](https://docs.kernel.org/process/deprecated.html). Some of these
APIs are insecure and still being used in many parts of the kernel.
Developers really appreciate it when you upgrade their code. However, it
is often not as simple as search and replace—you might need to develop a
deeper understanding of that particular codebase. But by and large, I
would consider it as low-hanging fruit and one that is useful, more
useful than fixing spellings.

Which brings us to our next option: fixing spellings. This is the
easiest type of contribution, and I would recommend that you start with
fixing spellings. This is because it gives you a kickstart and is very
simple. The biggest benefit of fixing grammar issues is that it makes
you read the code/documentation. Nonetheless, you can even skip that
with a tool called codespell. Just run spellcheck drivers/, and it will
list all the spelling mistakes it found in the drivers directory.

I started with a simple patch, which was about fixing a spelling
mistake. I would highly recommend starting with simple patches first,
since they help you learn how things move in the kernel. In my first
patch, for example, I made the mistake of introducing two changes, while
my changelog described only one.

There are many ways to contribute to the Linux kernel. In fact, once you
get started, you will keep seeing issues after issues, and it will
become a routine. For a start, I would recommend reading the discussions
on LKML. They are very insightful.

## Conclusion 

While kernel development may seem daunting at first, trust
me, it’s really not. And what’s more, once you start, you become a much
better developer, and you will develop a very good insight into the
workings of computers—not just the kernel, but also in userspace and in
general. You will develop skills in Git, which is crucial if you want to
survive as a developer. In conclusion, I would totally recommend kernel
development. The kind of learning you will get here, you cannot get
anywhere, even in the best of companies.

Good luck!



## References

[^1]: [top500.org](https://www.stackscale.com/blog/most-powerful-supercomputers-linux/)
[^2]: [statcounter.com](https://gs.statcounter.com/os-market-share/mobile/worldwide)
[^3]: [zdnet.com](https://www.zdnet.com/article/linux-has-over-3-of-the-desktop-market-its-more-complicated-than-that/)
