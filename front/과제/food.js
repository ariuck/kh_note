let total = 0;

// 현재 배경사진 번호
let bgNum = 1;

// 음식 추가
function addFood() {
  let food = document.querySelector("#food").value;

  let cal = document.querySelector("#cal").value;

  if (food === "" || cal === "") {
    alert("음식이랑 칼로리 둘 다 입력해주세요");

    return;
  }

  let list = document.querySelector("#food-list");

  let div = document.createElement("div");

  div.classList.add("food-item");

  div.innerHTML =
    food +
    " / " +
    cal +
    " kcal" +
    "<button onclick='removeFood(this," +
    cal +
    ")'>삭제</button>";

  list.appendChild(div);

  total = total + Number(cal);

  document.querySelector("#total").innerHTML = total;

  let percent = total / 20;

  if (percent > 100) {
    percent = 100;
  }

  document.querySelector("#bar-in").style.width = percent + "%";

  let text = document.querySelector("#cal-text");

  if (total < 700) {
    text.innerHTML = "아직 여유 있음";
  } else if (total < 1500) {
    text.innerHTML = "슬슬 차오르는 중";
  } else if (total < 2000) {
    text.innerHTML = "거의 다 왔습니다";
  } else {
    text.innerHTML = "오늘 목표 칼로리 끝";
  }

  document.querySelector("#food").value = "";

  document.querySelector("#cal").value = "";
}

// 음식 삭제
function removeFood(btn, cal) {
  btn.parentElement.remove();

  total = total - Number(cal);

  document.querySelector("#total").innerHTML = total;

  let percent = total / 20;

  if (percent < 0) {
    percent = 0;
  }

  document.querySelector("#bar-in").style.width = percent + "%";

  let text = document.querySelector("#cal-text");

  if (total < 700) {
    text.innerHTML = "아직 여유 있음";
  } else if (total < 1500) {
    text.innerHTML = "슬슬 차오르는 중";
  } else if (total < 2000) {
    text.innerHTML = "거의 다 왔습니다";
  } else {
    text.innerHTML = "오늘 목표 칼로리 끝";
  }
}

// 랜덤 문구
function randomText() {
  let texts = [
    "그만먹어!",
    "또먹어?",
    "살쪄!",
    "오늘 샐러드 먹어야지?",
    "맛있으면 0칼로리? 겠어?",
    "체중계 ㄱㄱ",
    "으이구...",
  ];

  let num = Math.floor(Math.random() * texts.length);

  document.querySelector("#random-text").innerHTML = texts[num];
}

// 배경사진 변경
function changeBg() {
  bgNum = bgNum + 1;

  if (bgNum > 3) {
    bgNum = 1;
  }

  document.body.style.backgroundImage = "url('background" + bgNum + ".jpg')";
}
