# py-byte-pusher
- An implementation of the [BytePusher](https://esolangs.org/wiki/BytePusher) Virtual Machine made in Python. It was my first attempt at something like this but I was able to find some good examples in the internet. Thankfully, I didn't need to only paste the code (at least not TOO much). But still, it was a nice little exercise. Might try my luck with a Chip-8 implementation after this.
The app only implements Video and CPU operations.

# Tested ROMs:
- nyan.bp: works perfectly.
- palettetest: works perfectly.
- scrollinglogo: boots and shows graphics, but is extremely slow.
- Sprites.c: throws memory allocation error.

# Screenshots:
<p align="center">
  <img src="https://i.imgur.com/Td722tW.png">
  <img src="https://i.imgur.com/nV7RK7W.png">
  <img src="https://i.imgur.com/VnguOmg.png">
  <img src="https://i.imgur.com/5fBL7fb.jpg">
</p>

# Perfomance
It is SLOW. It takes about 7-8 seconds for it to render an entire frame using Pygame.
This is probably due to both Python and the configuration of my laptop, as most of the time is spent in the CPU step loop.

