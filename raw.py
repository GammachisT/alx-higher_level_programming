#!/usr/bin/python3
# This is how we can convert github.com url into raw.githubusercontent.com url.
# First copy your github url and replace the following github url
 
link = "https://github.com/GammachisT/alx-system_engineering-devops/blob/main/0x09-web_infrastructure_design/3-scale_up.png"

print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))

# when we run "./filename.py"
# we get the link like the following
# https://raw.githubusercontent.com/GammachisT/alx-system_engineering-devops/main/0x09-web_infrastructure_design/3-scale_up.png
