Summary:     GNOME guile interpreter
Summary(pl): Inetrpreter guile dla GNOME
Name:        gnome-guile
Version:     0.27
Release:     2
Copyright:   LGPL
Group:       X11/Gnome
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         http://www.gnome.org
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gnome

%description
GNOME guile (gnomeg) is a guile interpreter with GTK and GNOME support.
A number of GNOME utilities are written to use gnomeg.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl 
Inetrpreter guile GNOME'a, wiele jego narzêdzi wykorzystuje ten pakiet. 

%package devel
Summary:     GNOME guile libraries, includes, etc
Group:       X11/Gnome
Requires:    %{name} = %{version}

%description devel
Libraries and header files for GNOME guile development

%package static
Summary:     GNOME guile static libraries
Group:       X11/Gnome
Requires:    %{name}-devel = %{version}

%description static
GNOME guile static libraries.

%prep
%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=/usr
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
fi

make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*} || :

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
/usr/bin/*
/usr/lib/lib*.so.*.*

/usr/share/gtk
/usr/share/guile/toolkits/*
/usr/share/guile/gnome
/usr/share/guile/gtk
/usr/share/guile/site/*

%files devel
%defattr(644, root, root, 755)
/usr/lib/lib*.so
/usr/include/*

%files static
%attr(644, root, root) /usr/lib/*.a

%changelog
* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- removed COPYING from %doc,
- added full %attr description in %files,
- added striping shared libraries and binaries.

* Fri Jul 17 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.27-1]
- added pl translation.

* Wed May 27 1998 Michael Fulbright <msf@redhat.com>
- modified file list to include %{prefix}/share/guile, %{prefix}/share/gtk

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-guile CVS source tree.
