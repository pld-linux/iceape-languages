# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=2.10
U=http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/$V/langpack/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Iceape
Summary(pl.UTF-8):	Pakiety językowe dla Iceape-a
Name:		iceape-languages
Version:	2.10
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.be.langpack.xpi
# Source0-md5:	5e4e42bd9c479eed512f6816058fd17d
Source1:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ca.langpack.xpi
# Source1-md5:	9aa59f5cb90d7bf4d9e4c23a273aa810
Source2:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.cs.langpack.xpi
# Source2-md5:	a926a9b2198da296ee6eb593485e4f2a
Source3:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.de.langpack.xpi
# Source3-md5:	16cce2b4b16ff666ef3a669a8dc308ca
Source4:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-GB.langpack.xpi
# Source4-md5:	e7a6ddeef43735284252be38f0702b5e
Source5:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-US.langpack.xpi
# Source5-md5:	8c8e3923e999f0e41a11d95131abfcf9
Source6:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-AR.langpack.xpi
# Source6-md5:	facd6b5de9add7e540ca986e07d164c8
Source7:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-ES.langpack.xpi
# Source7-md5:	77fea51830d2496d17354309284067d2
Source8:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fi.langpack.xpi
# Source8-md5:	cab2091d967dc9145a21e33fac2441e6
Source9:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fr.langpack.xpi
# Source9-md5:	aa6f63ec1935672e524d56b69af8fe8a
Source10:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.gl.langpack.xpi
# Source10-md5:	d00bb54eabf09b23fb692cbadc162c32
Source11:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.hu.langpack.xpi
# Source11-md5:	b7fe3a360204886456796f536cae328b
Source12:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.it.langpack.xpi
# Source12-md5:	f4d05ec08ca28e5294c2ab48ce7c8d48
Source13:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ja.langpack.xpi
# Source13-md5:	39cac57c383c81fca6f36219607552d0
Source14:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.lt.langpack.xpi
# Source14-md5:	11a19dc842538daeae0042bfe6a0685a
Source15:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nb-NO.langpack.xpi
# Source15-md5:	fd986c260975c217804520457ace95e0
Source16:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nl.langpack.xpi
# Source16-md5:	52fb982b069a4379a94227ce2a6dcdc7
Source17:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pl.langpack.xpi
# Source17-md5:	5e8532f81e89036611dce7b45a2a962c
Source18:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pt-PT.langpack.xpi
# Source18-md5:	3b48c6a2c972733643063f55218ccfcd
Source19:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ru.langpack.xpi
# Source19-md5:	612b77e19a36a3b41654e1e4da5b1290
Source20:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sk.langpack.xpi
# Source20-md5:	a21171c98c07e43a794ca9daaf9b08cb
Source21:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sv-SE.langpack.xpi
# Source21-md5:	7cc9b9c1b4c3499292965f967d8ac61f
Source22:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.tr.langpack.xpi
# Source22-md5:	3591e44b04e5ec94d9c30662f379545b
Source23:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.uk.langpack.xpi
# Source23-md5:	13bfd8e87e648d1298ee8ca5b1044c5d
Source24:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-CN.langpack.xpi
# Source24-md5:	7ae154000ac553b415d723a5aedcdd97
Source25:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-TW.langpack.xpi
# Source25-md5:	3fbcc45b118c52d98ee2d1344e842609
URL:		http://www.seamonkey-project.org/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		iceapedir	%{_datadir}/iceape

%description
Language packs for Iceape.

%description -l pl.UTF-8
Pakiety językowe dla Iceape-a.

%package -n iceape-lang-be
Summary:	Belarusian resources for Iceape
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-be
Belarusian resources for Iceape.

%description -n iceape-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Iceape-a.

%package -n iceape-lang-ca
Summary:	Catalan resources for Iceape
Summary(ca.UTF-8):	Recursos catalans per Iceape
Summary(es.UTF-8):	Recursos catalanes para Iceape
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-ca
Catalan resources for Iceape.

%description -n iceape-lang-ca -l ca.UTF-8
Recursos catalans per Iceape.

%description -n iceape-lang-ca -l es.UTF-8
Recursos catalanes para Iceape.

%description -n iceape-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Iceape-a.

%package -n iceape-lang-cs
Summary:	Czech resources for Iceape
Summary(pl.UTF-8):	Czeskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-cs
Czech resources for Iceape.

%description -n iceape-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Iceape-a.

