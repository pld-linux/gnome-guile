Summary:	GNOME guile interpreter
Summary(pl):	Interpreter guile dla GNOME
Name:		gnome-guile
Version:	0.20
Release:	2
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-guile/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-new_gtkhtml.patch
Patch1:		%{name}-destdir_in_makefiles.patch
URL:		http://www.gnome.org/
BuildRequires:	gnome-http-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkhtml-devel
BuildRequires:	guile-devel
Requires:	gtk+ >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GNOME guile (gnomeg) is a guile interpreter with GTK and GNOME
support. A number of GNOME utilities are written to use gnomeg. GNOME
is the GNU Network Object Model Environment. That's a fancy name but
really GNOME is a nice GUI desktop environment. It makes using your
computer easy, powerful, and easy to configure.

%description -l pl
Interpreter guile dla GNOME. Wiele jego narzêdzi wykorzystuje ten
pakiet.

%package devel
Summary:	GNOME guile includes
Summary(pl):	Pliki nag³ówkowe dla GNOME guile
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for GNOME guile development.

%description devel -l pl
Pliki nag³ówkowe do programowania z u¿yciem GNOME guile.

%package static
Summary:	GNOME guile static libraries
Summary(pl):	Biblioteki statyczne GNOME guile
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME guile static libraries.

%description static -l pl
Biblioteki statyczne GNOME guile.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT%{_datadir}/guile/toolkits/libgtkstubs.so
#ln -s %{_libdir}/libguilegtk.so \
#	$RPM_BUILD_ROOT%{_datadir}/guile/toolkits/libgtkstubs.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_datadir}/gtk
%{_datadir}/guile/toolkits/*
%{_datadir}/guile/gnome
%{_datadir}/guile/gtk
%{_datadir}/guile/site/*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
