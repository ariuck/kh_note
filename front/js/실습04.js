// //리스트 중 2번째요소
// const x = document.querySelectorAll("li");
// const a = x[1];
// //클래스가 item인 요소 근데 태그명은 div여야됨
// const b = document.querySelector("div[class=item");
// //폼태그 내 인풋태그 중 네임값이 username인 요소
// const c = document.querySelector("from input[name=username]");
// console.log(a);
// console.log(b);
// console.log(c);
// const x = document.querySelector(".item");
// x.innerHTML = "adfafafaf";
// console.log(x.innerHTML);
// x = document.querySelector("input[type=text]");
// console.log(x.type);
const x = document.querySelector("#target");
console.log(x.classList);
function f01() {
  const x = document.querySelector("#target");
  console.log(x.classList);
  x.classList.toggle("gray");
}
