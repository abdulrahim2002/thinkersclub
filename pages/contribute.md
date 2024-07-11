---
layout: page
menu: false
date: '2024-07-21 05:53:59'
title: Contribute
description: contributing
permalink: /contribute/
math: true
---

<img class="img-rounded" src="/assets/img/uploads/thinkersclub.png" alt="Thinkers Club logo" width="200">


# Contributions

To contribute to out website your need to clone this repo, add your post using `initpost.py` or manually adding your post in `_posts`. Please note the front matter properties. 


1. Step 1: Fork the repo

A fork is your own copy of a repo that you own and you can change it.

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_1080/v1720728478/Screenshot_from_2024-07-12_01-37-03_g8qrio.png)
*Fig. 1: Click on the fork button*


2. Step 2: clone your newly forked repo

Click on code and select the ssh. Copy the ssh url. It starts with `git@github.com:`. Please ensure that you have your ssh key setup with your github account, if not follow this two instruction: [generating ssh key and adding it to your accuont](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows) and [adding ssh key to your github account](), or [follow this simeple tutorial](https://www.youtube.com/watch?v=iVJesFfzDGs).

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1720728791/Screenshot_from_2024-07-12_01-42-48_wnjtgi.png)
*Fig. 2: Click on the *

Open terminal, change to the directory where you want to store the repo. And run the following command:

```bash
git clone <url_you_just_copied>
```

To keep track of changes in [original repo](https://github.com/abdulrahim2002/thinkersclub/) you might find it useful to add upstream, bu running:

```bash
git remote add upstream git@github.com:abdulrahim2002/thinkersclub.git
```

This will add upstream as a remote in your local repository so your can run `git fetch` to *fetch* changes and then successively run `git merge upstream/main origin/main` to get those changes in your *main*.

Subsequently you can do the following to keep up to date:

```
git fetch upstream      # fetches latest changes from original repository to your upstream
git switch main         # switch to main
git merge upstream/main # merges upstream/main with your origin/main, hence you are uptodate
```

As a rule of thumb, create new branches in your remote with sensible name(describing the feature it will implement). And make pull requests from this branch i.e. new branches. 

And keep the main branch to fetch changes only and to keep latest copy.

3. Step 3: Switch to new feature branch.

Create a new feature branch, with a descriptive name, i.e. the name should describe the update you make.

```
git checkout -b tutorial # creates a new branch tutorial and switches to it
```

4. Step 4: 

Make the desired changes in your preferred code editor, here's some common changes you might wanna make.

- Add your author: Add yourself as author on the website, so you showup on [members page](www.thinkersclub.tech/members).
    - All authors are stored in `_authors` directory as .md files. Each file is named as name of the author. And has some properties. You might want to change these properties according to your preference.
    - You can use the `initauthor.py` script provided. Execute the script, using `python3 initauthor.py`, or manually add a file in the `_authors` directory and add an author appropriately.

- Add a post: You can add a new post. 
    - All posts are stored in `_posts` directory. 
    - You can use the `initpost.py` script provided. or manually add a post, following conventions.
    - Open the file you created and change its contents. 
    - Change the front matter properties. At top of file and change the contents as your like. **All posts are written in markdown.** and html/css is supported.
    - You can upload the images at any cloud image hosting service like [cloudinary](https://cloudinary.com/), [unsplash](https://unsplash.com/) etc. But cloudnary is a good option since it lets you, resize images dynamically using query parameters. Just upload your image to cloudnary, get the url. In the url, add parameters, `c_scale,w_760`(760 width), just after the /upload. Here's the [documentation](https://cloudinary.com/documentation/resizing_and_cropping).

Make your changes accordingly. If you have any doubts contact me.

5. Step 5: Commit and push your changes

```
git add .
git commit -m "commit message, preferably following conventions: https://www.conventionalcommits.org/en/v1.0.0/"
git push --set-upstream origin tutorial
```

4. Step 6: create a pull request from your feature branch

Go to github and create a pull request.

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/s_scale,w_1080/v1720734359/0723d197-ee8a-47d6-9cea-18e905a68663.png)
*Click and the compare and pull request*

Make sure that, to base repository is `abdulrahim2002/thinkersclub` and base branch is `main`

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_1080/v1720734543/8eda041b-e862-45d4-990e-a851859e47a9.png) 

Resolve merge conflicts (if any).

To check, ensure that your pull request appears in, [issues](https://github.com/abdulrahim2002/thinkersclub/pulls).




Voillaa!! you made it. Contact me, to review and accept.

In case you have any doubts, please feel free to reach out at abdulrahimhere[at]yahoo.com



### Thanks for reading

