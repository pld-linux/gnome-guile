Summary:	GNOME guile interpreter
Summary(pl):	Inetrpreter guile dla GNOME
Name:		gnome-guile
Version:	0.27
Release:	1
Copyright:	LGPL
Group:		X11/Gnome
Group(pl):	X11/Gnome
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
Requires:	gtk+ >= 1.2.1
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%description
GNOME guile (gnomeg) is a guile interpreter with GTK and GNOME support.
A number of GNOME utilities are written to use gnomeg.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl 
Inetrpreter guile GNOME'a, wiele jego narzêdzi wykorzystuje ten pakiet. 

%package devel
Summary:	GNOME guile libraries, includes, etc
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and header files for GNOME guile development

%package static
Summary:	GNOME guile static libraries
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME guile static libraries.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*} || :

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

/usr/X11R6/share/gtk
/usr/X11R6/share/guile/toolkits/*
/usr/X11R6/share/guile/gnome
/usr/X11R6/share/guile/gtk
/usr/X11R6/share/guile/site/*

%files devel
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/*

%files static
%attr(644,root,root) /usr/X11R6/lib/*.a
