# ManyToManyField

## 좋아요 기능 (Like)

## Profile Page

## 팔로우 기능 (Follow)





---

# Intro

![image-20211020220124696](/Users/euijinpang/TIL/django/Model relationship2.assets/image-20211020220124696.png)

이 관계는 1 : N : 1의 관계이다.

Reservation 테이블은 중개 모델이다.

이러한 관계도를 까마귀발 표현법이라 한다.



### ManyToManyField

- 다대다 관계 설정 시 사용하는 모델
- 하나의 필수 위치인자가 필요하다. (두 클래스 중 하나)

```python
# hospitals/models.py

# class Doctor(models.Model):
  	...

# class Patient(models.Model):
		doctors = models.ManyToManyField(Doctor)
  	...
```

- 중개 테이블이 생성된다.
  - hopitals_doctor
  - hospitals_patient
  - hospitals_patient_doctors
    - id : integer
    - patient_id : bigint
    - doctor_id : bigint

```python
# 예약 생성 (참조) : patient1 이 doctor1 에게 예약
patient1.doctors.add(doctor1)

# patient1이 예약한 의사 목록 확인
patient1.doctors.all()

# doctor1에게 예약된 환자 목록 확인
doctor1.patient_set.all()
```

```python
# 예약 생성 (역참조) : doctor1 이 patient2 를 예약
doctor1.patient_set.all(patient2)
```

