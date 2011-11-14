# revision 23639
# category Package
# catalog-ctan undef
# catalog-date 2011-06-29 21:13:30 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex
Version:	20110629
Release:	3
Summary:	A TeX macro package that defines LaTeX
Group:		Publishing
URL:		http://tug.org/texlive
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex.source.tar.xz
# revision 23398
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Source3:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin.tar.xz
Source4:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-luatex
Requires:	texlive-pdftex
Requires:	texlive-latexconfig
Requires:	texlive-latex-fonts
Requires:	texlive-latex.bin
%rename tetex-latex
%rename texlive-texmf-latex
%rename texlive-latex-bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
LaTeX is a widely-used macro package for TeX, providing many
basic document formating commands extended by a wide range of
packages. It is a development of Leslie Lamport's original
LaTeX 2.09, and superseded the older system in June 1994. The
basic distribution is catalogued separately, at latex-base;
apart from a large set of contributed packages and third-party
documentation (elsewhere on the archive), the distribution
includes: - a bunch of required packages, which LaTeX authors
are "entitled to assume" will be present on any system running
LaTeX; and - a minimal set of documentation detailing
differences from the 'old' version of LaTeX in the areas of
user commands, font selection and control, class and package
writing, font encodings, configuration options and modification
of LaTeX. For downloading details, see the linked catalogue
entries above.

%pre
    %_texmf_mktexlsr_pre
    %_texmf_fmtutil_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_fmtutil_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
	%_texmf_fmtutil_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_fmtutil_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_fmtutil_d/latex
