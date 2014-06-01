wethepeople-adlibs
==================

If you haven't visited https://petitions.whitehouse.gov/ you should go take a look at it's list of petitions right now. A lot of the petitions on the website are very serious and have a purpose behind them. On the other hand there are petitions that are less serious (or may appear to be).

This script pulls down the petitions from the website and then gives the user several queries to choose words to replace words that were written into the descriptions of the petitions.

## Installing Prerequisites

### simplejson

#### On GNU/Linux:

  1. Open up a terminal and run the following command
  ```
  sudo easy_install simplejson
  ```

#### On Windows:

  1. Download the simplejson tarball from here: https://pypi.python.org/pypi/simplejson/
  2. Extract the tarball
  3. Open up a command shell in the directory you extracted the tarball into
  4. Run the following command `python setup.py install`

### NLTK (Python Natural Language Toolkit)

#### On GNU/Linux:

  1. First you need to install NLTK do so by following the link below:
  http://www.nltk.org/install.html
  2. Next you need to download some NLTK data
  3. Open up a python shell (as root) `sudo python`
  4. Open the NLTK downloader
  ```
  import nltk
  nltk.download()
  ```
  Once you have the downloader open:
  
  1. Set the installation directory to `/usr/share/nltk_data`
  2. Download the package `maxent_treebank_pos_tagger`

#### On Windows:

  1. First you need to install NLTK do so by following the windows installation instructions in the link below:
  http://www.nltk.org/install.html
  2. Next you need to download some NLTK data
  3. Open up a python shell and enter the following command to open up the NLTK downloader
  ```
  import nltk
  nltk.download()
  ```
  Once you have the downloader open:
  
  1. Set the installation directory to `C:\nltk_data`
  2. Download the package `maxent_treebank_pos_tagger`

## Using

This script takes no parameters, just simply `./adlibs.py` to execute it!
