Summary:	GTKFig
Summary(pl):	GTKFig
Name:		gtkfig
Version:	0.6.0
Release:	1
Copyright:	GPL
Group:		X11/Graphics
Group(pl):	X11/Grafika
Source:		ftp://k332.feld.cvut.cz/pub/local/lemming/%name/current.tgz
#Patch:		
#BuildRequires:	
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
  
%description -l pl

# optional package =====================  

#%package
#Summary:	
#Summary(pl):	
#Group:		
#Group(pl):	
#Vesrion:	

#%description 

#%description -l pl

# end of optional package ==============   

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

# optional package

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
#end of optional package
