var card = { suit: "heart", rank: "A"};
console.log(card.suit);
console.log(card["rank"]);
var obj = {};
console.log(obj);
card.value = 14;
console.log(card);
delete card.rank;
console.log(card);

