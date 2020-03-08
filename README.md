# Markdown Tistory Uploader

Markdown 타입의 파일을 Github CSS를 적용한 HTML파일로 변환해서 Tistory로 업로드하는 모듈입니다.

## Installation

pip install은 준비중입니다..

```shell
$ git clone https://github.com/momentjin/tistory-uploader.git
```
## Usage

### Client Id, Secret Key 발급

[티스토리 App 등록 페이지](https://www.tistory.com/guide/api/manage/register)에서 아래와 같이 서비스URL과 CallBack 값을 설정해주세요.

![config](./resource/config.png)

### Access Token 발급

```shell
$ ~/tistory-uploader python CommandConfig token
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)