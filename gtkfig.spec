Summary:	GTKFig figure-drawing tools
Summary(pl):	GTKFig
Name:		gtkfig
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://k332.feld.cvut.cz/pub/local/lemming/gtkfig/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libstdc++-devel
URL:		http://k332.feld.cvut.cz/~lemming/projects/gtkfig.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GTKFIG is a figure drawing tool. It can be used to draw flow-charts,
data structure diagrams etc. Generally, it should serve as replacement
for xfig, which has now (IMHO) outdated interface. Another program I
have inspired by was SmartDraw for MS Windows.

It is commercial software, but you can get demoversion at
www.smartdraw.com.

My idea is that GTKFIG would serve for same purpose as SmartDraw.

%description -l pl
GTKFIG jest narzêdziem do rysowania wykresów. Mo¿na go wykorzystaæ do
przygotowywania grafów, diagramów przedstawiaj±cych struktury danych
itd. Ma byæ substytutem programu xfig, którego interfejs -- w opinii
autora -- jest przestarza³y. Program ten jest równie¿ wzorowany na
SmartDraw dla Windows (program ten jest komercyjny, ale wersjê demo
mo¿na uzyskaæ z www.smartdraw.com). GTKFIG ma s³u¿yæ temu samemu, co
SmartDraw.

%prep
%setup -q

%build
CXXFLAGS="%{?debug:-g -O0}%{!?debug:$RPM_OPT_FLAGS} -fpermissive"
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
