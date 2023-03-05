# mybatis_springboot_starter ver.

### mySQL과 mybatis springboot starter 를 사용하는 버젼

데이터소스 연동, sql session생성, session template 생략하는 간단한 라이브러리 버젼

- pom.xml 에서 dependency 설정

```
		<dependency>
		    <groupId>com.mysql</groupId>
		    <artifactId>mysql-connector-j</artifactId>
		</dependency>
		
		<!-- https://mvnrepository.com/artifact/org.mybatis.spring.boot/mybatis-spring-boot-starter -->
		<dependency>
		    <groupId>org.mybatis.spring.boot</groupId>
		    <artifactId>mybatis-spring-boot-starter</artifactId>
		    <version>3.0.1</version>
		</dependency>
```



- application.properties

```
spring.datasource.url=jdbc:mysql://localhost:3306/spring/UserProfile?useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Seoul
spring.datasource.username=root
spring.datasource.password=
```



- Mapper.java

```java
@Mapper
public interface UserProfileMapper {
	@Select("SELECT * FROM UserProfile WHERE id=#{id}")
	UserProfile getUserProfile(@Param("id") String id);
	
}

```



- Controller.java

```java
@RestController
public class UserProfileController {
	
	private UserProfileMapper mapper;
	
	public UserProfileController(UserProfileMapper mapper) {
		this.mapper = mapper;
	}
	
	@GetMapping("/user/{id}")
	public UserProfile getUserProfile(@PathVariable("id") String id) {
		return mapper.getUserProfile(id);
	}

}
```

