---
date: 2024-07-08T17:17:28.000Z
layout: post
title: "Merkel Trees and computer memory"
subtitle: Merkel trees are data structures which store hashes insted of data. Can we use them in file systems
description: Merkel trees are data structures which store hashes insted of data. Can we use them in file systems
image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1720599290/merkeltreeindirectorytree_dcftly.jpg

# image should be 760, 399 and optimised should be 380, 200
# scaling in url: https://res.cloudinary.com/dm7h7e8xj/image/upload/c_scale,w_800/v1506079212/jekflix-capa_vfhuzh.png

optimized_image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_380/v1720599290/merkeltreeindirectorytree_dcftly.jpg
category: concept
tags:
    - file system
    - merkel trees
    - security
author: abdulrahim
---

## Introduction

<!-- mine
Computer memory is usually implemented as a file system. While tampering
of data is easy to detect, unauthorised access to memory is a more
complex task. A problem that lies in the domain of Intrusion Detection
Systems. While, most intrusion detection focus on analyzing network
traffic, or machine learning techniques to identify suspicious patterns.
We propose a method that works within the system, providing robust
access detection.
-->

Computer memory is usually implemented as a file system. While tampering
with data is easy to detect, unauthorized access to memory is a more
complex task falling within the domain of Intrusion Detection Systems
(IDS). Most intrusion detection systems focus on analyzing network traffic or
using machine learning techniques to identify suspicious patterns, we
explore if we can employ merkel trees for this task.

<!--
If unauthorised access to memory cannot be detected, user of the
computer would never know that the system was compromised. Detecting
tampered files is easy, you can hash the contents of the file and when
the hash changes (probably without your knowledge), you might conclude
that the file was tampered with. But detecting memory access is a more
complicated problem. Although linux does keep track of the last access
timestamp, available via that `stat` command[^stat]. It will only keep
track of file accesses that use `read()` syscall[^read]. A malicious
actor may still be able to access memory, directly interfacing with
hardware.
-->

If unauthorized memory access cannot be detected, users would never know
that the system was compromised. Detecting tampered files is
straightforward: you can hash the contents of a file, and if the hash
changes you might conclude that the file changed. However, detecting
memory access is more complicated. Although Linux keeps track of the
last access timestamp, available via the `stat` command[^stat], it only
tracks file accesses that use the `read()` syscall[^read].

<!--
In this article, I have described an approach to detect accesses to
memory usign merkel trees. The approach advocates for encryption of the
underlying memory, and the decryption be done in software. We will use a
`polluted` flag to identify the files/blocks that have been accessed
without user authentication.
-->

<!--
In this article, I describe an approach to detect memory access using
Merkle trees. The approach advocates for encrypting the underlying
memory, with decryption performed in software. We will use a "polluted"
flag to identify files or blocks that have been accessed without user
authentication.
-->


## Merkel Trees

<!--
Merkel trees are a tree data structure in which hashes are stored rather
than data. Leaf nodes store hashes of a particular block of data, while
other nodes store hashes of their children. Merkel trees are widely used
in blockchains, for its ability to detect tampering of data items. It
provides a robust mechanism to detect tampering in multiple distinct
data items. The idea is that if any of the data items in leaf node
changes, the whole tree would become invalidated, since it will change
the hashes of all nodes up the tree.
-->

Merkle trees are a data structure in which hashes are stored rather than
data. Leaf nodes store hashes of particular data blocks, while other
nodes store hashes of their children. Merkle trees are widely used in
blockchains for their ability to detect data tampering. They provide a
robust mechanism to detect tampering in multiple distinct data items. If
any data item in a leaf node changes, the whole tree becomes invalidated
because it changes the hashes of all nodes up the tree.


![Merkel tree](
https://res.cloudinary.com/dg6zyzzwr/image/upload/v1720603045/merkel_tree_vr2ji1.png)
*Fig. 1: A Merkle tree is a data structure in which each node contains a
hash. All non-leaf nodes contain hashes of their children, and all leaf
nodes contain hashes of the underlying data.*  

## Merkel tree as directory tree

Now, what we want to do is to augment the directory tree as a merkel
tree. To be exact the [_inode structure_](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/fs/ext4/ext4.h?h=v6.12-rc1#n771) (See [_inode doc_](https://www.kernel.org/doc/html/latest/filesystems/ext4/inodes.html) for more details).

Doing this would make us have hashes for children in directory tree. And
the benefit of that is whenever the child inodes change, the
current inode would change. And there's 2 fields that each node would
contain, the last seen hash (expected hash) of it's child and the
current hash of the same child. And when the current hash changes to a
different value from expected hash, then we can imply that the child
inode changed.

But one question is that if memory can be accessed bare metal, then the
protections done in software doesn't really make any sense. One possible
solution to this problem is employing encryption.

The encryption should be performed in hardware, and the memory access
system calls should define protocols for decrypting the underlying
memory. The same system call would update necessary variables of the
file in question, such as access time. The memory access system call
needs to be implemented so that when one accesses memory, the data is
decrypted and other [functions](#working) are performed.

Below is a detailed description.

## Architecture

File system in most operating systems follow a hierarchical structure. We
augment this with a Merkle tree, where a node is attached to each file
in the file system. These nodes form a Merkle tree, where each node
contains the hash of its children (in the case of non-leaf nodes) or the
hash of the file data (in the case of files). Additionally, a **pollution
flag** is attached to each node to detect illegal access.

Each node will also has an expected hash, which is the hash of the node
when the subtree below that node was last valid.

## Working

The pollution flag is set if `expected_hash != hash`, which occurs only
on illegal access. I will explain this in a moment.

When a user or process requests memory, it will go through the memory
access system call, requiring authentication. Once the authentication is
successful, the underlying data is decrypted and returned, the access
time is updated, and all the hashes up to the root are updated along
with the expected hash (note that the expected hash changes on
authorized access). The tree remains valid.

If the authentication fails, the memory is not returned, but the access
time changes. Consequently, when the tree is re-evaluated, the hash of
this node changes since it incorporates the access time, but the
expected hash remains the same, setting the pollution flag for this
node.

Since the parent of this node uses its hash, the parent's hash also
changes. However, its expected hash remains the same, leading to its
invalidation. This process continues up the tree, invalidating the whole
tree.

The benefit of this approach is that all other nodes remain valid. If
one tries to determine which file was accessed and the timestamp, it is
easy to identify the exact file by following the invalid nodes from top
to bottom.

## Refrences

[^stat]: [stat man page](https://linux.die.net/man/2/stat)
[^read]: [read syscall](https://en.wikipedia.org/wiki/Read_(system_call))

