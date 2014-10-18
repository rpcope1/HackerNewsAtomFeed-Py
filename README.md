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