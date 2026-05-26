# report - email2trip

Informe TFI.

## Compilación con Latexmk

Se incluye un archivo `.latexmkrc` con la configuración necesaria.

Se resuelve automáticamente las pasadas de `pdflatex` y `biber` necesarias.

### Local

Requisitos
- [TeX Live 2026](https://tug.org/texlive/)
  - [latexmk](https://mgeier.github.io/latexmk.html)
  - [chktex](https://www.nongnu.org/chktex/) Opcional para comprobar la sintaxis de LaTeX

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

# Diagrama de Arquitectura

El diagrama de arquitectura se genera con [mingrammer/diagrams](https://diagrams.mingrammer.com) y está ubicado en `docs/`.

Para crearlo ejecutar los siguientes comandos:

```bash
cd docs/
brew install graphviz
uv sync --group diagrams
uv run diagram.py
```
Los íconos fueron obtenidos de https://svgl.app/

## Exportar a Word con Pandoc

Requisitos
- [pandoc](https://pandoc.org/)

Instalación en macOS con Homebrew:

```bash
brew install pandoc
```

Creación del archivo `report.docx` con `pandoc`:

```bash
pandoc report.tex \
  --from=latex \
  --to=docx \
  --output=report.docx \
  --resource-path=. \
  --bibliography=references.bib \
  --citeproc
```
