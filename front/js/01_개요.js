// window : 전역객체
// indow.alert("hello~~~!");

// x = confirm("ㄹㅇ???");
// console.log(x);

// x = prompt("name ?");
// console.log(x);

// document.write("<h1>zzz</h1>"); 근데 이제 이거 안씀

function f01() {
  // x = document.getElementById("target"); 이거 이제 거의 안씀
  // x = document.getElementsByTagName("h1");이거 이제 거의 안씀
  // x = document.getElementsByClassName("abc");이거 이제 거의 안씀

  // x = document.querySelectorAll("h1");
  // console.log(x);
  // x[0].innerHTML = "hello~~";

  x = document.querySelector("input[name=title]");
  console.log(x.value);
  x.focus();
  x.value = "오늘 점심 오미라";
}
