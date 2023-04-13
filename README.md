describezip
===========

* Takes in a single zip archive (`filename`)
* Filters out files that don't match a file regex (`file_regex_string`)
* Merges together all objects from all files into a single object tree.
* Pretty-prints out the merged tree, with summary data for each leaf node.

Example summary data:
* int | float -> min, avg, max, count, count_unique
* str -> frequency count of each string type
* boolean -> frequency count for true | false | null
* mixed -> lists all unique types used

Example usage
-------------
All JSON blobs

`python test_archive.zip`

Only load X.json files where X is a number  
`python test_archive.zip "^\d*\.json$"`


Requirements
------------
Python 3.10+ (for PEP 636)