%{_texmfdistdir}/makeindex/latex/gglo.ist
%{_texmfdistdir}/makeindex/latex/gind.ist
%{_texmfdistdir}/tex/latex/base/alltt.sty
%{_texmfdistdir}/tex/latex/base/ansinew.def
%{_texmfdistdir}/tex/latex/base/applemac.def
%{_texmfdistdir}/tex/latex/base/article.cls
%{_texmfdistdir}/tex/latex/base/article.sty
%{_texmfdistdir}/tex/latex/base/ascii.def
%{_texmfdistdir}/tex/latex/base/bezier.sty
%{_texmfdistdir}/tex/latex/base/bk10.clo
%{_texmfdistdir}/tex/latex/base/bk11.clo
%{_texmfdistdir}/tex/latex/base/bk12.clo
%{_texmfdistdir}/tex/latex/base/book.cls
%{_texmfdistdir}/tex/latex/base/book.sty
%{_texmfdistdir}/tex/latex/base/cp1250.def
%{_texmfdistdir}/tex/latex/base/cp1252.def
%{_texmfdistdir}/tex/latex/base/cp1257.def
%{_texmfdistdir}/tex/latex/base/cp437.def
%{_texmfdistdir}/tex/latex/base/cp437de.def
%{_texmfdistdir}/tex/latex/base/cp850.def
%{_texmfdistdir}/tex/latex/base/cp852.def
%{_texmfdistdir}/tex/latex/base/cp858.def
%{_texmfdistdir}/tex/latex/base/cp865.def
%{_texmfdistdir}/tex/latex/base/decmulti.def
%{_texmfdistdir}/tex/latex/base/doc.sty
%{_texmfdistdir}/tex/latex/base/docstrip.tex
%{_texmfdistdir}/tex/latex/base/exscale.sty
%{_texmfdistdir}/tex/latex/base/fix-cm.sty
%{_texmfdistdir}/tex/latex/base/fixltx2e.sty
%{_texmfdistdir}/tex/latex/base/flafter.sty
%{_texmfdistdir}/tex/latex/base/fleqn.clo
%{_texmfdistdir}/tex/latex/base/fleqn.sty
%{_texmfdistdir}/tex/latex/base/fontenc.sty
%{_texmfdistdir}/tex/latex/base/fontmath.cfg
%{_texmfdistdir}/tex/latex/base/fontmath.ltx
%{_texmfdistdir}/tex/latex/base/fonttext.cfg
%{_texmfdistdir}/tex/latex/base/fonttext.ltx
%{_texmfdistdir}/tex/latex/base/graphpap.sty
%{_texmfdistdir}/tex/latex/base/hyphen.ltx
%{_texmfdistdir}/tex/latex/base/idx.tex
%{_texmfdistdir}/tex/latex/base/ifthen.sty
%{_texmfdistdir}/tex/latex/base/inputenc.sty
%{_texmfdistdir}/tex/latex/base/lablst.tex
%{_texmfdistdir}/tex/latex/base/latex.ltx
%{_texmfdistdir}/tex/latex/base/latex209.def
%{_texmfdistdir}/tex/latex/base/latexbug.tex
%{_texmfdistdir}/tex/latex/base/latexsym.sty
%{_texmfdistdir}/tex/latex/base/latin1.def
%{_texmfdistdir}/tex/latex/base/latin10.def
%{_texmfdistdir}/tex/latex/base/latin2.def
%{_texmfdistdir}/tex/latex/base/latin3.def
%{_texmfdistdir}/tex/latex/base/latin4.def
%{_texmfdistdir}/tex/latex/base/latin5.def
%{_texmfdistdir}/tex/latex/base/latin9.def
%{_texmfdistdir}/tex/latex/base/lcyenc.dfu
%{_texmfdistdir}/tex/latex/base/leqno.clo
%{_texmfdistdir}/tex/latex/base/leqno.sty
%{_texmfdistdir}/tex/latex/base/letter.cls
%{_texmfdistdir}/tex/latex/base/letter.sty
%{_texmfdistdir}/tex/latex/base/lppl.tex
%{_texmfdistdir}/tex/latex/base/ltnews.cls
%{_texmfdistdir}/tex/latex/base/ltpatch.ltx
%{_texmfdistdir}/tex/latex/base/ltxcheck.tex
%{_texmfdistdir}/tex/latex/base/ltxdoc.cls
%{_texmfdistdir}/tex/latex/base/ltxguide.cls
%{_texmfdistdir}/tex/latex/base/ly1enc.dfu
%{_texmfdistdir}/tex/latex/base/macce.def
%{_texmfdistdir}/tex/latex/base/makeidx.sty
%{_texmfdistdir}/tex/latex/base/minimal.cls
%{_texmfdistdir}/tex/latex/base/newlfont.sty
%{_texmfdistdir}/tex/latex/base/next.def
%{_texmfdistdir}/tex/latex/base/nfssfont.tex
%{_texmfdistdir}/tex/latex/base/oldlfont.sty
%{_texmfdistdir}/tex/latex/base/omlcmm.fd
%{_texmfdistdir}/tex/latex/base/omlcmr.fd
%{_texmfdistdir}/tex/latex/base/omlenc.def
%{_texmfdistdir}/tex/latex/base/omllcmm.fd
%{_texmfdistdir}/tex/latex/base/omscmr.fd
%{_texmfdistdir}/tex/latex/base/omscmsy.fd
%{_texmfdistdir}/tex/latex/base/omsenc.def
%{_texmfdistdir}/tex/latex/base/omsenc.dfu
%{_texmfdistdir}/tex/latex/base/omslcmsy.fd
%{_texmfdistdir}/tex/latex/base/omxcmex.fd
%{_texmfdistdir}/tex/latex/base/omxlcmex.fd
%{_texmfdistdir}/tex/latex/base/openbib.sty
%{_texmfdistdir}/tex/latex/base/ot1cmdh.fd
%{_texmfdistdir}/tex/latex/base/ot1cmfib.fd
%{_texmfdistdir}/tex/latex/base/ot1cmfr.fd
%{_texmfdistdir}/tex/latex/base/ot1cmr.fd
%{_texmfdistdir}/tex/latex/base/ot1cmss.fd
%{_texmfdistdir}/tex/latex/base/ot1cmtt.fd
%{_texmfdistdir}/tex/latex/base/ot1cmvtt.fd
%{_texmfdistdir}/tex/latex/base/ot1enc.def
%{_texmfdistdir}/tex/latex/base/ot1enc.dfu
%{_texmfdistdir}/tex/latex/base/ot1lcmss.fd
%{_texmfdistdir}/tex/latex/base/ot1lcmtt.fd
%{_texmfdistdir}/tex/latex/base/ot2enc.dfu
%{_texmfdistdir}/tex/latex/base/ot4enc.def
%{_texmfdistdir}/tex/latex/base/preload.cfg
%{_texmfdistdir}/tex/latex/base/preload.ltx
%{_texmfdistdir}/tex/latex/base/proc.cls
%{_texmfdistdir}/tex/latex/base/proc.sty
%{_texmfdistdir}/tex/latex/base/report.cls
%{_texmfdistdir}/tex/latex/base/report.sty
%{_texmfdistdir}/tex/latex/base/sample2e.tex
%{_texmfdistdir}/tex/latex/base/sfonts.def
%{_texmfdistdir}/tex/latex/base/shortvrb.sty
%{_texmfdistdir}/tex/latex/base/showidx.sty
%{_texmfdistdir}/tex/latex/base/size10.clo
%{_texmfdistdir}/tex/latex/base/size11.clo
%{_texmfdistdir}/tex/latex/base/size12.clo
%{_texmfdistdir}/tex/latex/base/slides.cls
%{_texmfdistdir}/tex/latex/base/slides.def
%{_texmfdistdir}/tex/latex/base/slides.sty
%{_texmfdistdir}/tex/latex/base/small2e.tex
%{_texmfdistdir}/tex/latex/base/syntonly.sty
%{_texmfdistdir}/tex/latex/base/t1cmdh.fd
%{_texmfdistdir}/tex/latex/base/t1cmfib.fd
%{_texmfdistdir}/tex/latex/base/t1cmfr.fd
%{_texmfdistdir}/tex/latex/base/t1cmr.fd
%{_texmfdistdir}/tex/latex/base/t1cmss.fd
%{_texmfdistdir}/tex/latex/base/t1cmtt.fd
%{_texmfdistdir}/tex/latex/base/t1cmvtt.fd
%{_texmfdistdir}/tex/latex/base/t1enc.def
%{_texmfdistdir}/tex/latex/base/t1enc.dfu
%{_texmfdistdir}/tex/latex/base/t1enc.sty
%{_texmfdistdir}/tex/latex/base/t1lcmss.fd
%{_texmfdistdir}/tex/latex/base/t1lcmtt.fd
%{_texmfdistdir}/tex/latex/base/t2aenc.dfu
%{_texmfdistdir}/tex/latex/base/t2benc.dfu
%{_texmfdistdir}/tex/latex/base/t2cenc.dfu
%{_texmfdistdir}/tex/latex/base/testpage.tex
%{_texmfdistdir}/tex/latex/base/texsys.cfg
%{_texmfdistdir}/tex/latex/base/textcomp.sty
%{_texmfdistdir}/tex/latex/base/tracefnt.sty
%{_texmfdistdir}/tex/latex/base/ts1cmr.fd
%{_texmfdistdir}/tex/latex/base/ts1cmss.fd
%{_texmfdistdir}/tex/latex/base/ts1cmtt.fd
%{_texmfdistdir}/tex/latex/base/ts1cmvtt.fd
%{_texmfdistdir}/tex/latex/base/ts1enc.def
%{_texmfdistdir}/tex/latex/base/ts1enc.dfu
%{_texmfdistdir}/tex/latex/base/ucmr.fd
%{_texmfdistdir}/tex/latex/base/ucmss.fd
%{_texmfdistdir}/tex/latex/base/ucmtt.fd
%{_texmfdistdir}/tex/latex/base/ulasy.fd
%{_texmfdistdir}/tex/latex/base/ullasy.fd
%{_texmfdistdir}/tex/latex/base/utf8-test.tex
%{_texmfdistdir}/tex/latex/base/utf8.def
%{_texmfdistdir}/tex/latex/base/utf8enc.dfu
%{_texmfdistdir}/tex/latex/base/utf8test.tex
%{_texmfdistdir}/tex/latex/base/x2enc.dfu
%doc %{_texmfdistdir}/doc/latex/base/00readme.txt
%doc %{_texmfdistdir}/doc/latex/base/alltt.pdf
%doc %{_texmfdistdir}/doc/latex/base/autoload.txt
%doc %{_texmfdistdir}/doc/latex/base/bugs.txt
%doc %{_texmfdistdir}/doc/latex/base/cfgguide.pdf
%doc %{_texmfdistdir}/doc/latex/base/changes.txt
%doc %{_texmfdistdir}/doc/latex/base/classes.pdf
%doc %{_texmfdistdir}/doc/latex/base/clsguide.pdf
%doc %{_texmfdistdir}/doc/latex/base/cmfonts.pdf
%doc %{_texmfdistdir}/doc/latex/base/cyrguide.pdf
%doc %{_texmfdistdir}/doc/latex/base/doc.pdf
%doc %{_texmfdistdir}/doc/latex/base/docstrip.pdf
%doc %{_texmfdistdir}/doc/latex/base/encguide.pdf
%doc %{_texmfdistdir}/doc/latex/base/exscale.pdf
%doc %{_texmfdistdir}/doc/latex/base/fixltx2e.pdf
%doc %{_texmfdistdir}/doc/latex/base/fntguide.pdf
%doc %{_texmfdistdir}/doc/latex/base/graphpap.pdf
%doc %{_texmfdistdir}/doc/latex/base/ifthen.pdf
%doc %{_texmfdistdir}/doc/latex/base/inputenc.pdf
%doc %{_texmfdistdir}/doc/latex/base/latex209.pdf
%doc %{_texmfdistdir}/doc/latex/base/latexsym.pdf
%doc %{_texmfdistdir}/doc/latex/base/lb2.pdf
%doc %{_texmfdistdir}/doc/latex/base/legal.txt
%doc %{_texmfdistdir}/doc/latex/base/letter.pdf
%doc %{_texmfdistdir}/doc/latex/base/lgc2.pdf
%doc %{_texmfdistdir}/doc/latex/base/lppl-1-0.txt
%doc %{_texmfdistdir}/doc/latex/base/lppl-1-1.txt
%doc %{_texmfdistdir}/doc/latex/base/lppl-1-2.txt
%doc %{_texmfdistdir}/doc/latex/base/lppl.pdf
%doc %{_texmfdistdir}/doc/latex/base/lppl.txt
%doc %{_texmfdistdir}/doc/latex/base/ltnews.pdf
%doc %{_texmfdistdir}/doc/latex/base/ltx3info.pdf
%doc %{_texmfdistdir}/doc/latex/base/ltxcheck.pdf
%doc %{_texmfdistdir}/doc/latex/base/ltxdoc.pdf
%doc %{_texmfdistdir}/doc/latex/base/makeindx.pdf
%doc %{_texmfdistdir}/doc/latex/base/manifest.txt
%doc %{_texmfdistdir}/doc/latex/base/manual.pdf
%doc %{_texmfdistdir}/doc/latex/base/modguide.pdf
%doc %{_texmfdistdir}/doc/latex/base/newlfont.pdf
%doc %{_texmfdistdir}/doc/latex/base/oldlfont.pdf
%doc %{_texmfdistdir}/doc/latex/base/patches.txt
%doc %{_texmfdistdir}/doc/latex/base/proc.pdf
%doc %{_texmfdistdir}/doc/latex/base/slides.pdf
%doc %{_texmfdistdir}/doc/latex/base/slifonts.pdf
%doc %{_texmfdistdir}/doc/latex/base/source2e.pdf
%doc %{_texmfdistdir}/doc/latex/base/syntonly.pdf
%doc %{_texmfdistdir}/doc/latex/base/tex2.txt
%doc %{_texmfdistdir}/doc/latex/base/texpert.txt
%doc %{_texmfdistdir}/doc/latex/base/tlc2.pdf
%doc %{_texmfdistdir}/doc/latex/base/usrguide.pdf
%doc %{_texmfdistdir}/doc/latex/base/utf8ienc.pdf
%doc %{_texmfdistdir}/doc/latex/base/webcomp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/base/alltt.dtx
%doc %{_texmfdistdir}/source/latex/base/alltt.ins
%doc %{_texmfdistdir}/source/latex/base/autoload.ins
%doc %{_texmfdistdir}/source/latex/base/cfgguide.tex
%doc %{_texmfdistdir}/source/latex/base/classes.dtx
%doc %{_texmfdistdir}/source/latex/base/classes.ins
%doc %{_texmfdistdir}/source/latex/base/clsguide.tex
%doc %{_texmfdistdir}/source/latex/base/cmextra.ins
%doc %{_texmfdistdir}/source/latex/base/cmfonts.fdd
%doc %{_texmfdistdir}/source/latex/base/cmfonts.ins
%doc %{_texmfdistdir}/source/latex/base/cyrguide.tex
%doc %{_texmfdistdir}/source/latex/base/doc.dtx
%doc %{_texmfdistdir}/source/latex/base/docstrip.dtx
%doc %{_texmfdistdir}/source/latex/base/docstrip.ins
%doc %{_texmfdistdir}/source/latex/base/ec.ins
%doc %{_texmfdistdir}/source/latex/base/encguide.tex
%doc %{_texmfdistdir}/source/latex/base/exscale.dtx
%doc %{_texmfdistdir}/source/latex/base/exscale.ins
%doc %{_texmfdistdir}/source/latex/base/fixltx2e.dtx
%doc %{_texmfdistdir}/source/latex/base/fixltx2e.ins
%doc %{_texmfdistdir}/source/latex/base/fntguide.tex
%doc %{_texmfdistdir}/source/latex/base/fontdef.dtx
%doc %{_texmfdistdir}/source/latex/base/format.ins
%doc %{_texmfdistdir}/source/latex/base/graphpap.dtx
%doc %{_texmfdistdir}/source/latex/base/graphpap.ins
%doc %{_texmfdistdir}/source/latex/base/ifthen.dtx
%doc %{_texmfdistdir}/source/latex/base/ifthen.ins
%doc %{_texmfdistdir}/source/latex/base/inputenc.dtx
%doc %{_texmfdistdir}/source/latex/base/inputenc.ins
%doc %{_texmfdistdir}/source/latex/base/latex209.dtx
%doc %{_texmfdistdir}/source/latex/base/latex209.ins
%doc %{_texmfdistdir}/source/latex/base/latexbug.el
%doc %{_texmfdistdir}/source/latex/base/latexsym.dtx
%doc %{_texmfdistdir}/source/latex/base/latexsym.ins
%doc %{_texmfdistdir}/source/latex/base/lb2.err
%doc %{_texmfdistdir}/source/latex/base/letter.dtx
%doc %{_texmfdistdir}/source/latex/base/letter.ins
%doc %{_texmfdistdir}/source/latex/base/lgc2.err
%doc %{_texmfdistdir}/source/latex/base/ltalloc.dtx
%doc %{_texmfdistdir}/source/latex/base/ltbibl.dtx
%doc %{_texmfdistdir}/source/latex/base/ltboxes.dtx
%doc %{_texmfdistdir}/source/latex/base/ltclass.dtx
%doc %{_texmfdistdir}/source/latex/base/ltcntrl.dtx
%doc %{_texmfdistdir}/source/latex/base/ltcounts.dtx
%doc %{_texmfdistdir}/source/latex/base/ltdefns.dtx
%doc %{_texmfdistdir}/source/latex/base/ltdirchk.dtx
%doc %{_texmfdistdir}/source/latex/base/lterror.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfiles.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfinal.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfloat.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfntcmd.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfssbas.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfsscmp.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfssdcl.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfssini.dtx
%doc %{_texmfdistdir}/source/latex/base/ltfsstrc.dtx
%doc %{_texmfdistdir}/source/latex/base/lthyphen.dtx
%doc %{_texmfdistdir}/source/latex/base/ltidxglo.dtx
%doc %{_texmfdistdir}/source/latex/base/ltlength.dtx
%doc %{_texmfdistdir}/source/latex/base/ltlists.dtx
%doc %{_texmfdistdir}/source/latex/base/ltlogos.dtx
%doc %{_texmfdistdir}/source/latex/base/ltmath.dtx
%doc %{_texmfdistdir}/source/latex/base/ltmiscen.dtx
%doc %{_texmfdistdir}/source/latex/base/ltnews01.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews02.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews03.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews04.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews05.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews06.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews07.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews08.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews09.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews10.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews11.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews12.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews13.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews14.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews15.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews16.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews17.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews18.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews19.tex
%doc %{_texmfdistdir}/source/latex/base/ltnews20.tex
%doc %{_texmfdistdir}/source/latex/base/ltoutenc.dtx
%doc %{_texmfdistdir}/source/latex/base/ltoutenc.ins
%doc %{_texmfdistdir}/source/latex/base/ltoutput.dtx
%doc %{_texmfdistdir}/source/latex/base/ltpage.dtx
%doc %{_texmfdistdir}/source/latex/base/ltpageno.dtx
%doc %{_texmfdistdir}/source/latex/base/ltpar.dtx
%doc %{_texmfdistdir}/source/latex/base/ltpictur.dtx
%doc %{_texmfdistdir}/source/latex/base/ltplain.dtx
%doc %{_texmfdistdir}/source/latex/base/ltsect.dtx
%doc %{_texmfdistdir}/source/latex/base/ltspace.dtx
%doc %{_texmfdistdir}/source/latex/base/lttab.dtx
%doc %{_texmfdistdir}/source/latex/base/ltthm.dtx
%doc %{_texmfdistdir}/source/latex/base/ltvers.dtx
%doc %{_texmfdistdir}/source/latex/base/ltx3info.tex
%doc %{_texmfdistdir}/source/latex/base/ltxdoc.dtx
%doc %{_texmfdistdir}/source/latex/base/ltxref.dtx
%doc %{_texmfdistdir}/source/latex/base/makeindx.dtx
%doc %{_texmfdistdir}/source/latex/base/makeindx.ins
%doc %{_texmfdistdir}/source/latex/base/manual.err
%doc %{_texmfdistdir}/source/latex/base/modguide.tex
%doc %{_texmfdistdir}/source/latex/base/newdc.ins
%doc %{_texmfdistdir}/source/latex/base/newlfont.dtx
%doc %{_texmfdistdir}/source/latex/base/nfssfont.dtx
%doc %{_texmfdistdir}/source/latex/base/nfssfont.ins
%doc %{_texmfdistdir}/source/latex/base/olddc.ins
%doc %{_texmfdistdir}/source/latex/base/oldlfont.dtx
%doc %{_texmfdistdir}/source/latex/base/preload.dtx
%doc %{_texmfdistdir}/source/latex/base/proc.dtx
%doc %{_texmfdistdir}/source/latex/base/proc.ins
%doc %{_texmfdistdir}/source/latex/base/slides.dtx
%doc %{_texmfdistdir}/source/latex/base/slides.ins
%doc %{_texmfdistdir}/source/latex/base/slifonts.fdd
%doc %{_texmfdistdir}/source/latex/base/source2e.tex
%doc %{_texmfdistdir}/source/latex/base/syntonly.dtx
%doc %{_texmfdistdir}/source/latex/base/syntonly.ins
%doc %{_texmfdistdir}/source/latex/base/tlc2.err
%doc %{_texmfdistdir}/source/latex/base/unpack.ins
%doc %{_texmfdistdir}/source/latex/base/usrguide.tex
%doc %{_texmfdistdir}/source/latex/base/utf8ienc.dtx
%doc %{_texmfdistdir}/source/latex/base/webcomp.err
%doc %{_mandir}/man1/latex.1*
%doc %{_texmfdir}/doc/man/man1/latex.man1.pdf
%doc %{_mandir}/man1/pdflatex.1*
%doc %{_texmfdir}/doc/man/man1/pdflatex.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2 -a3 -a4

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/latex <<EOF
latex pdftex language.dat -translate-file=cp227.tcx *latex.ini
pdflatex pdftex language.dat -translate-file=cp227.tcx *pdflatex.ini
dvilualatex luatex language.dat,language.dat.lua dvilualatex.ini
lualatex luatex language.dat,language.dat.lua lualatex.ini
EOF
