# zinetools
Tools for zines

So far, we only have zine_decomposer.py which takes a scan of a zine that's like (for an 8 page pdf)

8 | 1

2 | 7

6 | 3

4 | 5

And makes a new pdf that's like

1

2

3

4

5

6

7

8

(for however many pages)

To use it, install `PyPDF2` and then run `python zine_decomposer.py input.pdf output.pdf`

Upcoming: I don't know, I'm just saving this one little file.