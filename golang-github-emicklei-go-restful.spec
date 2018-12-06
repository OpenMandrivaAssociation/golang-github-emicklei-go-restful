# http://github.com/emicklei/go-restful

%global goipath         github.com/emicklei/go-restful
%global commit          09691a3b6378b740595c1002f40c34dd5f218a22

%gometa -i

Name:           golang-github-emicklei-go-restful
Version:        1.1.3
Release:        0.19%{?dist}
Summary:        Package for building REST-style Web Services using Google Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml
mv swagger/README.md README-swagger.md
mv swagger/CHANGES.md CHANGES-swagger.md

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGES.md README-swagger.md CHANGES-swagger.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1.3-0.18.git09691a3
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1.3-0.17.20161212git09691a3
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.16.git09691a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1.3-0.15.git09691a3
- Bump to upstream 09691a3b6378b740595c1002f40c34dd5f218a22
  related: #1215626

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.14.gitbf50d2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.13.gitbf50d2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.12.gitbf50d2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1.3-0.11.gitbf50d2b
- Bump to upstream bf50d2be18145391aa3d4339b07195807b25a427
  related: #1215626

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-0.10.gitbdfb7d4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-0.9.gitbdfb7d4
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.8.gitbdfb7d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 1.1.3-0.7.gitbdfb7d4
- Update to spec-2.1
  related: #1215626

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 1.1.3-0.6.gitbdfb7d4
- Update spec file to spec-2.0
  related: #1215626

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-0.5.gitbdfb7d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 1.1.3-0.4.gitbdfb7d4
- Bump to upstream bdfb7d41639a84ea7c36df648e5865cd9fbf21e2
  related: #1215626

* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 1.1.3-0.3.gitd487287
- Bump to upstream d4872876992d385f0e69b007f154e5633bdb40af
  related: #1215626

* Mon Apr 27 2015 jchaloup <jchaloup@redhat.com> - 1.1.3-0.2.git03f8ad5
- Bump to upstream 03f8ad5589baf3c67a448fd9354da27419db712d
  resolves: #1215626

* Wed Apr 01 2015 jchaloup <jchaloup@redhat.com> - 1.1.3-0.1.git5e1952e
- Bump to upstream 5e1952ed0806503c059e4463c2654200660f484b
  related: #1164152

* Wed Dec 10 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.git692a500
- update to the latest commit 692a50017a7049b26cf7ea4ccfc0d8c77369a793
  related: #1164152

* Fri Nov 14 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.gitad99b12
- First package for Fedora
  resolves: #1164152

