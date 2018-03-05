#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmlstarlet
Version  : 1.6.1
Release  : 2
URL      : https://sourceforge.net/projects/xmlstar/files/xmlstarlet/1.6.1/xmlstarlet-1.6.1.tar.gz
Source0  : https://sourceforge.net/projects/xmlstar/files/xmlstarlet/1.6.1/xmlstarlet-1.6.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xmlstarlet-bin
Requires: xmlstarlet-doc
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : sed

%description
XMLStarlet is a command line XML toolkit which can be used to transform,
query, validate, and edit XML documents and files using  simple set of shell
commands in similar way it is done for plain text files  using grep/sed/awk/
tr/diff/patch.

%package bin
Summary: bin components for the xmlstarlet package.
Group: Binaries

%description bin
bin components for the xmlstarlet package.


%package doc
Summary: doc components for the xmlstarlet package.
Group: Documentation

%description doc
doc components for the xmlstarlet package.


%prep
%setup -q -n xmlstarlet-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520290319
%configure --disable-static --with-libxml-include-prefix=/usr/include/libxml2
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1520290319
rm -rf %{buildroot}
%make_install
## make_install_append content
pushd %{buildroot}/usr/bin
ln -sf xml xmlstarlet
popd
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xml
/usr/bin/xmlstarlet

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xmlstarlet/*
%doc /usr/share/man/man1/*
