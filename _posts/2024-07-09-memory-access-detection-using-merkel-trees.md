---
date: 2024-07-08T17:17:28.000Z
layout: post
title: "Memory Access Detection using Merkel Trees"
subtitle: (Concept) In a novel approach, we explore application of Merkel Trees in detection of unauthorised access
description: A novel approach to detection of unauthorised memory access, which enables one to identify weather a file/memory block was accessed/tampered
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
complex task, falling within the domain of Intrusion Detection Systems
(IDS). Most intrusion detection focuses on analyzing network traffic or
using machine learning techniques to identify suspicious patterns. We
propose a method that operates within the system, providing robust
access detection.

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
changes (probably without your knowledge), you might conclude that the
file was tampered with. However, detecting memory access is more
complicated. Although Linux keeps track of the last access timestamp,
available via the `stat` command[^stat], it only tracks file accesses
that use the `read()` syscall[^read].

<!--
In this article, I have described an approach to detect accesses to
memory usign merkel trees. The approach advocates for encryption of the
underlying memory, and the decryption be done in software. We will use a
`polluted` flag to identify the files/blocks that have been accessed
without user authentication.
-->

In this article, I describe an approach to detect memory access using
Merkle trees. The approach advocates for encrypting the underlying
memory, with decryption performed in software. We will use a "polluted"
flag to identify files or blocks that have been accessed without user
authentication.


---

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

<!--
*Fig. 1: A merkel tree is a data structure in which each node contains a
hash. All non leaf nodes contain hash(hash of their childrens) and all
leaf nodes contain hash(underlying data)*
-->



## Encryption


<!--
In addition to merkel trees, we would need encryption. Also, the
encryption should be done in hardware, and the memory access system
calls should define protocalls for decrypting underlying memory, also
the same system call would change the necessary variables of the file in
question, for example access time etc.
-->

In addition to Merkle trees, we need encryption. This encryption should
be performed in hardware, and the memory access system calls should
define protocols for decrypting the underlying memory. The same system
call would update necessary variables of the file in question, such as
access time.


## Memory Access System Call

<!--
The memory access system call needs to be implemented in such a way that
when one accesses memory the data would be decrypted and other
[functions](#working)  would be performed.
-->

The memory access system call needs to be implemented so that when one
accesses memory, the data is decrypted and other [functions](#working) are
performed.


## Architecture

<!--
The file system in most operating systems follows a hierarchial
structure, we augment this with merkel tree, hence a node would be
attached to each file in the file system, these node would form a merkel
tree, where each node would contain hash of its children in case of
non-leaf nodes and hash of the file data in case of files. In addition a
**pollution flag** would be attached to each node, to discern files that
have been accessed without authorization.
-->

Most operating systems' file systems follow a hierarchical structure. We
augment this with a Merkle tree, where a node is attached to each file
in the file system. These nodes form a Merkle tree, where each node
contains the hash of its children (in the case of non-leaf nodes) or the
hash of the file data (in the case of files). Additionally, a **pollution
flag** is attached to each node to identify files that have been accessed
without authorization.

<!--
Also, there will be an **expected hash** for each node, which is the
hash if the node is valid. Expected hash would contain the last hash
value when the subtree below that node was valid.
-->

Each node will also have an expected hash, which is the hash of the node
when the subtree below that node was last valid.



## Working

<!--
Pollution flag is set if `expected_hash != hash`, which would **only**
occur if either the memory was accessed or tampered in an unauthorised
way. I will explain this in a moment.
-->

The pollution flag is set if `expected_hash != hash`, which occurs if the
memory was accessed or tampered with in an unauthorized way. I will
explain this in a moment.


<!--
When a user/process requests memory, it will go through our system call,
which would require authentication. Once the authentication is
successfull underlying data would be decrypted and returned, the access
time would change, and all the hashes upto root change along with
expected hash(*note that we change expected hash on authorised access*).
The tree remains valid.
-->

When a user or process requests memory, it will go through our system
call, requiring authentication. Once the authentication is successful,
the underlying data is decrypted and returned, the access time is
updated, and all the hashes up to the root are updated along with the
expected hash (note that the expected hash changes on authorized
access). The tree remains valid.

<!--
And if the authentication fails, then what would happen is the memory
will not be returned, but the access time would change.  The consequence
of this is that when next time, tree would be re-evaluated, the hash of
this node would change, since it incorporates accesss time, but the
expected hash would remain same, leading to pollution flag being set for
this node.
-->

If the authentication fails, the memory is not returned, but the access
time changes. Consequently, when the tree is reevaluated, the hash of
this node changes since it incorporates the access time, but the
expected hash remains the same, setting the pollution flag for this
node.


<!--
And since the parent of this node uses this nodes hash, the parents hash
would also change. But its expected hash also remains the same, leading
it to becoming invalidated. The same process would happen all up the
tree. Leading to the whole tree becoming invalidated.
-->

Since the parent of this node uses its hash, the parent's hash also
changes. However, its expected hash remains the same, leading to its
invalidation. This process continues up the tree, invalidating the whole
tree.


<!--
The benefit of this approach is that all other nodes remain valid.
Hence, if one tries to triage, which file it was and what was the
timestamp, then it is easy to point out the exact file, because one only
needs to follow invalid nodes top to bottom.
-->


The benefit of this approach is that all other nodes remain valid. If
one tries to determine which file was accessed and the timestamp, it is
easy to identify the exact file by following the invalid nodes from top
to bottom.


## Conclusion

<!--
We, described an approach to detect memory access, which relies on
merkel trees along with encryption.

However, one might argue that access detection can simply be done with
encrypted memory, all failed authentication attempts are simply
unauthorised access detection. While this is true, but keeping track of
such a system will be expensive in terms of space, since each block will
have its own database of illegal access. Also to manage such a system
would be difficult.


Our approach provides a better solution, firstly it provides a structure
that can be incorporated with existing filesystems, requiring mimnimal
change. Secondly, it provides an efficient method for detection of files
that might be accessed.  -->


In this article, we presented a novel approach to detecting unauthorized
memory access using Merkle trees and encryption. Our method enhances
existing file system structures by integrating Merkle trees, allowing
for robust detection of tampering and unauthorized access. By encrypting
memory and employing a "polluted" flag to signal unauthorized access
attempts, our approach provides a reliable and efficient means of
safeguarding data integrity.

This technique addresses the limitations of traditional intrusion
detection systems that primarily focus on network traffic or machine
learning techniques. Instead, our solution operates within the system,
ensuring that unauthorized memory access is promptly detected and
addressed. By incorporating this method, we can offer a more secure and
resilient computing environment, protecting users from potential threats
and maintaining the integrity of their data.


## Refrences

[^stat]: [stat man page](https://linux.die.net/man/2/stat)
[^read]: [read syscall](https://en.wikipedia.org/wiki/Read_(system_call))