%package -n iceape-lang-de
Summary:	German resources for Iceape
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-de
German resources for Iceape.

%description -n iceape-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Iceape-a.

%package -n iceape-lang-en_GB
Summary:	English (British) resources for Iceape
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-en_GB
English (British) resources for Iceape.

%description -n iceape-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Iceape-a.

%package -n iceape-lang-en_US
Summary:	English (American) resources for Iceape
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-en_US
English (American) resources for Iceape.

%description -n iceape-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Iceape-a.

%package -n iceape-lang-es_AR
Summary:	Spanish (Andorra) resources for Iceape
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Iceape
Summary(es.UTF-8):	Recursos españoles (Andorra) para Iceape
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceape-a (wersja dla Andory)
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-es_AR
Spanish (Spain) resources for Iceape.

%description -n iceape-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Iceape.

%description -n iceape-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Iceape.

%description -n iceape-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceape-a (wersja dla Andory).

%package -n iceape-lang-es
Summary:	Spanish (Spain) resources for Iceape
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Iceape
Summary(es.UTF-8):	Recursos españoles (España) para Iceape
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceape-a (wersja dla Hiszpanii)
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-es
Spanish (Spain) resources for Iceape.

%description -n iceape-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Iceape.

%description -n iceape-lang-es -l es.UTF-8
Recursos españoles (España) para Iceape.

%description -n iceape-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceape-a (wersja dla Hiszpanii).

%package -n iceape-lang-fi
Summary:	Finnish resources for Iceape
Summary(pl.UTF-8):	Fińskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-fi
Finnish resources for Iceape.

%description -n iceape-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Iceape-a.

%package -n iceape-lang-fr
Summary:	French resources for Iceape
Summary(pl.UTF-8):	Francuskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-fr
French resources for Iceape.

%description -n iceape-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Iceape-a.

%package -n iceape-lang-gl
Summary:	Galician resources for Iceape
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-gl
Galician resources for Iceape.

%description -n iceape-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Iceape-a.

%package -n iceape-lang-hu
Summary:	Hungarian resources for Iceape
Summary(hu.UTF-8):	Magyar nyelv Iceape-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-hu
Hungarian resources for Iceape.

%description -n iceape-lang-hu -l hu.UTF-8
Magyar nyelv Iceape-hez.

%description -n iceape-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Iceape-a.

%package -n iceape-lang-it
Summary:	Italian resources for Iceape
Summary(pl.UTF-8):	Włoskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-it
Italian resources for Iceape.

%description -n iceape-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Iceape-a.

%package -n iceape-lang-ja
Summary:	Japanese resources for Iceape
Summary(pl.UTF-8):	Japońskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-ja
Japanese resources for Iceape.

%description -n iceape-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Iceape-a.

%package -n iceape-lang-lt
Summary:	Lithuanian resources for Iceape
Summary(pl.UTF-8):	Litewskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-lt
Lithuanian resources for Iceape.

%description -n iceape-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Iceape-a.

%package -n iceape-lang-nb
Summary:	Norwegian Bokmaal resources for Iceape
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-nb
Norwegian Bokmaal resources for Iceape.

%description -n iceape-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Iceape-a.

%package -n iceape-lang-nl
Summary:	Dutch resources for Iceape
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-nl
Dutch resources for Iceape.

%description -n iceape-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Iceape-a.

%package -n iceape-lang-pl
Summary:	Polish resources for Iceape
Summary(pl.UTF-8):	Polskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-pl
Polish resources for Iceape.

%description -n iceape-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Iceape-a.

%package -n iceape-lang-pt
Summary:	Portuguese (Portugal) resources for Iceape
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Iceape-a (wersja dla Portugalii)
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-pt
Portuguese (Portugal) resources for Iceape.

%description -n iceape-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Iceape-a (wersja dla Portugalii).

%package -n iceape-lang-ru
Summary:	Russian resources for Iceape
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-ru
Russian resources for Iceape.

%description -n iceape-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Iceape-a.

%package -n iceape-lang-sk
Summary:	Slovak resources for Iceape
Summary(pl.UTF-8):	Słowackie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-sk
Slovak resources for Iceape.

%description -n iceape-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Iceape-a.

%package -n iceape-lang-sv
Summary:	Swedish resources for Iceape
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-sv
Swedish resources for Iceape.

%description -n iceape-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Iceape-a.

%package -n iceape-lang-tr
Summary:	Turkish resources for Iceape
Summary(pl.UTF-8):	Tureckie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-tr
Turkish resources for Iceape.

