BASES = rudinfa
-include ../Makefile

TEXS = $(wildcard rudinfa*.tex)

default: rudinfa-a4.pdf

rudinfa-$(PAPER).dvi: rudinfa.tex rudinfa-a4.ind rudinfa-a4.bib \
	rudinfa.bib

# One shot run
rudinfa-dvi:
	latex '\errorstopmode \input rudinfa-a4.tex' < /dev/null

rudinfa-a4.pdf:  ${TEXS}
	latexmk -pdf -halt-on-error rudinfa-a4.tex

lclean:
	rm -f rudinfa-a4.aux


# not for relase
-include Make.local
