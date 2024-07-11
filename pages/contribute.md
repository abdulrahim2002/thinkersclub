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

To contribute to the website you need to fork to repository, make changes to your fork and submit a pull request, below are the detailed steps for your reference:

- Step 1: Fork the repo

A fork is your own copy of a repo that you own and you can change it.

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_1800/v1720728478/Screenshot_from_2024-07-12_01-37-03_g8qrio.png)
*Fig. 1: Click on the fork button*


-  Step 2: clone your newly forked repo

Click on code and select the ssh. Copy the ssh url. It starts with `git@github.com:`. Please ensure that you have your ssh key setup with your github account, if not follow these instructions: [generating ssh key and adding it to your accuont](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows) or [follow this simeple tutorial](https://www.youtube.com/watch?v=iVJesFfzDGs).

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_1800/v1720728791/Screenshot_from_2024-07-12_01-42-48_wnjtgi.png)
*Fig. 2: Copy the ssh url*

Open terminal, change to the directory where you want to store the repo. And run the following command:

```bash
git clone <url_you_just_copied>
```

To keep track of changes in [original repo](https://github.com/abdulrahim2002/thinkersclub/) you might find it useful to add upstream, by running:

```bash
git remote add upstream git@github.com:abdulrahim2002/thinkersclub.git
```

This will add upstream as a remote in your local repository so your can run `git fetch` to *fetch* changes and then successively run `git merge origin/main` to get those changes in your *main*.

Subsequently, you can do the following to keep up to date:

```
git fetch upstream      # fetches latest changes from original repository to your upstream
git switch main         # switch to main
git merge upstream/main # merges upstream/main with your origin/main, hence you are uptodate
```

As a rule of thumb, create new branches in your remote with sensible name(describing the feature it will implement). And make pull requests from this branch i.e. new branches. 

And keep the main branch to fetch changes only and to keep latest copy.

- Step 3: Switch to new feature branch.

Create a new feature branch, with a descriptive name, i.e. the name should describe the update you make.

```
git checkout -b tutorial # creates a new branch tutorial and switches to it
```

- Step 4: 

Make the desired changes in your preferred code editor, here's some common changes you might wanna make.

- Add your author: Add yourself as author on the website, so you showup on [members page](www.thinkersclub.tech/members).
    - All authors are stored in `_authors` directory as .md files. Each file is named as name of the author. And has some properties. You might want to change these properties according to your preference.
    - You can use the `initauthor.py` script provided. Execute the script, using `python3 initauthor.py`, or manually add a file in the `_authors` directory and add an author appropriately.

- Add a post: You can add a new post. 
    - All posts are stored in `_posts` directory. 
    - You can use the `initpost.py` script provided. or manually add a post is `_posts` directory.
    - Open the file you created and change its contents. 
    - Change the front matter properties. At top of file and change the contents as your like. **All posts are written in markdown,** and html/css is supported.
    - You can upload the images at any cloud image hosting service like [cloudinary](https://cloudinary.com/), [unsplash](https://unsplash.com/) etc. But cloudnary is a good option since it lets you, resize images dynamically using query parameters. Just upload your image to cloudnary, get the url. In the url, add parameters, `c_scale,w_760`(760 width), just after the /upload. Here's the [documentation](https://cloudinary.com/documentation/resizing_and_cropping).

Make your changes accordingly. If you have any doubts contact me.

- Step 5: Commit and push your changes

```
git add .
git commit -m "commit message, preferably following conventions"
git push --set-upstream origin tutorial
```

See, [commit conventions](https://www.conventionalcommits.org/en/v1.0.0/)


- Step 6: create a pull request from your feature branch

Go to github and create a pull request.

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_1800/v1720734359/0723d197-ee8a-47d6-9cea-18e905a68663.png)
*Fig. 3: Click and the compare and pull request*

Make sure that, to base repository is `abdulrahim2002/thinkersclub` and base branch is `main`

![](https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_1800/v1720734543/8eda041b-e862-45d4-990e-a851859e47a9.png) 
*Fig. 4: Create pull request*

Resolve merge conflicts (if any).

To check, ensure that your pull request appears in, [issues](https://github.com/abdulrahim2002/thinkersclub/pulls).


Voillaa!! you made it. Contact me, so i can review and accept your changes.

In case you have any doubts, please feel free to reach out at abdulrahimhere[at]yahoo.com


### Thanks for reading

