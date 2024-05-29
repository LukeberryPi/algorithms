// https://leetcode.com/problems/destination-city/description/

// const paths = [
//   ["London", "New York"],
//   ["New York", "Lima"],
//   ["Lima", "Sao Paulo"],
// ];

const paths = [
  ["B", "C"],
  ["D", "B"],
  ["C", "A"],
];

function findDestinationCity(paths) {
  let originCities = [];
  for (let path of paths) {
    originCities.push(path[0]);
  }

  const flat = paths.flat();
  const noOrigins = flat.filter((city) => !originCities.includes(city));

  return noOrigins[0];
}

console.log(findDestinationCity(paths));
