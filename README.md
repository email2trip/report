# report

Informe TFI.

## Compilación recomendada

## Bibliografía

El archivo de bibliografía que usa el informe es `export.bib` y puede ser usado con BibDesk.

### Línea de comando

Desde la raíz del repo:

```bash
latexmk report.tex
```

Resuelve automáticamente las pasadas de `pdflatex` y `biber` necesarias usando la configuración definida en `.latexmkrc`.

### Limpieza de archivos auxiliares

```bash
latexmk -c report.tex
```

Hace una limpieza parcial: elimina auxiliares de compilación, pero conserva archivos útiles.

Para una limpieza completa del build:

```bash
latexmk -C report.tex
```

Eso también elimina `report.bbl`, `report.pdf` y `report.synctex.gz`.

### TexShop

En TexShop se recomienda utilizar `latexmk`

Se incluye un archivo `.latexmkrc` de forma que TexShop y la compilación por línea de comando desde la terminal usan la misma configuración.