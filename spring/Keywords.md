# Inversion of control(IoC) 제어 역전

IoC는 기존 제어 흐름과 비교하여 [제어 흐름을](https://en.wikipedia.org/wiki/Control_flow) 반전시킵니다 . IoC에서 [컴퓨터 프로그램](https://en.wikipedia.org/wiki/Computer_program) 의 사용자 지정 부분은 일반 [프레임워크](https://en.wikipedia.org/wiki/Software_framework) 에서 제어 흐름을 수신합니다 . 이 디자인 의 [소프트웨어 아키텍처](https://en.wikipedia.org/wiki/Software_architecture) 는 기존의 [절차적 프로그래밍](https://en.wikipedia.org/wiki/Procedural_programming) 과 비교하여 제어를 역전 시킵니다. 기존 프로그래밍에서 프로그램 [호출](https://en.wikipedia.org/wiki/Function_call#Main_concepts) 의 목적을 표현하는 사용자 지정 코드 일반 작업을 처리하기 위해 재사용 가능한 라이브러리로 변환하지만 제어 역전으로 사용자 지정 또는 작업별 코드를 호출하는 것은 프레임워크입니다.



# Dependency injection(DI) 의존성 주입

 [오브젝트](https://en.wikipedia.org/wiki/Object_(computer_science)) 가 호출 의존성에 의존하는 다른 객체를 수신한다. 일반적으로 수신 객체를 [클라이언트](https://en.wikipedia.org/wiki/Client_(computing)) 라고 하고 전달된('주입된') 객체를 [서비스](https://en.wikipedia.org/wiki/Service_(systems_architecture)) 라고 합니다 . 서비스를 클라이언트에 전달하는 코드를 인젝터라고 합니다. 클라이언트가 사용할 서비스를 지정하는 대신 인젝터는 클라이언트에게 사용할 서비스를 알려줍니다. '주입'은 종속성(서비스)을 사용하는 클라이언트로 전달하는 것을 말합니다.

 [제어 역전의](https://en.wikipedia.org/wiki/Inversion_of_control) 광범위한 기술의 한 형태입니다 . 일부 서비스를 호출하려는 클라이언트는 해당 서비스를 구성하는 방법을 알 필요가 없습니다. 대신 클라이언트는 외부 코드(인젝터)에 위임합니다. 클라이언트는 인젝터를 인식하지 못합니다. [[2\]](https://en.wikipedia.org/wiki/Dependency_injection#cite_note-HollywoodPrinciple.c2-2) 인젝터는 인젝터 자체에 의해 존재하거나 구성할 수 있는 서비스를 클라이언트에 전달합니다. 그런 다음 클라이언트는 서비스를 사용합니다.

즉, 클라이언트는 인젝터, 서비스 구성 방법 또는 실제로 사용 중인 서비스에 대해 알 필요가 없습니다. 클라이언트 는 서비스 의 [인터페이스](https://en.wikipedia.org/wiki/Interface_(computing)) 만 알면 됩니다. 이러한 [인터페이스](https://en.wikipedia.org/wiki/Interface_(computing)) 는 클라이언트가 서비스를 사용할 수 있는 방법을 정의하기 때문입니다. 이것은 '사용'의 책임과 '건설'의 책임을 분리합니다.



# Reactive processing

### Reactive

반응형 시스템에는 대기 시간이 짧고 처리량이 많은 워크로드에 이상적인 특정 특성이 있습니다. Project Reactor와 Spring 포트폴리오는 함께 작동하여 개발자가 응답성, 탄력성, 탄력성 및 메시지 중심의 엔터프라이즈급 반응 시스템을 구축할 수 있도록 합니다

### Reactive processing

반응 처리는 개발자가 역압(흐름 제어)을 처리할 수 있는 비차단, 비동기 애플리케이션을 구축할 수 있도록 하는 패러다임입니다.



# Microserves

마이크로서비스는 소프트웨어에 대한 현대적인 접근 방식으로 애플리케이션 코드가 다른 코드와 독립적으로 작고 관리 가능한 조각으로 전달됩니다.



# SpringBoot

Spring Boot is the quickest and most popular way to start Spring projects.



