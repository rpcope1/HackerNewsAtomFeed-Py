# Hacker News Atom Feed Server
=====================

This is a simple atom feed server based on HackerNewsAPI, pyatom,
and SimpleHTTPServer, which creates an Atom feed server on your local machine.
To setup the server,

```
    python setup.py develop
```

To launch the server, after installing, simply call

```
    python -m HNAtomFeedGen (OPT: Hostname) (OPT: Port) (OPT: Feed update in minutes)
```

or locally,

```
    python HNAtomFeedServe.py (OPT: Hostname) (OPT: Port) (OPT: Feed update in minutes)
```

The feed can be accessed at:

```
    http://(hostname):(port)/
    http://(hostname):(port)/feed.xml
```


in your favorite Atom news reader.

## Bugs, Features, and other Issues

If you find a bug, would like a feature added, or have an issue, open an issue ticket, and I will attend to it.
I am also to pull requests, so if you want to fix or add something, the fork the repo and send me a pull request.
I promise I don't bite (too much). ;)