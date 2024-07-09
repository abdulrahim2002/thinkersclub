#! /usr/bin/python3

"""
default:
---
layout: author
photo: /assets/img/uploads/thinkersclub.png
name: defaultname
display_name: Default Name
position: For academic heads only
bio: Describe your interesets and what you work/like to work on
# github_username:
# twitter_username:
# instagram_username:
# linkedin_username:
# medium_username:
---
"""

from datetime import datetime
from os.path import join, dirname, abspath, exists

parent_dir = dirname(abspath(__file__))
authors_dir = join(parent_dir, "_authors")

def main():
    name = input("Enter your(author's) name: ")
    author_file = join( authors_dir, f"{name}.md")
    content = f"""---
# comment out any field with `#` to leave out
layout: author

# Add your profile picture, you can use any image hosting service of you choice.
# or store your picture here(not recommended because of space concerns).
# Add your image in `/assets/img/uploads/`and replace `thinkersclub.png` below
# to your filename
# Please ensure that aspect ratio is 1:1 and resolution is less than 680x680
photo: /assets/img/uploads/thinkersclub.png

# or your can host your image somewhere and add url to it here
# photo: "https://" # i.e. url of your profile picture

name: {name}
display_name: Default Name
position: your position
bio: Describe your interesets and what you work / would like to work on, in short
# keep commented in case dont want to provide
# github_username:
# twitter_username:
# instagram_username:
# linkedin_username:
# medium_username:
---
"""
    if exists(author_file):
        print("Author already added")
        return
    else
        with open(author_file, "w") as f:
            f.write(content)

    print(f"File created: {author_file}\nPlease change front matter properties, according to your preference.")


if __name__ == "__main__":
    main()
