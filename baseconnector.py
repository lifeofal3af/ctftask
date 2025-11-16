from pwn import *

HOST = "c32891d7da2e219e.chal.ctf.ae"
io = remote(host=HOST, port=443, ssl=True, sni=HOST)

io.interactive()
