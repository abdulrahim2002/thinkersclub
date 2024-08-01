---
date: 2024-06-01T14:22:31.000Z
layout: post
title: 'How to compile vim with clipboard support'
subtitle: One major problem beginners face with vim is the inability to copy from/to system clipboard. While usually this problem is solved by installing gvim; an unnecessary bloat. In this article we discover how we can compile vim with clipboard support.

description: One major problem beginners face with vim is the inability to copy from/to system clipboard. While usually this problem is solved by installing gvim; an unnecessary bloat. In this article we discover how we can compile vim with clipboard support.

# host image at any image hosting service and paste url's here
# image should be 760, 399
image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1720559138/default_bvrxw3.png

# and optimised should be 380, 200
optimized_image: https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1720559138/default_bvrxw3.png
category: dev
tags:
  - comp science
  - dev
author: abdul
---

## Introduction

When you install vim, a usual requirement as with all text editors is
the ability to copy to/from system clipboard so you can lets say, copy
something into your vim session from lets say firefox. Or vice versa,
however copy pasting in terminal editors is not as straight forward as
with GUI editors. In vim if you want to copy something into an auxilary
space( anticipating it would be used later, so you can paste from this
auxilary space ) is achieved by **registers**.

The register that represents system clipboard is `+` register. Anything
that you copy into this register is available in system clipboard.

## How to use registers to copy/paste

To copy a text into a register, select it in visual mode and press 
`"<register_name>y` to yank the contents into the given register. And to
paste the contents of a particular register at current position, use
`"<register_name>p`.

To use system clipboard, you just have to substitute "+" in the above
commands. 


## clipboard support

But the `+` register wont work unless you have clipboard support with
your vim installation. By default there is no clipboard support in vim.

To check if your vim installation has clipboard support use:

```bash
$ vim --version | grep clipboard
+clipboard         +keymap            +printer           +vertsplit
+ex_extra          +mouse_netterm     +syntax            +xterm_clipboard
```

or inside of vim, you can run the command:

```
:echo has('clipboard')
```

If the output is **0**, your installation doesnt have clipboard support.


## Compiling vim

Now there are 2 solutions to this problem:

1. Either install **gvim**:
2. Or compile vim from sources with clipboard support

To install `gvim`:

On Debian:

```
sudo apt install vim-gtk
```

On Fedora

```
sudo dnf install gvim
```

## How to compile vim with clipboard support

Below are the simple steps:

### Step 1: Grab the sources

Clone the repository:

```
git clone https://github.com/vim/vim.git vim
cd vim
```

### Step 2: Install dependencies

Install the required libraries and tools to build vim, for example gcc,
x11 etc. Note that you only need them to compile vim and you are free to
delete them once you are done.

On Debian:

```
sudo apt install build-essential libx11-dev libncurses5-dev
```

On Fedora:

```
sudo dnf groupinstall "Development Tools"
sudo yum install gcc
sudo yum groupinstall "X Software Development"
sudo dnf install libX11-devel ncurses-devel 
```

Also, you need to remove the existing installation(if any).

On Debian

```
sudo apt remove vim
```

On Fedora

```
sudo dnf remove vim gvim
```

### Step 3: Configure and Compile

Configure vim with features of your choice

```bash
./configure \\
--enable-cscope \\
--enable-gui=auto \\
--enable-gtk2-check \\
--enable-gnome-check \\
--with-features=huge \\
--with-x 
```


Then compile and install with:

```
make
sudo make install
```


## Conclusion

In this article we learned how can we compile vim with clipboard
support, you can also tweak configuration according to your
requirements. There are many configuration options available.
