# py-byte-pusher
- An implementation of the [BytePusher](https://esolangs.org/wiki/BytePusher) Virtual Machine made in Python. It was my first attempt at something like this but I was able to find some good examples in the internet.
The app only implements Video and CPU operations.

# Tested ROMs:
| ROM  | Status  |
| ------------------- | ------------------- |
|  nyan.bp |  Works 100% |
|  palettetest |  Works 100% |

# Screenshots:
<p align="center">
  <img src="https://i.imgur.com/5fBL7fb.jpg">
  <img src="https://i.imgur.com/alU2wA1.jpg">
</p>

# Perfomance
It is SLOW. It takes about 7-8 seconds for it to render an entire frame using Pygame.
This is probably due to both Python and the configuration of my laptop, as most of the time is spent in the CPU step loop.

