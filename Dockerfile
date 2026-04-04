FROM texlive/texlive:latest

WORKDIR /work

ENTRYPOINT ["latexmk"]

CMD ["report.tex"]
