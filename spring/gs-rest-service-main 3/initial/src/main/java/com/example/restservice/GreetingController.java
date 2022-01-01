//package com.example.restservive;
//
//import java.util.concurrent.atomic.AtomicLong;
//
//import com.example.restservice.Greeting;
//import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.RequestParam;
//import org.springframework.web.bind.annotation.RestController;
//// 클래스가 컨트롤러로써, 모든 메서드는 view가 아닌 domain object를 반환하게 된다.
//// Greeting 오브젝트는 HTTP message converter가 지원하는 Jackson2가 있고
//// classpath에 있기 때문에 스프링의 MappingJackson2HttpMessageConverter 가 자동으로 선택된다.
//@RestController
//public class GreetingController {
//
//    private static final String template = "Hello, %s!";
//    private final AtomicLong counter = new AtomicLong();
//
//    @GetMapping("/greeting") // /greeting 요청과 greeting() 메서드를 매핑
//    // 쿼리스트링 파라미터 name을 greeting() 메서드의 파라미터로 바인딩
//    public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
//        // 새로운 `Greeting` 오브젝트 & greeting template을 사용하여 반환된 name을 문자열로 반환
//        return new Greeting(counter.incrementAndGet(),
//                String.format(template, name));
//    }
//}

package com.example.restservice;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @GetMapping("/greeting")
    public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
        return new Greeting(counter.incrementAndGet(), String.format(template, name));
    }
}