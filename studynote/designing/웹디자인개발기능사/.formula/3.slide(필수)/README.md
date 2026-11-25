# CSS

### Fade

- 굳이 div class="slider s1" 할 필요 없다
- 굳이 CSS에서 background-image:url(); 할 필요 없다
- 그래도 JS 에서 애니메이션 입히려면 div class="slide" 정도는 해야한다

### right

- 마찬가지로 CSS에서는 div로 지목하고, JS에서는 ".slide"로 지목한다

### upward

- 반응형에서 위아래로 움직이려면, 상하 크기를 100%가 아닌 100vh 로 주어야 한다
    - height: calc(100vh - 120px);
    - height: 100vh;
    - marginTop: -currentIndex * 100 + "vh"
- CSS 에서는 sliderWrap 의 display:flex 만 지우면 되고
- JS 에서는 marginLeft 를 marginTop 으로 바꾸고 % 를 px 나 vh 로 바꾸면 된다