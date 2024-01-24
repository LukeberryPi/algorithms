// https://www.codewars.com/kata/550f22f4d758534c1100025a/javascript

const sampleInput = ".... . -.--   .--- ..- -.. .";

const MORSE_CODE = {
  ".-": "A",
  "-...": "B",
  "-.-.": "C",
  "-..": "D",
  ".": "E",
  "..-.": "F",
  "--.": "G",
  "....": "H",
  "..": "I",
  ".---": "J",
  "-.-": "K",
  ".-..": "L",
  "--": "M",
  "-.": "N",
  "---": "O",
  ".--.": "P",
  "--.-": "Q",
  ".-.": "R",
  "...": "S",
  "-": "T",
  "..-": "U",
  "...-": "V",
  ".--": "W",
  "-..-": "X",
  "-.--": "Y",
  "--..": "Z",
  "-----": "0",
  ".----": "1",
  "..---": "2",
  "...--": "3",
  "....-": "4",
  ".....": "5",
  "-....": "6",
  "--...": "7",
  "---..": "8",
  "----.": "9",
  "/": " ",
};

function decodeMorse(morseCode) {
  let answer = "";
  const wordListInMorseCode = morseCode.trim().split("   ");

  for (word of wordListInMorseCode) {
    const letters = word.split(" ");
    for (const letter of letters) {
      const toMorse = MORSE_CODE[letter]
      answer += toMorse;
    }
    answer += " ";
  }

  return answer.trim();
}

console.log(decodeMorse(sampleInput));
