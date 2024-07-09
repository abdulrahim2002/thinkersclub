#! /usr/bin/python3

from os.path import abspath, join, dirname, exists
from datetime import datetime

root = dirname(abspath(__file__))
posts_dir = join(root,"_posts")
print(f"parent dir: {root}")

def create_new_post(title):
    # Get the current date and time
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")  # Use hyphens instead of colons

    # Format the title to be used in the post file name
    formatted_title = title.lower().replace(" ", "-")  # Replace spaces with underscores
    post_filename = f"{date_string}-{formatted_title}.md"

    # Set the front matter data
    layout = "post"
    fullFormatDate = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    subtitle = f"{title}"
    description = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    image_url = "https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1720559138/default_bvrxw3.png"
    optimized_image_url = "https://res.cloudinary.com/dg6zyzzwr/image/upload/c_scale,w_760/v1720559138/default_bvrxw3.png"
    category = "dev"
    tags = "  - comp science\n  - dev"
    author = "thinkersclub"

    # Define the content of the post with front matter
    content = f"""---
date: {fullFormatDate}
layout: {layout}
title: '{title}'
subtitle: {subtitle}
description: {description}


# host image at any image hosting service and paste url's here
# image should be 760, 399
image: {image_url}

# and optimised should be 380, 200
optimized_image: {optimized_image_url}
category: {category}
tags:
{tags}
author: {author}
---

## somehting



## adding images

host your images somewhere, and put it here as:

![image](url)

host in cludinary or unsplash are good, because they let you control requested images in query parameters. 

when hosting on cloudinary, upload the image. then after the upload add,

/c_scale,w_780 

for a width of 780.


for example:
https://cloudinary.com/documentation/resizing_and_cropping
"""

    post_path = join(posts_dir, post_filename)

    if exists(post_path):
        print(f"Post {post_path} already exists")
    else:
        with open(post_path, "w") as f:
            f.write(content)
            print(f"created successfullt at: {post_path}")
            return

def main():
    title = input("Enter post title: ")
    create_new_post(title)


if __name__ == "__main__":
    main()
