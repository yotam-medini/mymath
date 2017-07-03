BASES = rudinfa
-include ../Makefile

rudinfa-$(PAPER).dvi: rudinfa.tex rudinfa-a4.ind rudinfa-a4.bib \
	rudinfa.bib

# One shot run
rudinfa-dvi:
	latex '\errorstopmode \input rudinfa-a4.tex' < /dev/null

.PSEUDO: pdf
# errorstopmode  batchmode
pdf:
	pdflatex -interaction nonstopmode rudinfa-a4.tex

lclean:
	rm -f rudinfa-a4.aux


# not for relase
-include Make.local