%description -n iceape-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Iceape-a.

%package -n iceape-lang-uk
Summary:	Ukrainian resources for Iceape
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-uk
Ukrainian resources for Iceape.

%description -n iceape-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Iceape-a.

%package -n iceape-lang-zh_CN
Summary:	Simplified Chinese resources for Iceape
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-zh_CN
Simplified Chinese resources for Iceape.

%description -n iceape-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Iceape-a.

%package -n iceape-lang-zh_TW
Summary:	Traditional Chinese resources for Iceape
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Iceape-a
Group:		I18n
Requires:	iceape >= %{version}
Provides:	iceape-lang-resources = %{version}

%description -n iceape-lang-zh_TW
Traditional Chinese resources for Iceape.

%description -n iceape-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Iceape-a.

%prep
unpack() {
    local args="$1" file="$2"
	base=$(basename $file)
	local lang=$(basename $file .langpack.xpi)
	lang=${lang##seamonkey-%{version}.}
	install -d $lang

	# rebrand locale for Iceape
	cd $lang
	cp -p $file .
	unzip -q $base install.rdf chrome/$lang/locale/$lang/branding/brand.{dtd,properties}
	sed -i -e 's/SeaMonkey/Iceape/g;' chrome/$lang/locale/$lang/branding/brand.{dtd,properties}
	zip -q0 $base chrome/$lang/locale/$lang/branding/brand.{dtd,properties}
	if ! grep -q "<em:minVersion>%{version}</em:minVersion>" install.rdf; then
		echo "$base most likely doesn't work with iceape %{version}!" >&2
		exit 1
	fi
	%{__rm} -rf chrome install.rdf
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 25 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{iceapedir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .langpack.xpi)
	basename=${basename##seamonkey-%{version}.}
	cp -p $a $RPM_BUILD_ROOT%{iceapedir}/extensions/langpack-$basename@seamonkey.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n iceape-lang-be
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-be@seamonkey.mozilla.org.xpi

%files -n iceape-lang-ca
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-ca@seamonkey.mozilla.org.xpi

%files -n iceape-lang-cs
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-cs@seamonkey.mozilla.org.xpi

%files -n iceape-lang-de
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-de@seamonkey.mozilla.org.xpi

%files -n iceape-lang-en_GB
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-en-GB@seamonkey.mozilla.org.xpi

%files -n iceape-lang-en_US
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-en-US@seamonkey.mozilla.org.xpi

%files -n iceape-lang-es_AR
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-es-AR@seamonkey.mozilla.org.xpi

%files -n iceape-lang-es
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-es-ES@seamonkey.mozilla.org.xpi

%files -n iceape-lang-fi
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-fi@seamonkey.mozilla.org.xpi

%files -n iceape-lang-fr
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-fr@seamonkey.mozilla.org.xpi

%files -n iceape-lang-gl
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-gl@seamonkey.mozilla.org.xpi

%files -n iceape-lang-hu
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-hu@seamonkey.mozilla.org.xpi

%files -n iceape-lang-it
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-it@seamonkey.mozilla.org.xpi

%files -n iceape-lang-ja
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-ja@seamonkey.mozilla.org.xpi

%files -n iceape-lang-lt
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-lt@seamonkey.mozilla.org.xpi

%files -n iceape-lang-nb
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-nb-NO@seamonkey.mozilla.org.xpi

%files -n iceape-lang-nl
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-nl@seamonkey.mozilla.org.xpi

%files -n iceape-lang-pl
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-pl@seamonkey.mozilla.org.xpi

%files -n iceape-lang-pt
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-pt-PT@seamonkey.mozilla.org.xpi

%files -n iceape-lang-ru
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-ru@seamonkey.mozilla.org.xpi

%files -n iceape-lang-sk
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-sk@seamonkey.mozilla.org.xpi

%files -n iceape-lang-sv
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-sv-SE@seamonkey.mozilla.org.xpi

%files -n iceape-lang-tr
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-tr@seamonkey.mozilla.org.xpi

%files -n iceape-lang-uk
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-uk@seamonkey.mozilla.org.xpi

%files -n iceape-lang-zh_CN
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-zh-CN@seamonkey.mozilla.org.xpi

%files -n iceape-lang-zh_TW
%defattr(644,root,root,755)
%{iceapedir}/extensions/langpack-zh-TW@seamonkey.mozilla.org.xpi
