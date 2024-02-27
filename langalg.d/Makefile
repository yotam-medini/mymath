# -*- Makefile -*-

ifneq ($(emv),)
emv:
	@echo $($(emv))
endif

.DELETE_ON_ERROR:

langalg.pdf: langalg.tex mymacs.tex
	pdflatex $<
	makeindex $<
	pdflatex $<

clean:
	rm -f \
	    langalg.ilg \
	    langalg.ind \
	    langalg.log \
            langalg.pdf \
