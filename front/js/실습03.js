function f01(x) {
  console.log(x);
}
function change() {
  const divtag = document.querySelector("div");
  if (divtag.classList.contains("abc")) {
    divtag.classList.remove("abc");
  } else {
    divtag.classList.add("abc");
  }
}
