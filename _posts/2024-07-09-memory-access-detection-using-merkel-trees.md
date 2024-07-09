---
date: 2024-07-08T17:17:28.000Z
layout: post
title: "Memory Access Detection using Merkel Trees"
subtitle: (Concept) Detecting access to memory using Merkel trees
description: A novel approach to detection of unauthorised memory access, which enables one to identify weather a file/memory block was accessed/tampered.
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

Moreover, if unauthorised access to memory cannot be detected, user of the computer would never know that the system was compromised. Currently, there is no reliable method of detecting weather a file has been accessed. Detecting tampered files is easy, you can hash the contents of the file and when the hash (probably without your knowledge) changes, you might conclude that the file was tampered with. But detecting memory access is a more complicated problem. Although linux does keep track of the last access timestamp, available via that `stat` command. It will only keep track of file accesses that use `read()` syscall[^2]. A malicious actor may still be able to access memory without detection, directly interfacing with hardware.

In this article, I have described an approach to detect accesses to memory usign merkel trees. The approach advocates for encryption of the underlying memory, and the decryption be done in software. We will use a `polluted` flag to identify the files/blocks that have been accessed without user authentication.


## Merkel Trees

Merkel trees are a tree data structure in which hashes are stored rather than data. Leaf nodes store hashes of a particular block of data, while other nodes store hashes of their children. Merkel trees are widely used in blockchains, for its ability to detect tampering of data items. It provides a robust mechanism to detect tampering in multiple distinct data items. The idea is that if any of the data items in leaf node changes, the whole tree would become invalidated, since it will change the hashes of all nodes up the tree.


## Encryption

In addition to merkel trees, we would need encryption. Since, all our measures are of no use if an adversiry can simply access unencrypted data in hardware. Also, the encryption should be done in hardware, and the memory access system calls should define protocalls for decrypting underlying memory, also the same system call would change the necessary variables of the file in question, for example access time etc.

## Memory Access System Call

The memory access system call needs to be implemented in such a way that when one accesses memory the data would be decrypted and other functions[#working] would be performed.

## Architecture

The file system in most operating systems follows a hierarchial structure, we augment this with merkel tree, hence a node would be attached to each file in the file system, these node would form a merkel tree, where each node would contain hash of its children in case of directories and hash of the file data in case of files. In addition a **pollution flag** would be attached to each node, to discern compromised files. 

Each leaf node of the merkel tree 


## Working

When a user/process requests memory, it will go through our system call, which would prompt for password. Once the password is provided the underlying data would be decrypted and 

## Conclusion
The underlying memory would be encrypted, and access would only be allowed through an API.

We will allow an access with invalid credentials, but will flag the file accessed as polluted.

This pollution would show up in the tree. Which makes the tracing easier.
                                                                                                                                                             
## Refrences

[^1]: [NTFS vs FAT](https://dnl.tebyan.net/Library/Books/pdf/English/0075f27de8b7d47e87ab6969dac55433.pdf)
[^2]: [read syscall](https://en.wikipedia.org/wiki/Read_\(system_call\))

