%define pkgname cucumber
Summary:	Behaviour Driven Development with elegance and joy
Name:		ruby-%{pkgname}
Version:	10.2.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	19633670a53a456ca40aaa98ae39583e
URL:		https://cucumber.io/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	sed >= 4.0
Requires:	ruby-base64 >= 0.2
Requires:	ruby-builder >= 3.2
Requires:	ruby-cucumber-ci-environment >= 9
Requires:	ruby-cucumber-ci-environment < 12
Requires:	ruby-cucumber-core >= 15
Requires:	ruby-cucumber-core < 17
Requires:	ruby-cucumber-cucumber-expressions >= 17
Requires:	ruby-cucumber-cucumber-expressions < 20
Requires:	ruby-cucumber-html-formatter >= 21
Requires:	ruby-cucumber-html-formatter < 23
Requires:	ruby-diff-lcs >= 1.5
Requires:	ruby-logger >= 1.6
Requires:	ruby-mini_mime >= 1.1
Requires:	ruby-multi_test >= 1.1
Requires:	ruby-sys-uname >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cucumber lets software development teams describe how software should
behave in plain text. The text is written in a business-readable
domain-specific language and serves as documentation, automated tests
and development-aid.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/cucumber
%{ruby_vendorlibdir}/cucumber.rb
%{ruby_vendorlibdir}/cucumber
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
