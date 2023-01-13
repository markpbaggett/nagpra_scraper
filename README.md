# Islandora 7 Scraper


This script scrapes the viewer, title, description, and metadata elements associated with a work in Islandora 7 
and stores it as a .png.

This script exists to aid in the Office of Repatriation's efforts to discover and make decisions about sensitive content
in our repository.

## Expectations

The script expects a list of PIDs. This list should be generate based on Solr or RISEARCH results or another source.

## Caveats

When the description element is very large, the screenshot will fail to capture the viewer and some metadata.  Some work
is happening to address this.