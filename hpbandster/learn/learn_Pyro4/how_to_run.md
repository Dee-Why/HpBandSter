# open three terminal
all in this directory and using the correct virtual-environment
## Terminal1
`pyro4-ns` which means activate the local pyro4 nameserver
## Terminal2
`python greeting-server.py`  find the nameserver and register a name:uri
## Terminal3
`python greeting-client.py`  use the name to find uri, use uri to get access to the class decorated with @Pyro4.expose