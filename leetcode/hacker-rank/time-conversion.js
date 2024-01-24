// https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

const sampleInput = "12:45:54PM";

function timeConversion(s) {
  const timeCode = s.slice(-2);
  const [hours, minutes, seconds] = s.slice(0, -2).split(":");

  if (timeCode === "AM" && hours === "12") return `00:${minutes}:${seconds}`;
  if (timeCode === "PM" && hours === "12")
    return `${hours}:${minutes}:${seconds}`;
  if (timeCode === "AM") return `${hours}:${minutes}:${seconds}`;
  if (timeCode === "PM") return `${Number(hours) + 12}:${minutes}:${seconds}`;
}

console.log(timeConversion(sampleInput));
