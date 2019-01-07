# Notes for contributors to the Journal of Southern Hemisphere Earth Systems Science

<!-- MarkdownTOC -->

- [Editorial Aims & Scope](#editorial-aims--scope)
- [General](#general)
- [How to submit](#how-to-submit)
- [Preparing your manuscript](#preparing-your-manuscript)
  - [Templates](#templates)
    - [Using the JSHESS templates](#using-the-jshess-templates)
  - [Structure](#structure)
    - [Title](#title)
    - [Author name(s)](#author-names)
    - [Author affiliation](#author-affiliation)
    - [Article provenance data](#article-provenance-data)
    - [Abstract](#abstract)
    - [Text](#text)
    - [Figures](#figures)
      - [Referencing figures](#referencing-figures)
    - [Tables](#tables)
    - [Figure and table captions](#figure-and-table-captions)
    - [Corresponding Author Details](#corresponding-author-details)
    - [Acknowledgements](#acknowledgements)
    - [References](#references)
      - [Reference list](#reference-list)
        - [Examples](#examples)
      - [In-text citations](#in-text-citations)
    - [Appendix](#appendix)
  - [Conventions & Nomenclature](#conventions--nomenclature)
    - [Mathematical symbols and formulae](#mathematical-symbols-and-formulae)
    - [Units](#units)
    - [Abbreviations](#abbreviations)

<!-- /MarkdownTOC -->


<a name="editorial-aims--scope"></a>
## Editorial Aims & Scope


<a name="general"></a>
## General

All manuscripts that are submitted to JSHESS must not have been published elsewhere in another publication of any type and in any manner that could be construed as a prior or duplicate publication of the same, or very similar work, nor may they be under consideration for publication elsewhere.

Authors of papers accepted for publication will receive galley proofs only. As JSHESS is an online-only journal, reprints will not be available.

All articles published in JSHESS are published under the terms of the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided appropriate credit is given to the original author(s) and the source, a link to the Creative Commons license is provided, and any changes made are indicated.

<a name="how-to-submit"></a>
## How to submit
Submissions should be made direct to the Managing Editor (TODO) by email. Authors are encouraged to contact the Managing Editor to discuss potential submission prior to drafting their manuscript.

<a name="preparing-your-manuscript"></a>
## Preparing your manuscript

JSHESS is published online as an open access publication. JSHESS does not charge authors page fees to publish their manuscripts, however, in return, JSHESS expects authors to assist in the preparation of manuscripts by using the JSHESS article templates and abiding by the formatting and presentation guidelines below.

<a name="templates"></a>
### Templates

For your convenience, JSHESS provides manuscript templates in two formats:

- Microsoft Word 2007 and above (LINK TODO)
- [LaTeX](https://github.com/timothydsmith/JSHESS-latex-template)

All manuscripts submitted for publication in JSHESS must make use of one of these templates.

<a name="using-the-jshess-templates"></a>
#### Using the JSHESS templates

> **Microsoft Word users:**
>
> *The following instructions are provided for users of Microsoft Word 2010. Users with other versions of Microsoft Word should consult the Word documentation to ensure that they apply the templates correctly.*
>
> 1. Download the [JSHESS Word Template](LINK TODO) to your computer.
> 2. Open Word and click `File > New` to display a list of available templates.
> 3. Choose the option `New from existing`.
> 4. Navigate to where you downloaded the JSHESS template.
> 5. Select the file `JSHESSArticle.dotx` and click `Create New`. This will load a new document using the JSHESS Word Template instead of the default template. You should see a mock article containing guidance on how to layout and style your article.
> 6. Replace the sample content with your own content.

> **LaTeX users:**
>
> 1. Download the [JSHESS LaTeX Template](https://github.com/timothydsmith/JSHESS-latex-template) to your computer.
> 2. Unzip the archive to a new folder in a location that you choose.
> 3. Open either `template.tex` or `template-samplecontent.tex` with your text editor. The files are identical except `template-samplecontent.tex` contains a mock article containing guidance on how to layout and style your article.
> 4. Add your own content to either file.
> 5. Compile to PDF. **NB:** Articles using the JSHESS LaTeX Template must be compiled using the XeTeX (xelatex) typesetting engine to produce the correct fonts. Not using XeTeX is not going to break anything, it just means that your compiled article may look a little different to what it's meant to. The Editorial Office will recompile your article in this instance. XeTeX comes bundled with most LaTeX distributions, so everything will probably work fine, you just need to explicitly invoke it: run xelatex foo.tex (or xetex foo.tex) instead of latex foo.tex (tex foo.tex)


<a name="structure"></a>
### Structure
Each manuscript generally includes the following components, which should be presented in the order listed.

> **Microsoft Word users:**
>
> The appropriate Microsoft Word paragraph style to be used for each section is listed in parentheses after the section name. Microsoft Word paragraph styles can be accessed via the Quick Style Gallery on the Home tab of the Ribbon.

> **LaTeX users:**
>
> The correct styles will be applied when the Tex file is built into a PDF, provided that the appropriate commands are used to identify each section.

<a name="title"></a>
#### Title
> **Microsoft Word style:** Title
>
> **LaTeX command:** `\title`

The title should be both brief and descriptive. It must clearly communicate the nature of the article. Ideally, your title should incorporate a key phrase related to your topic within the first 65 characters.

<a name="author-names"></a>
#### Author name(s)
> **Microsoft Word style:** Authors
>
> **LaTeX command:** `\author`

Individual author names must be listed in the following style: first name then initials with full stops after each initial then last name, followed by any generational suffix. Prefixed and postnominal professional titles and academic qualifications should not be included.

Author names should be listed one after the other without line breaks and separated by commas, with the exception of the last name of a multi-name list, which should be separated by the word "and" without a comma.

Numbers indicating author affiliations (see above) should be included in supertext after each name or after the separating comma, if one is used.

> Example: John D. Smith,<sup>1</sup> Jane. B. Citizen<sup>2</sup> and Joseph C. Doe<sup>3</sup>

Collaborative groups may be included in author lists, however JSHESS currently cannot provide a means for including a listing of individual members of collaborative groups.

<a name="author-affiliation"></a>
#### Author affiliation
> **Microsoft Word style:** Affiliations
>
> **LaTeX command:** `\affiliations`


Each affiliation should be as concise as possible and in general should not constitute a complete address, rather indicate the primary institution of the author(s) and the city and country that the institution is located in.

Each affiliation should be on its own line.

Affiliations should be preceded by the relevant number in supertext that corresponds with the numbers used in the author line above.

<a name="article-provenance-data"></a>
#### Article provenance data
> **Microsoft Word style:** Provenance
>
> **LaTeX command:** `\msreceived` and `\msaccepted`

The date of receipt and acceptance, if acceptable, will be supplied by the Managing Editor.

<a name="abstract"></a>
#### Abstract
> **Microsoft Word style:** Abstract
>
> **LaTeX command:** `\begin{abstract}...\end{abstract}`

An abstract is required at the beginning of each article and, at the discretion of the Editor, at the beginning of appropriate shorter contributions. Authors are reminded to summarise their conclusions in the abstract, as well as the methods used, since abstracts are frequently quoted verbatim in abstracting journals.

Authors are encouraged to think about how the words and phrases that a researcher might use to search for their article and include these words and phrases in their abstract in a natural and contextual manner.

Abstracts may consist of multiple paragraphs if absolutely necessary. Headings should not be used in abstracts.

<a name="text"></a>
#### Text
> **Microsoft Word style:** Normal

For style refer to the publication Style Manual for Authors, Editors and Printers of Australian Government Publications (6<sup>th</sup> edition, 2002), and to recent issues of the journal.

The text should be divided into sections, each with a separate heading.

Section headings may be up to three levels deep. Sections should not be numbered.

> **Microsoft Word users:**
>
> Headings and sub-headings must always use the corresponding Microsoft Word style (Heading 1, Heading 2, and Heading 3).
>
> **LaTeX users:**
>
> Section headings can be achieved with the relevant commands:
> `\section`
> `\subsection`
> `\subsubsection`
>
> The use of `\label` commands is encouraged for section headings to enable easy cross-referencing using the `\ref` command.

<a name="figures"></a>
#### Figures

Please choose the location where you insert your figure into the template wisely. It should be as close as possible to the location of the first reference in the text, but care must be taken to ensure that the image fits on the page and does not introduce extraneous white space into the article.

Authors are strongly encouraged to join multi-part figures into a single image before attempting to insert the figure into the article template.

> **Microsoft Word users:**
>
> Figures can be inserted by clicking on the "Picture" button on the "Insert" tab of the ribbon. Figures must be centre justified on their own line and have text wrapping should be set to "In line with text."
>
> **LaTeX users:**
>
> Refer to `template-samplecontent.tex` for an example of the best way to insert figures into your article.



<a name="referencing-figures"></a>
##### Referencing figures

All figures should be mentioned specifically in the text: e.g. Figure 1.

> **Microsoft Word users:**
>
> References to figures in the text should be achieved with the use of cross-references. Guidance on how to use this feature can be found courtesy of the [website of the International Electrotechnical Commission](http://www.iec.ch/standardsdev/resources/draftingpublications/writing_editing/tips_recommendations_we/cross_references.htm)

> **LaTeX users:**
>
> References to figures in the text should be achieved with the use of the `\ref` command.

<a name="tables"></a>
#### Tables

> **Microsoft Word users:**
>
> Tables can be inserted by clicking on the “Table” button on the “Insert” tab of the Ribbon.
>
> Tables should be styled using the JSHESS Table Style included in the template, accessible via the `Table Tools > Design` tab on the Ribbon. The JSHESS Table Style is listed in the “Custom” group; the style name can be found by hovering your mouse over the style preview image.
>
> All tables should be centre justified on the page, and should only be as wide as is necessary to adequately display the con-tent.
>
> Additional horizontal lines may be added to separate groups of cells, if doing so will aid comprehension (see Table 1). These lines must be added manually by changing the “Border” options for the relevant cells. The Microsoft Office support site has an article that explains how to add borders to tables.

> **LaTeX users:**
>
> Refer to `template-samplecontent.tex` for an example of the best way to insert tables into your article.
>
> Note that by default the JSHESS LaTeX Template provides a custom table environment `JSHESSTable`. This is built on top of the [tabularx](https://www.ctan.org/pkg/tabularx?lang=en) package which provides adjustable-width columns. Refer to the [tabularx package documentation](https://www.ctan.org/pkg/tabularx?lang=en) for more information on how to take advantage of all the options of this package.

Each table must have a brief caption that describes its contents that must be understandable without reference to the text. The captions should be formatted the same as for figures.

<a name="figure-and-table-captions"></a>
#### Figure and table captions
> **Microsoft Word style:** Caption
>
> **LaTeX command:** `\caption`

Each figure must be provided with an adequate caption set above the figure.

Captions and caption labels must be set in the main text not part of the drawing.

Caption labels (e.g. Figure 1) must be separated from the caption text by a single tab character. Punctuation marks should not be used to separate caption labels and the caption text.

> **Microsoft Word users:**
>
> Captions should be added by right clicking on the figure and selecting `Insert caption` or selecting the entire table, right clicking and choosing `Insert caption`. This method will ensure that figures and tables are numbered correctly and that cross-references link to the correct place within the article.

> **LaTeX users:**
>
> Captions must be inserted using the `\caption` command from within a `figure` environment or equivalent.
>
> The use of `\label` commands is encouraged for figures and tables to enable easy cross-referencing using the `\ref` command. Refer to `template-samplecontent.tex` for examples.

<a name="corresponding-author-details"></a>
#### Corresponding Author Details

Details of the corresponding author must be included in the footer of the manuscript on the first page. Details must include:

- Full name (see [Author name(s)](#author-names-microsoft-word-style-authors) above);
- Email address; and
- Full postal address, including country.

> **Microsoft Word users:**
>
> This information can be edited by double clicking on the footer area on the first page and changing the relevant place holder text.

> **LaTeX users:**
>
> This information should be entered using the custom LaTeX commands `\cauthorname`, `\cauthoraddress`, and `\cauthoremail`. The JSHESS LaTeX Template includes these commands as standard.


<a name="acknowledgements"></a>
#### Acknowledgements
The last paragraph of the article is the place to acknowledge people, places, and funding. Acknowledgements can contain multiple paragraphs.

<a name="references"></a>
#### References
<a name="reference-list"></a>
##### Reference list
> **Microsoft Word style:** References
>
> **LaTeX command:** `\bibliography{your-BibTex-file}`

References must be placed at the very end of the article.

References must follow the Harvard referencing style. A [guide to this referencing style](http://www.lib.unimelb.edu.au/recite/citations/printableDocs/Harvard%20Style%20General%20Notes.pdf) is available from the University of Melbourne.

Authors are responsible for the accuracy and completeness of all references.

JSHESS strongly encourages the use of a reference manager such as [Endnote](http://endnote.com/), [Mendeley](https://www.mendeley.com/), or [Zotero](https://www.zotero.org/) to ensure that reference lists are formatted correctly. If you wish to compile your reference list manually, a site like [Harvard Generator](http://www.harvardgenerator.com/) can be helpful to ensure the proper formatting is applied.

<a name="examples"></a>
###### Examples

**Articles**

Budin, G.R. 1985. Interannual variability of Australian snowfall. *Aust. Met. Mag.*, 33, 145-159

Davis, C. J. 2013. Towards the development of long-term winter records for the Snowy Mountains. *Aust. Met. Oceanogr. J.*, 63, 303-313

Fiddes, S. L., Pezza, A. B. and Barras, V. 2014a. Synoptic climatology of extreme precipitation in alpine Australia. *Int. J. Climatol.*, doi: 10.1002/joc.3970

**Books**

Van der Linden, P., Mitchell, J.F.B. and (Eds.) 2009. ENSEMBLES: Climate change and its impacts. Summary of research and results from the ENSEMBLES project. Exeter, UK, Met Office Hadley Centre.

**Conference Papers**

Trewin, B.C. 2010. Site location effects on measured precipitation in highly exposed coastal and alpine environments. *2010 AMOS National Conference, Canberra, 27-29 January 2010.*

<a name="in-text-citations"></a>
##### In-text citations
> **LaTeX users:**
>
> The JSHESS LaTeX Template provides the [natbib](https://www.ctan.org/pkg/natbib?lang=en) package by default, thus the additional in-text citation commands are available, including: `\citet`, `\citeauthor`, and `\citeyear`. A [useful quick reference sheet for the natbib commands](http://merkel.zoneo.net/Latex/natbib.php) is provided by S&eacute;bastien Merkel.

In-text citations citation should consist of the name of the author and the year of publication. Thus, 'according to Halley (1686)', or 'as shown by an earlier study (Halley 1686)'. When there are two or more papers by the same author published in the same year, the distinguishing letters a, b, etc., should be added to the year.


<a name="appendix"></a>
#### Appendix
Lengthy mathematical analyses whose details are subordinate to the main theme of the paper should normally be put into an appendix.

<a name="conventions--nomenclature"></a>
### Conventions & Nomenclature

<a name="mathematical-symbols-and-formulae"></a>
#### Mathematical symbols and formulae
Equations should, where appropriate, be included in-line with the main body text. Where this is not possible, equations should included centre justified on a separate line.  The numbers that identify equations are to be placed at the right-hand margin.

> **Microsoft Word users:**
>
> Properly formatted equations can be easily inserted in the correct format by using the provided JSHESS Equation template. This can be done by clicking the arrow under the `equation` icon on the `Insert` tab on the Ribbon and choosing `JSHESS Equation` from the list of equation templates.

> **LaTeX users:**
>
> Equations can be inserted ad normal using LaTex math mode. Block level equations will be properly styled if they are contained within an equation environment, e.g. `\begin{equation}...\end{equation}`.

References in text to equations should be made by the equation number prefixed by Eqn.

The following guidelines should be followed when using equations:

1. Double-line fractions should not be used in the body of the text. To indicate such fractions, use the solidus (/) or the negative exponent; thus a/b, or ab-1, or b-1a. Double-line fractions should be avoided also in centred equations if they can be expressed conveniently by any of the methods just noted and the resulting equation will appear on only one line.
2. The radical sign should be avoided. To indicate roots, use a fractional positive or negative exponent.
3. Avoid double superscripts or subscripts as well as superscripts attached to the same symbol.
4. Indicate vectors and matrices by placing a wavy line under the symbol. Do not underline any other symbols or use underlining as part of a symbol.
5. When the number e is modified by a complicated exponent, use the symbol exp.
6. In writing units, the solidus (/) may be used instead of negative exponents provided ambiguity is avoided: i.e. either J kg-1 K-1 or J/(kg K) is acceptable, but not J/kg/K. Multiple use of the solidus is never justified.

<a name="units"></a>
#### Units
The International System of Units is standard in the Southern Hemisphere Earth System Science and SI (m, kg, s, K) units should be used throughout.

Words and symbols for units should not be mixed; in general, symbols should be used only when preceded by a number (thus '10 m', but 'several metres').

Unit symbols are not punctuated, i.e. they are not treated as abbreviations; the same symbol is used for both singular and plural.

Note that, although the Kelvin is the unit of temperature in the SI, the degree sign must be used in writing temperatures or temperature differences in the Celsius scale, i.e. '272 K', but '22 &deg;C'.

Day, month and year are written '29 December 1959' (do not abbreviate names of months).

The recommended time zone is Coordinated Universal Time, abbreviated UTC. Time, time zone, day, month and year are written '2330 UTC 29 December 1959', in some instances the use of other time zones is permissible, for example, AEST (150?E meridian civil time).


<a name="abbreviations"></a>
#### Abbreviations
Unless repetitive, abbreviations should be avoided, especially of organisations (write 'World Meteorological Organization' not 'WMO'), and acronyms should be identified with their first use, e.g. 'clear-air turbulence (CAT)'.