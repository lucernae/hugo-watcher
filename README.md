# hugo-watcher
A fork of the debian based klakegg/hugo (https://hub.docker.com/r/klakegg/hugo/) docker image that watches a directory and autobuilds when files change.


Please note that this docker image is quite specific to the Kartoza OpenSource-GIS-Stack (https://github.com/kartoza/OpenSource-GIS-Stack/) project - see that project for a fully worked out example.

If you are just looking for a generic Hugo image that watches a directory and builds when the files change, you can clone and tweak this project - probably you just need to tweak the provided templates.

Here is a sample docker-compose service showing typical usage:

```
version: "3.9"

x-hugo-image: &hugo-image hugo-watcher:latest
volumes:
  generated_hugo_data:
  scp_hugo_data:
  
services:
  hugo-watcher:
    # This service watches for changes in the static content
    # source files of the hugo site and rebuilds the site 
    # whenver a source file is changed.
    # Use the scp volume to upload your markdown files to
    # scp_hugo_data (you need to deploy an scp service for that)
    # docker-compose --profile=site run hugo-watcher
    # or 
    # make odm
    image: *hugo-image
    profiles: ["site"]
    volumes:
      # This is what should be mounted on nginx as a /location
      - generated_hugo_data:/src/public
      # Only raw markdown should be put in here
      # This service will replace content with default from hugo_conf/content_template
      # which is a potentially DESTRUCTIVE operation
      - scp_hugo_data:/src/content
      # config from host mounted volume
      - ./hugo_conf/config.yaml:/src/config.yaml


```
See https://github.com/kartoza/osgs for a full usage example.

Tim Sutton 
info@kartoza.com
July 2021
