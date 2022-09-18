# TIL

> Today I Learned

- 0728
-- Java HashMap 사용하기

- 0917
-- Disk는 Sequential Device 가 아닌 Random Device로 파일을 읽고 쓰기 위해 내부적인 Block으로 쪼갠다.
-- 그리고 이 블록의 조합을 Mater Blocktable에 기록하며, 해당 파일이 00번 block에 있다고 기록한다.
-- NTFS File System은 mater file table과 mirroring file table 2개를 두고, 깨지면 sync를 맞추어 찾는다.
