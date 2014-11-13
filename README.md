pawprints-adlibs
==================

If you haven't visited http://pawprints.rit.edu/ you should go take a look at it's list of petitions right now. A lot of the petitions on the website are very serious and have a purpose behind them. On the other hand there are petitions that are less serious (or may appear to be).

This script pulls down the petitions from the website and then gives the user several queries to choose words to replace words that were written into the descriptions of the petitions.

## Installing Prerequisites

You need to install TextBlob and NumPy. With Pip we can do this very simply.

```
pip install textblob numpy
```

### simplejson (optional)

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

## Using

This script takes no parameters, just simply `./adlibs.py` to execute it!
