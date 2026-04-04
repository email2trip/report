# report

Informe TFI.

## Compilación con Latexmk

Se incluye un archivo `.latexmkrc` con la configuración necesaria.

Se resuelve automáticamente las pasadas de `pdflatex` y `biber` necesarias.

### Local

Requisitos
- [TeX Live 2025](https://tug.org/texlive/)
- [latexmk](https://mgeier.github.io/latexmk.html)

#### Creación del PDF

```bash
latexmk report.tex
```

#### Limpieza de archivos auxiliares

```bash
latexmk -c report.tex
```

#### Limpieza completa

```bash
latexmk -C report.tex
```

### Docker

Requisitos
- Docker

#### Construcción de la imagen

```bash
docker build -t report-latex .
```

#### Creación del PDF

Compilar el informe montando el repositorio actual dentro del contenedor:

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/work" report-latex
```
#### Limpieza de archivos auxiliares

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/work" report-latex -c report.tex
```

#### Limpieza completa

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/work" report-latex -C report.tex
```

## TexLive macOS

### TexShop

[TexShop](https://pages.uoregon.edu/koch/texshop/)

En TexShop se recomienda utilizar `latexmk`

### BibDesk

[BibDesk](https://bibdesk.sourceforge.io)

El archivo de bibliografía que usa el informe es `references.bib` y puede ser usado con BibDesk.

## Estructura de archivos LaTeX

El informe está dividido en varios archivos para separar configuración de contenido:

- `report.tex`: archivo raíz del documento.
- `preamble.tex`: paquetes, macros y configuración global.
- `frontmatter/titlepage.tex`: portada.
- `sections/`: secciones del informe.
- `references.bib`: bibliografía usada por `biblatex`/`biber`.
