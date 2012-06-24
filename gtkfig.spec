Summary:	GTKFig figure-drawing tools
Summary(pl):	GTKFig - narz�dzia do rysowania wykres�w
Name:		gtkfig
Version:	0.7.0
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://k332.feld.cvut.cz/pub/local/lemming/gtkfig/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://k332.feld.cvut.cz/~lemming/projects/gtkfig.html
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GTKFIG is a figure drawing tool. It can be used to draw flow-charts,
data structure diagrams etc. Generally, it should serve as replacement
for xfig, which has now (IMHO) outdated interface. Another program I
have inspired by was SmartDraw for MS Windows (it is commercial
software, but you can get demoversion at http://www.smartdraw.com/).
My idea is that GTKFIG would serve for same purpose as SmartDraw.

%description -l pl
GTKFIG jest narz�dziem do rysowania wykres�w. Mo�na go wykorzysta� do
przygotowywania graf�w, diagram�w przedstawiaj�cych struktury danych
itd. Ma by� substytutem programu xfig, kt�rego interfejs - w opinii
autora - jest przestarza�y. Program ten jest r�wnie� wzorowany na
SmartDraw dla Windows (program ten jest komercyjny, ale wersj� demo
mo�na uzyska� z http://www.smartdraw.com/). GTKFIG ma s�u�y� temu
samemu, co SmartDraw.

%prep
%setup -q

%build
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fpermissive"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics

gzip -9nf AUTHORS ChangeLog HINTS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/%{name}.desktop
