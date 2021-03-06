# Markdown Tistory Uploader

Markdown 타입의 파일을 Github CSS를 적용한 HTML파일로 변환해서 Tistory로 업로드하는 모듈입니다. 

## Prerequisites
- VS Code
- Python >= 3
- Tistory github markdown style 설정
    - css 파일은 [여기](https://github.com/sindresorhus/github-markdown-css)에서 다운로드하면 됩니다.
    - 위에서 다운로드한 css파일을 tistory에 등록해야 합니다.

## Installation

pip install은 지원되지 않습니다.

```shell
$ git clone https://github.com/momentjin/tistory-uploader.git
$ cd tistory-uploader
```

## Usage

### Client Id, Secret Key 발급

[티스토리 App 등록 페이지](https://www.tistory.com/guide/api/manage/register)에서 아래와 같이 서비스URL과 CallBack 값을 설정해주세요.

![config](https://user-images.githubusercontent.com/33324731/76165339-a1c2a500-6199-11ea-8c9c-49714c079f1f.png)

### User Info 설정

1. 아래와 같이 프로젝트 디렉토리에서 다음 명령어를 입력합니다.

```shell
$ ~/tistory-uploader python CommandConfig init
```

2. user.json 파일이 열리면 아래 설명을 보고 내용을 입력합니다.

```json
{
    "blog_name": "",
    "client_id": "",
    "client_secret": "",
    "access_token": "",
    "categories": []
}
```

- blog_name : 블로그 이름 입력. tistory 주소의 앞부분 (예를 들어 momentjin.tistory.com이면 'momentjin' 을 입력)
- client_id : Tistory 앱 등록 페이지의 App ID 입력
- client_secret : Tistory 앱 등록 페이지의 Secret Key 입력
- access_token과 categories는 명령어에 의해 입력됩니다.

### Access Token 발급

1. 아래 커맨드를 입력합니다.

```shell
$ ~/tistory-uploader python CommandConfig code
```

2. 다음 화면에서 블로그 업로드 권한을 얻기 위해 `허가하기` 버튼을 눌러주시면 됩니다.

![authorization](https://user-images.githubusercontent.com/33324731/76165333-9cfdf100-6199-11ea-8a09-c8cb2aed6af3.png)

3. `user.json`에 access_token이 입력된 것을 확인합니다. (현재 문제가 있어 오류 메세지가 보일 수 있습니다. 무시하면 됩니다)

### Category 정보 획득

게시글 쓰기 및 수정 작업시에 카테고리 정보를 포함시키려면, 카테고리 ID를 알아야 합니다. 카테고리 정보 없이 게시글 업로드 작업을 한다면 생략하시면 됩니다.

1. 아래 커맨드를 입력합니다.

```shell
$ ~/tistory-uploader python CommandConfig category
```

2. `user.json`에 categories 데이터가 입력된 것을 확인합니다.

> 게시글 업로드시 카테고리는 카테고리 이름을 입력합니다. 카테고리 이름을 통해 user.json의 카테고리 정보에서 id를 획득한 뒤 이를 API로 전달하는 방식입니다.

### 글 쓰기

1-1. (카테고리 정보가 필요 없는 경우) 아래 커맨드를 입력합니다.

```shell
$ ~/tistory-uploader python CommandConfig write [file_path]
```

1-2. (카테고리 정보가 필요한 경우) 아래 커맨드를 입력합니다. `category_name`는 영문의 경우 대소문자를 명확히 구분해주세요.

```shell
$ ~/tistory-uploader python CommandConfig write [file_path] -cg [category_name]
```

2. 출력 값에 포함된 url에 접속해서 게시글이 제대로 게시되었는지 확인합니다.

### 글 수정

1-1. (카테고리 정보가 필요 없는 경우) 아래 커맨드를 입력합니다.

```shell
$ ~/tistory-uploader python CommandConfig modify [category_name] [file_path]
```

1-2. (카테고리 정보가 필요한 경우) 아래 커맨드를 입력합니다. `category_name`은 영문의 경우 대소문자를 명확히 구분해주세요.

```shell
$ ~/tistory-uploader python CommandConfig modify [category_name] [file_path] -cg [category_name]
```

2. 출력 값에 포함된 url에 접속해서 게시글이 제대로 수정되었는지 확인합니다.

## Release History

v0.1
- 2020.03.08
- Work in progress

## License

Distributed under the MIT License. See [LICENSE](https://github.com/momentjin/tistory-uploader/blob/master/LICENSE) for more information.