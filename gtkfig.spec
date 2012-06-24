Summary:	GTKFig figure-drawing tools
Summary(pl):	GTKFig
Name:		gtkfig
Version:	0.7.0
Release:	1
Copyright:	GPL
Group:		X11/Graphics
Group(pl):	X11/Grafika
Source:		ftp://k332.feld.cvut.cz/pub/local/lemming/gtkfig/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GTKFIG is a figure drawing tool. 
It can be used to draw flow-charts, data structure diagrams etc. 
Generally, it should serve as replacement for xfig, which has now (IMHO)
outdated interface. Another program I have inspired by was SmartDraw 
for MS Windows. 

It is commercial software, but you can get demoversion at www.smartdraw.com.

My idea is that GTKFIG would serve for same purpose as SmartDraw. 

%description -l pl
GTKFIG jest narz�dziem do rysowania wykres�w.
Mo�na go wykorzysta� do przygotowywania graf�w, diagram�w przedstawiaj�cych
struktury danych itd. Ma by� substytutem programu xfig, kt�rego interfejs -- 
w opinii autora -- jest przestarza�y. Program ten jest r�wnie� wzorowany na 
SmartDraw dla Windows (program ten jest komercyjny, ale wersj� demo mo�na 
uzyska� z www.smartdraw.com).
GTKFIG ma s�u�y� temu samemu, co SmartDraw.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
