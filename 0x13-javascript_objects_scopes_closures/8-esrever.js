// reverseModule.js

function esrever(list) {
  const length = list.length;
  const middle = Math.floor(length / 2);

  for (let i = 0; i < middle; i++) {
    const temp = list[i];
    list[i] = list[length - 1 - i];
    list[length - 1 - i] = temp;
  }
}

module.exports = { esrever };
