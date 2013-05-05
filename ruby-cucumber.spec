%define	pkgname	cucumber
Summary:	Tool to execute plain-text documents as functional tests
Name:		ruby-%{pkgname}
Version:	1.2.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	891940571d5ff073da27e415b2b0db31
URL:		http://cukes.info/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-builder >= 2.1.2
Requires:	ruby-diff-lcs >= 1.1.3
Requires:	ruby-gherkin < 2.12
Requires:	ruby-gherkin >= 2.11.0
Requires:	ruby-json >= 1.4.6
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%{__rm} $RPM_BUILD_ROOT%{ruby_vendorlibdir}/README.rdoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md History.md LICENSE
%attr(755,root,root) %{_bindir}/cucumber
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}

%{ruby_vendorlibdir}/autotest/cucumber.rb
%{ruby_vendorlibdir}/autotest/cucumber_mixin.rb
%{ruby_vendorlibdir}/autotest/cucumber_rails.rb
%{ruby_vendorlibdir}/autotest/cucumber_rails_rspec.rb
%{ruby_vendorlibdir}/autotest/cucumber_rails_rspec2.rb
%{ruby_vendorlibdir}/autotest/cucumber_rspec.rb
%{ruby_vendorlibdir}/autotest/cucumber_rspec2.rb
%{ruby_vendorlibdir}/autotest/discover.rb
