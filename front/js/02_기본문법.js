// function f01() {
//   const x = 10;
//   // 변수 만들때 그냥 만들면 안되고 스코프 달아야함 var, let, const
//   // var은 문제가 많아서 잘 안쓰고 let ,const를 씀 차이는 재할당여부 let은 가능 const는 불가능
//   console.log(x);
// }

// 타입
// const x = []; //배열

// 객체
// const x ={
//   title : "해리포터",
//   price : 3000,
// }

// 함수
// comst x = function f01(){}

// const result = 1 +1;
// console.log(result)

// Number('1')
// parseInt('1')
// parseFloat('3.14')

// const x = 3;

// if (x > 0) {
//   console.log("plus~~~");
// } else if (x == 0) {
//   console.log("zero");
// } else {
//   console.log("minus~~~");
// }

// for (let i = 0; i < 10; ++i) {
//   console.log(i);
// }

// let i =0;
// while (i<10){
//   console.log("zzz")
//   i+=1
// }
//숫자 받아서 plus,zero,minus출력
// function num() {
//   const x = Number(prompt("숫자를 입력하세요"));
//   if (x > 0) {
//     console.log("plus");
//   } else if (x == 0) {
//     console.log("zero");
//   } else {
//     console.log("minus");
//   }
// }
// num();

// //숫자 받아서 홀 짝 판단
// function holjjak() {
//   const x = Number(prompt("숫자 입력"));
//   if (x % 2 == 0) {
//     console.log("짝");
//   } else {
//     console.log("홀");
//   }
// }
// holjjak();

//나이를 입력받아서 성인인지 판단
// function old() {
//   const x = Number(prompt("나이 입력"));
//   if (x < 20) {
//     console.log("미성년자");
//   } else {
//     console.log("성인");
//   }
// }
// old();

// //hello world출력 무한반복
// i = 0;
// function infi() {
//   while (i++ < 10) {
//     console.log("hello world");
//   }
// }
// infi();
for (let x = 0; x < 10; x++) {
  console.log("hello world ~ !");
}
