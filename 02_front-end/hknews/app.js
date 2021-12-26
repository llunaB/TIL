const container = document.getElementById('root');
const ajax = new XMLHttpRequest(); // let은 다른 값 넣을 수 있지만(변수), const는 바꿀 수 없다.(상수) 
const content = document.createElement('div');
const NEWS_URL = 'https://api.hnpwa.com/v0/news/1.json';
const CONTENT_URL = 'https://api.hnpwa.com/v0/item/@id.json';
const store = {
  currentPage: 1,
};

// API로부터 데이터를 받아 반환하는 함수
function getData(url) {
  ajax.open('GET', url, false); // 동기적으로 처리하겠다 true는 비동기
  ajax.send(); // 데이터 가져온다.

  return JSON.parse(ajax.response); // json을 객체화
}

// 글 목록 화면
function newsFeed() {
  const newsFeed = getData(NEWS_URL);
  const newsList = []; // <li> 여러개를 넣는다

  newsList.push('<ul>');

  for(let i = (store.currentPage - 1) * 10; i < store.currentPage * 10; i++) {
    newsList.push(`
      <li>
        <a href="#/show/${newsFeed[i].id}">
          ${newsFeed[i].title} (${newsFeed[i].comments_count})
        </a>
      </li>
    `);
  }

  newsList.push('</ul>');

  // 네비게이션
  newsList.push(`
    <div>
      <a href="#/page/${store.currentPage > 1 ? store.currentPage - 1 : 1}">이전 페이지</a>
      <a href="#/page/${store.currentPage + 1}">다음 페이지</a>
    </div>
  `);

  // 배열을 하나의 문자열로 만들어 innerHTML로 넣어준다
  container.innerHTML = newsList.join('');
}

// 뉴스 내용 함수
function newsDetail() {
  // console.log(location.hash) // #/show/29586970
  const id = location.hash.substr(7); // 29586970
  const newsContent = getData(CONTENT_URL.replace('@id', id));

  container.innerHTML = `
    <h1>${newsContent.title}</h1>
    <div>
      <a href="#/page/${store.currentPage}">목록으로</a>
    </div>
  `;
}

// 글 목록 화면으로 돌아가는 라우터
function router() {
  const routePath = location.hash; // #/page/2

  if (routePath === '') {
    newsFeed();            // 리스트 호출
  } else if (routePath.indexOf('#/page/') >= 0){  // indexOf : -1이면 입력으로 주어진 문자열 없음
    store.currentPage = Number(routePath.substr(7)); // 문자열이라 '2' + '1 '이 되어버림
    newsFeed();        
  } else {
    newsDetail(); // 뉴스내용 호출
  }
}

window.addEventListener('hashchange', router);

router();