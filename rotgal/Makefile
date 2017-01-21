# May override by 
#    make .... PAPER=a4
# or
#    make .... PAPER=letter
PAPER = letter
PAPER = a4

SHELL=/bin/bash

ifneq ($(emv),)
emv:
	@echo $($(emv))
endif

.DELETE_ON_ERROR:

.PRECIOUS: %.dvi %.idx %.toc %.bbl

.tex.dvi: ;	latex '\scrollmode \input '"$*"; while grep -s 'Rerun to get cross-references right' $*.log; do latex '\scrollmode \input '"$*"; done

%.idx:
	@echo LaTeXing for idx
	latex $(*F)

%.ind: %.idx
	makeindex $*
	@ls -l $@ $< || true

# %-$(PAPER).bbl: %-$(PAPER).aux
#%.bbl: %.tex
#	@echo LaTeXing for bbl
#	latex $(*F)
#	bibtex $*
#	@ls -l $@ || true

%.ps: %.dvi
	dvips -o $@ -t $(PAPER) $<

rotgal-$(PAPER).bib: rotgal.bib
	rm -f $@
	ln -s $< $@

rotgal-$(PAPER).bbl: Makefile rotgal-$(PAPER).bib rotgal-$(PAPER).tex rotgal.tex
	@echo LaTeXing for bbl
	latex rotgal-$(PAPER).tex
	bibtex rotgal-$(PAPER)
	@ls -l $@ || true

rotgal-$(PAPER).dvi: \
	q4_4_00_12_9.out \
	rotgal-$(PAPER).bbl \
	Makefile \
	rotgal-$(PAPER).ind


q4_4_00_12_9.out: q4_4_00_12_9.py
	$< > $@

rotgal-$(PAPER).pdf: rotgal-$(PAPER).tex rotgal.tex q4_4_00_12_9.out rotgal.bib
	rm -rf pdf;
	(mkdir -p pdf; cd pdf; \
	  ln -s ../rotgal{,-$(PAPER)}.tex .; \
	  ln -s ../q4_4_00_12_9.{py,out} ../rotgal-$(PAPER).bbl .; \
	  touch rotgal-$(PAPER).ind; \
	  pdflatex -interaction=nonstopmode rotgal-$(PAPER).tex; \
	  makeindex rotgal-$(PAPER); \
	  pdflatex -interaction=batchmode rotgal-$(PAPER).tex; \
	)
	mv pdf/rotgal-$(PAPER).pdf .
	ls -l rotgal-$(PAPER).pdf

# One shot run
rotgal-dvi:
	latex '\errorstopmode \input rotgal-a4.tex' < /dev/null


srcfiles = \
	rotgal.tex \
	rotgal-letter.tex \
	rotgal-a4.tex \
	Makefile \
	q4_4_00_12_9.py \
	rotgal.bib

rotgal.tgz: $(srcfiles)
	tar cvfz $@ $(srcfiles)
	ls -l $@

clean:
	touch dum
	rm -f *.{dvi,ps,pdf,aux,ind,idx,toc,blg,ilg,log,bbl} \
	   q4_4_00_12_9.out dum

all-letter:
	$(MAKE) -w PAPER=letter rotgal-letter.{dvi,ps,pdf}

all-a4:
	$(MAKE) -w PAPER=a4 rotgal-a4.{dvi,ps,pdf}

all: all-letter all-a4

# not for relase
-include Make.local
