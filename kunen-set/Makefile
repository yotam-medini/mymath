BASES = kunen
include ../common.makefile

default: kunen-a4.pdf

KUNEN_TEXS = kunen-a4.tex kunen.tex kunen1.tex

kunen-a4.pdf: ${KUNEN_TEXS}
	latexmk -pdf -halt-on-error kunen-a4.tex
