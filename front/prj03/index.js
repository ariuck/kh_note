async function f01() {
  const resp = await fetch(`http://192.168.40.3:8000/hello`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ nick: "에헤라디아" }),
  });
  const data = await resp.json();
  console.log(data);
}
// 프로트앤드 개발자와 서버 개발자가 통신하는거 구현
