BASES = rudinrca
-include ../Makefile

FIGTEXS = 10-37-a.tex 10-37-b.tex 10-37-c.tex 10-37-d.tex

$(FIGTEXS): 10-37.py
	$< 10-37

figtexs: $(FIGTEXS)

rudinrca-$(PAPER).dvi: rudinrca.tex rudinrca-a4.ind rudinrca-a4.bib \
	rudinrca.bib $(FIGTEXS)

rudinrca-a4.bib: rudinrca.bib
	rm -f $@
	ln -s $< $@

# One shot run
# One shot run
%-dvi: %.tex
	latex -interaction=errorstopmode $< < /dev/null

rudinrca-dvi:
	latex -interaction=errorstopmode rudinrca-a4.tex < /dev/null

rudinrca-dvi-old:
	latex '\errorstopmode \input rudinrca-a4.tex' < /dev/null

#	 ln -s ../rudinrca-a4.tex ../rudinrca.tex .; 
# rudinrca-a4.pdf: rudinrca-a4.tex rudinrca.tex
RUDINTEXS = \
	rudinrca1.tex \
	rudinrca2.tex \
	rudinrca3.tex \
	rudinrca4.tex \
	rudinrca5.tex \
	rudinrca6.tex \
	rudinrca7.tex \
	rudinrca8.tex \
	rudinrca9.tex \
	rudinrca10.tex \
	rudinrca11.tex \


rudinrca-a4.pdf: rudinrca-a4.tex rudinrca.tex ${RUDINTEXS} 10-37-fig.tex
	TEXINPUTS=.:..:${TEXINPUTS} latexmk -pdf -halt-on-error rudinrca-a4.tex
	ls -l $@

# 10-37-fig.tex: 10-37.py
#	$< > $@

rudinrca-a4.dvi: 10-37-fig.tex

mposts:
	mpost myfigs.mp

clean-pdf:
	rm -f rudin*.pdf


SRCFILES = \
	Makefile \
	rudinrca.tex \
	rudinrca-a4.tex \
	$(wildcard rudinrca[0-9].tex rudinrca1[0-9]) \
	trig.tex \
	trigdoc.tex \
	myfancy.tex

SAVEFILES = \
	$(SRCFILES) \
	rudinrca.bib \
	rudinrca-a4.bib \
	trigdoc.bib

SAVETGZ = rudinrca.tar.gz

.PHONY: save
save: $(SAVETGZ)
$(SAVETGZ): $(SAVEFILES)
	tar cfz $@ $(SAVEFILES)
	tar tvfz $@; ls -l $@

# not for relase
-include Make.local
