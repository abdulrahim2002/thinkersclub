---
date: 2024-07-08T17:17:28.000Z
layout: post
title: "(Concept) Memory Access Detection using Merkel Trees"
subtitle: (Concept) Memory Access Detection using Merkel Trees Post
description: A novel approach to detection of unauthorised memory access, which enables one to identify weather a file/memory block was accessed/tampered. We propose a polluted flag in directory structure which enables one to identify exactly what are the files that have been accessed by a malicious actor.
image: https://res.cloudinary.com/dz48emek2/image/upload/c_scale,w_760/v1689964438/samples/food/spices.jpg
# image should be 760, 399 and optimised should be 380, 200

# scaling in url: https://res.cloudinary.com/dm7h7e8xj/image/upload/c_scale,w_800/v1506079212/jekflix-capa_vfhuzh.png
# ![placeholder](http://link//to//image "description text")
optimized_image: https://res.cloudinary.com/dz48emek2/image/upload/c_scale,w_380/v1689964438/samples/food/spices.jpg
category: concept
tags:
    - file system
    - merkel trees
    - security
author: abdulrahim
---

## Introduction

Computer memory is usually implemented as NTFS or FAT32[^1]. While, data on disks is generally considered secure. One with appropriate setup can access individual memory blocks in hardware without any authentication. This is because memory is not protected at hardware level, and authentication is usually implemented in software.

Moreover, if unauthorised access to memory cannot be detected, user of the computer would never know that the system was compromised. Currently, there is no reliable method of detecting weather a file has been accessed. Detecting tampered files is easy, you can hash the contents of the file and when the hash (probably without your knowledge) changes, you might conclude that the file was tampered with. But detecting memory access is a more complicated problem. Although linux does keep track of the last access timestamp, available via that `stat` command. It will only keep track of file accesses that use `read` syscall. A malicious actor may still be able to access memory without detection, directly interfacing with hardware.

In this article, I have described an approach to detect accesses to memory usign merkel trees. The approach advocates for encryption of the underlying memory, and the decryption be done in software. We will use a `polluted` flag to identify the files/blocks that have been accessed without user authentication.


## Merkel Trees

Merkel trees are a tree data structure in which hashes are stored rather than data. Leaf nodes store 

our approach is based on encryption and merkel tree for detection of access in the directory tree.

the approach is easily implementable on a wide veriety of software and hardware, using current approaches.


files would be labeled as polluted if an **illegal access** is detected

The underlying memory would be encrypted, and access would only be allowed through an API.

We will allow an access with invalid credentials, but will flag the file accessed as polluted.

This pollution would show up in the tree. Which makes the tracing easier.
                                                                                                                                                             
## Refrences

[^1]: [NTFS vs FAT](https://dnl.tebyan.net/Library/Books/pdf/English/0075f27de8b7d47e87ab6969dac55433.pdf)
