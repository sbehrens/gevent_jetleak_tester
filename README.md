# gevent_jetleak_tester
Gevented script for checking servers for Jetleak vulnerability.  

See [GDS Security](http://blog.gdssecurity.com/labs/2015/2/25/jetleak-vulnerability-remote-leakage-of-shared-buffers-in-je.html) for more information.

## Usage
Simply specifiy a list of new line delimited urls for testing

```
python jetleak_tester.py urls.txt
```

## Requires
Requests
Gevent
