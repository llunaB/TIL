# setting

> vscode setting

### install

https://code.visualstudio.com/

- window의 경우 설치시 기타 체크

  - "Code로 열기" 작업을 Windows 탐색기 파일의 상황에 맞는 메뉴에 추가
  - "Code로 열기" 작업을 Windows 탐색기 디렉터리의 상황에 맞는 메뉴에 추가
  - PATH에 추가

  

### python extention

- 파이썬 익스텐션 설치
- 파이썬 환경설정 코드 작성, `editor tabsize` 설정

`ctrl(command) + shift + p` → `json` 검색 → `Preferences: Open Settings (JSON)` 선택

```jsx
// settings.json

{
    ... 생략 ...,

    **"editor.tabSize": 2,

    // python
    "[python]": {
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    },
    "python.languageServer": "Pylance",
    "python.analysis.extraPaths": ["./sources"],**
}
```



###  vscode default terminal 변경

```bash
git bash 사전설치 필수!!
```

1. `ctrl(command) + shift + p` → `default` 검색 → `Terminal: Select Default Profile` 선택 → `Git bash` 선택

2. `ctrl(command) + shift + p` → `json` 검색 → `Preferences: Open Settings (JSON)` 선택

3. 하단 코드 작성 (windows)

   ```json
   // settings.json
   
   {
       ... 생략 ...,
   
       **"terminal.integrated.profiles.windows": {
           "PowerShell": null,
           "Windows PowerShell": null,
           "Command Prompt": null,
           "Git Bash": {
               "source": "Git Bash",
               "path": "C:\\\\Program Files\\\\Git\\\\bin\\\\bash.exe",
           }
       },
       "terminal.integrated.defaultProfile.windows": "Git Bash"**
   }
   ```

4. 하단 코드 작성(mac)

   ```json
   // settings.json
   
   {
       ... 생략 ...,
   
       **"terminal.integrated.profiles.windows": {
           "PowerShell": null,
           "Windows PowerShell": null,
           "Command Prompt": null,
           "Git Bash": {
               "source": "Git Bash",
               "path": "C:\\\\Program Files\\\\Git\\\\bin\\\\bash.exe",
           }
       },
       "terminal.integrated.defaultProfile.windows": "Git Bash"**
   }
   ```

