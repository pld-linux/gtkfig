Summary:	GTKFig
Summary(pl):	GTKFig
Name:		gtkfig
Version:	0.7.0
Release:	1
Copyright:	GPL
Group:		X11/Graphics
Group(pl):	X11/Grafika
Source:		ftp://k332.feld.cvut.cz/pub/local/lemming/%name/current.tgz
BuildRequires:	gtk+
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
GTKFIG is a figure drawing tool. 
It can be used to draw flow-charts, data structure diagrams etc. 
Generally, it should serve as replacement for xfig, which has now (IMHO)
outdated interface. Another program I have inspired by was SmartDraw 
for MS Windows. 

It is commercial software, but you can get demoversion at www.smartdraw.com.

My idea is that GTKFIG would serve for same purpose as SmartDraw. 

%description -l pl

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
