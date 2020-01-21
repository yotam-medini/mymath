# May override by 
#    make .... PAPER=a4
# or
#    make .... PAPER=letter

ifneq ($(emv),)
emv:
	@echo $($(emv))
endif

PAPER = letter
PAPER = a4

.PRECIOUS: %.dvi %.idx %.toc %.bbl %.ind

.tex.dvi: ;	latex '\scrollmode \input '"$*"; while grep -s 'Rerun to get cross-references right' $*.log; do latex '\scrollmode \input '"$*"; done

%.idx:
	@echo LaTeXing for idx
	latex $(*F)

%.ind: %.idx
	makeindex $*
	@ls -l $@ $< || true

%.ps: %.dvi
	dvips -o $@ -t $(PAPER) $<

%-$(PAPER).bib: %.bib
	rm -f $@
	ln -s $< $@

%-$(PAPER).bbl: Makefile %-$(PAPER).bib %-$(PAPER).tex %.tex
	@echo LaTeXing for bbl
	latex $(*F)-$(PAPER).tex
	bibtex $(*F)-$(PAPER)
	@ls -l $@ || true

%-$(PAPER).dvi: \
	%.tex \
	%-$(PAPER).bbl \
	Makefile \
	%-$(PAPER).ind

%-$(PAPER).pdf: %-$(PAPER).tex %.tex 
	rm -rf pdf;
	(mkdir -p pdf; cd pdf; \
	  ln -s ../$(*F){,-$(PAPER)}.tex .; \
	  ln -s ../q4_4_00_12_9.{py,out} ../$(*F)-$(PAPER).bbl .; \
	  touch $(*F)-$(PAPER).ind; \
	  pdflatex -interaction=nonstopmode $(*F)-$(PAPER).tex; \
	  makeindex $(*F)-$(PAPER); \
	  pdflatex -interaction=batchmode $(*F)-$(PAPER).tex; \
	)
	mv pdf/$(*F)-$(PAPER).pdf .
	ls -l $(*F)-$(PAPER).pdf

clean:
	touch dum
	rm -f *.{dvi,ps,pdf,aux,ind,idx,toc,blg,ilg,log,bbl}

ifeq ($(BASES),)
  BASES = rudin
endif

all-letter:
	for b in $(BASES); do; \
	  $(MAKE) -w PAPER=letter $$b-letter.{dvi,ps,pdf}; \
	done

all-a4:
	for b in $(BASES); do; \
	  $(MAKE) -w PAPER=a4 $$b-a4.{dvi,ps,pdf}; \
	done

all: all-letter all-a4
