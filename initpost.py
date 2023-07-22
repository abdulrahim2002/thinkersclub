# reference frontmatter
# date: 2019-05-16T23:48:05.000Z
# layout: post
# title: "New"
# subtitle: New Post
# description: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut et dolore magna aliqua.
# image: https://images.unsplash.com/photo-1520970014086-2208d157c9e2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80

# optimized_image: https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?utm_medium=medium&w=700&q=50&auto=format
# category: life
# tags:
#   - life
#   - tips
# author: abdulrahim

import os
from datetime import datetime

parentPath = os.getcwd()
print(parentPath)

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
    subtitle = f"{title} Post"
    description = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    image_url = "https://res.cloudinary.com/dz48emek2/image/upload/v1689964438/samples/food/spices.jpg"
    optimized_image_url = "https://res.cloudinary.com/dz48emek2/image/upload/v1689964438/samples/food/spices.jpg"
    category = "life"
    tags = "- life\n  - tips"
    author = "abdulrahim"

    # Define the content of the post with front matter
    content = f"""---
date: {fullFormatDate}\n
layout: {layout}\n
title: "{title}"\n
subtitle: {subtitle}\n
description: {description}\n
image: {image_url}\n
optimized_image: {optimized_image_url}\n
category: {category}\n
tags:
{tags}\n
author: {author}
---

Your post content goes here.
"""

    # Set the path to your Jekyll website's "_posts" directory
    posts_dir = "_posts"
    post_path = os.path.join(parentPath, posts_dir, post_filename)
    print(post_path)

    # Check if the post file already exists
    if os.path.exists(post_path):
        print(f"A post with the title '{title}' already exists.")
        return

    # Create the new post file
    with open(post_path, "w") as post_file:
        post_file.write(content)

    print(f"New post '{title}' created successfully.")

if __name__ == "__main__":
    # Prompt the user for the post title
    post_title = input("Enter the title for the new post: ")
    create_new_post(post_title)
