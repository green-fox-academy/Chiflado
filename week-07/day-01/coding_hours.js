// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

let coding_hours = 6 * (17 * 5);

console.log(coding_hours);

let every_hour = 52 * 17;
let coding_percentage = coding_hours / every_hour * 100;
let coding_percentage2 = (6 * 5) / 52 * 100;

console.log(coding_percentage);
console.log(coding_percentage2);
