BASE = kunen1980
include ../common.makefile

default: ${BASE}-a4.pdf

KUNEN_TEXS = ${BASE}-a4.tex ${BASE}.tex ${BASE}_1.tex ${BASE}_2.tex

${BASE}-a4.pdf: ${KUNEN_TEXS}
	latexmk -pdf -halt-on-error ${BASE}-a4.tex
